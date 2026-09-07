import fs from 'fs';
import path from 'path';
import { mathHtml } from '../assets/js/math.js';

function walkDir(dir, callback) {
  fs.readdirSync(dir).forEach(f => {
    let dirPath = path.join(dir, f);
    let isDirectory = fs.statSync(dirPath).isDirectory();
    if (isDirectory) {
      walkDir(dirPath, callback);
    } else if (dirPath.endsWith('.json')) {
      callback(dirPath);
    }
  });
}

function auditSubject(subject) {
  let totalStrings = 0;
  let remainingDollars = 0;
  let unrenderedCommands = [];

  function checkText(str, filePath, loc) {
    if (typeof str !== 'string') return;
    totalStrings++;
    const rendered = mathHtml(str);

    if (rendered.includes('$')) {
      remainingDollars++;
    }

    // Match any backslash followed by alphanumeric characters (unrendered command)
    const matches = rendered.match(/\\[A-Za-z0-9]+/g);
    if (matches) {
      unrenderedCommands.push({ filePath, loc, str, rendered, matches });
    }
  }

  function scanObj(obj, filePath, loc = '') {
    if (typeof obj === 'string') {
      checkText(obj, filePath, loc);
    } else if (Array.isArray(obj)) {
      obj.forEach((it, idx) => scanObj(it, filePath, `${loc}[${idx}]`));
    } else if (obj && typeof obj === 'object') {
      Object.keys(obj).forEach(k => scanObj(obj[k], filePath, `${loc}.${k}`));
    }
  }

  walkDir(`data/${subject}`, (filePath) => {
    try {
      const content = fs.readFileSync(filePath, 'utf-8');
      const json = JSON.parse(content);
      scanObj(json, filePath);
    } catch (err) {
      console.error(`Error reading ${filePath}:`, err.message);
    }
  });

  console.log(`=== AUDIT ${subject.toUpperCase()} ===`);
  console.log(`Total strings scanned: ${totalStrings}`);
  console.log(`Remaining raw dollars: ${remainingDollars}`);
  console.log(`Unrendered commands:   ${unrenderedCommands.length}`);
  if (unrenderedCommands.length > 0) {
    unrenderedCommands.forEach(c => {
      console.log(`  [${c.filePath} - ${c.loc}] ${c.matches.join(', ')}`);
      console.log(`    Raw:  ${c.str.slice(0, 100)}`);
      console.log(`    HTML: ${c.rendered.slice(0, 100)}`);
    });
  }
  console.log();
}

auditSubject('toan10');
auditSubject('ly10');
auditSubject('hoa10');
