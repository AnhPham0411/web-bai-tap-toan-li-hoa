/**
 * Lưu tiến độ và tuỳ chọn của người học vào localStorage.
 *
 * Dữ liệu riêng của từng môn (kết quả luyện tập, vị trí đọc lý thuyết, thiết lập đề
 * gần nhất) được tách theo subjectId để đổi môn không lẫn dữ liệu của nhau.
 */

const KEY = 'tlh10.v2';
const LEGACY_KEY = 'toan10.v1';
const DEFAULT_SUBJECT = 'toan10';

function read() {
  try {
    const raw = localStorage.getItem(KEY);
    if (raw) return JSON.parse(raw) || {};
    // Nâng cấp từ bản cũ: dữ liệu cũ luôn là của môn Toán 10.
    const legacy = JSON.parse(localStorage.getItem(LEGACY_KEY) || 'null');
    if (!legacy) return {};
    return {
      theme: legacy.theme,
      activeSubjectId: legacy.activeSubjectId || DEFAULT_SUBJECT,
      bySubject: {
        [legacy.activeSubjectId || DEFAULT_SUBJECT]: {
          results: legacy.results || [],
          theory: legacy.theory || null,
          setup: legacy.setup || null
        }
      }
    };
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

/** Đọc nhánh dữ liệu của một môn. */
function readSubject(data, subjectId) {
  return (data.bySubject && data.bySubject[subjectId]) || {};
}

/** Ghi vào nhánh dữ liệu của một môn. */
function updateSubject(subjectId, patch) {
  const data = read();
  if (!data.bySubject) data.bySubject = {};
  data.bySubject[subjectId] = { ...readSubject(data, subjectId), ...patch };
  write(data);
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
  return read().activeSubjectId || DEFAULT_SUBJECT;
}

export function setActiveSubjectId(id) {
  const data = read();
  data.activeSubjectId = id;
  write(data);
}

/** Ghi lại kết quả một lượt luyện tập của một môn. */
export function saveResult(subjectId, entry) {
  const prev = readSubject(read(), subjectId).results || [];
  updateSubject(subjectId, { results: [entry, ...prev].slice(0, 50) });
}

export function getResults(subjectId) {
  return readSubject(read(), subjectId).results || [];
}

/** Điểm cao nhất (theo tỉ lệ %) của một bộ câu hỏi trong một môn. */
export function getBest(subjectId, setId) {
  const results = getResults(subjectId).filter((r) => r.setId === setId);
  if (!results.length) return null;
  return results.reduce((best, r) => (r.ratio > best.ratio ? r : best), results[0]);
}

/** Vị trí bài lý thuyết đang đọc của một môn, để lần sau mở lại. */
export function saveTheoryPosition(subjectId, chapterId, lessonId) {
  updateSubject(subjectId, { theory: { chapterId, lessonId } });
}

export function getTheoryPosition(subjectId) {
  return readSubject(read(), subjectId).theory || null;
}

export function getLastSetup(subjectId) {
  return readSubject(read(), subjectId).setup || null;
}

export function saveLastSetup(subjectId, setup) {
  updateSubject(subjectId, { setup });
}
