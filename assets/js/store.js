/** Lưu tiến độ và tuỳ chọn của người học vào localStorage. */

const KEY = 'toan10.v1';

function read() {
  try {
    return JSON.parse(localStorage.getItem(KEY)) || {};
  } catch {
    return {};
  }
}

function write(data) {
  try {
    localStorage.setItem(KEY, JSON.stringify(data));
  } catch {
    /* localStorage bị khoá — bỏ qua, ứng dụng vẫn chạy bình thường */
  }
}

export function getTheme() {
  return read().theme || 'light';
}

export function setTheme(theme) {
  const data = read();
  data.theme = theme;
  write(data);
}

export function getActiveSubjectId() {
  return read().activeSubjectId || 'toan10';
}

export function setActiveSubjectId(id) {
  const data = read();
  data.activeSubjectId = id;
  write(data);
}

/** Ghi lại kết quả một lượt luyện tập. */
export function saveResult(entry) {
  const data = read();
  data.results = [entry, ...(data.results || [])].slice(0, 50);
  write(data);
}

export function getResults() {
  return read().results || [];
}

/** Điểm cao nhất (theo tỉ lệ %) của một bộ câu hỏi. */
export function getBest(setId) {
  const results = getResults().filter((r) => r.setId === setId);
  if (!results.length) return null;
  return results.reduce((best, r) => (r.ratio > best.ratio ? r : best), results[0]);
}

/** Vị trí bài lý thuyết đang đọc, để lần sau mở lại. */
export function saveTheoryPosition(chapterId, lessonId) {
  const data = read();
  data.theory = { chapterId, lessonId };
  write(data);
}

export function getTheoryPosition() {
  return read().theory || null;
}

export function getLastSetup() {
  return read().setup || null;
}

export function saveLastSetup(setup) {
  const data = read();
  data.setup = setup;
  write(data);
}
