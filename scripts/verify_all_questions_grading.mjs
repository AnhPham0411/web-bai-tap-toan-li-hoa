import fs from 'fs';
import * as grade from '../assets/js/grade.js';

const manifest = JSON.parse(fs.readFileSync('data/manifest.json', 'utf-8'));
let totalVerifiedQuestions = 0;
let errors = [];

for (const subj of manifest.subjects.filter(s => s.available)) {
  const index = JSON.parse(fs.readFileSync(`data/${subj.path}/index.json`, 'utf-8'));
  for (const qs of index.questionSets) {
    const qdata = JSON.parse(fs.readFileSync(`data/${subj.path}/${qs.file}`, 'utf-8'));
    for (const q of qdata.questions) {
      if (qs.type === 'multiple-choice') {
        const shuffled = grade.shuffleChoices(q);
        if (!shuffled.choices || shuffled.choices.length !== 4) {
          errors.push(`[${q.id}] choices count != 4`);
        }
        if (!grade.isCorrect(shuffled, 'multiple-choice', shuffled.answer)) {
          errors.push(`[${q.id}] correct answer grading failed`);
        }
      } else if (qs.type === 'short-answer') {
        const correctAns = String(q.answer);
        if (!grade.isCorrect(q, 'short-answer', correctAns)) {
          errors.push(`[${q.id}] short answer grading failed on "${correctAns}"`);
        }
        const formatted = grade.formatAnswer(q, 'short-answer');
        if (!formatted || formatted.length === 0) {
          errors.push(`[${q.id}] formatAnswer is empty`);
        }
      }
      totalVerifiedQuestions++;
    }
  }
}

if (errors.length > 0) {
  console.error(`Found ${errors.length} errors:`, errors.slice(0, 10));
  process.exit(1);
} else {
  console.log(`100% SUCCESS: Verified grading & formatting on all ${totalVerifiedQuestions} questions across all 6 subjects!`);
}
