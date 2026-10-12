import fs from 'fs';
import { renderTheory } from '../assets/js/views/theory.js';

const manifest = JSON.parse(fs.readFileSync('data/manifest.json', 'utf-8'));
globalThis.localStorage = { getItem: () => null, setItem: () => {} };

let tested = 0;
for (const subj of manifest.subjects.filter(s => s.available)) {
  const index = JSON.parse(fs.readFileSync(`data/${subj.path}/index.json`, 'utf-8'));
  const ctx = { subject: subj, index };
  
  for (const ch of index.chapters) {
    const theoryPath = `data/${subj.path}/${ch.theory}`;
    if (!fs.existsSync(theoryPath)) {
      throw new Error(`Theory file does not exist: ${theoryPath}`);
    }
    const theoryData = JSON.parse(fs.readFileSync(theoryPath, 'utf-8'));
    globalThis.fetch = async () => ({ ok: true, json: async () => theoryData });
    
    for (const ls of ch.lessons) {
      try {
        const html = await renderTheory(ctx, { chapterId: ch.id, lessonId: ls.id });
        if (!html || html.length < 100) throw new Error('Render output too short');
        tested++;
      } catch (err) {
        console.error(`ERROR rendering ${subj.id} / ${ch.id} / ${ls.id}:`, err);
        process.exit(1);
      }
    }
  }
}
console.log(`100% SUCCESS: Rendered all ${tested} lessons across all active subjects without any error!`);
