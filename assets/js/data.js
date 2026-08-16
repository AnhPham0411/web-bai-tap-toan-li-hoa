/**
 * Lớp truy cập dữ liệu: đọc toàn bộ nội dung từ các file JSON trong thư mục data/.
 * Hỗ trợ chuyển đổi linh hoạt giữa Toán 10, Vật lí 10, Hóa học 10.
 */

import { getActiveSubjectId, setActiveSubjectId } from './store.js';

const BASE = 'data';
const cache = new Map();

async function loadJson(path) {
  if (cache.has(path)) return cache.get(path);
  const promise = fetch(path, { cache: 'no-cache' }).then((res) => {
    if (!res.ok) throw new Error(`Không đọc được ${path} (HTTP ${res.status})`);
    return res.json();
  });
  cache.set(path, promise);
  return promise;
}

export function getManifest() {
  return loadJson(`${BASE}/manifest.json`);
}

export async function getActiveSubject() {
  const manifest = await getManifest();
  const savedId = getActiveSubjectId();
  const subject = manifest.subjects.find((s) => s.id === savedId && s.available) || manifest.subjects.find((s) => s.available);
  return subject;
}

export async function getSubjectIndex(subject) {
  return loadJson(`${BASE}/${subject.path}/index.json`);
}

export async function getChapterTheory(subject, chapter) {
  return loadJson(`${BASE}/${subject.path}/${chapter.theory}`);
}

export async function getQuestionSet(subject, set) {
  return loadJson(`${BASE}/${subject.path}/${set.file}`);
}

/** Nạp sẵn manifest + index + các bộ câu hỏi của môn học được chọn. */
export async function bootstrap(subjectId = null) {
  if (subjectId) {
    setActiveSubjectId(subjectId);
  }
  const manifest = await getManifest();
  const subject = await getActiveSubject();
  const index = await getSubjectIndex(subject);
  const sets = {};
  await Promise.all(
    index.questionSets.map(async (set) => {
      sets[set.id] = await getQuestionSet(subject, set);
    })
  );
  return { manifest, subject, index, sets };
}
