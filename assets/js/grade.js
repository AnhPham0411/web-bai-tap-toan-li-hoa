/** Chấm bài: xử lý cả câu trắc nghiệm và câu trả lời ngắn (đáp số). */

/**
 * Chuẩn hoá chuỗi người học nhập thành số.
 * Chấp nhận: dấu phẩy hoặc dấu chấm thập phân, dấu trừ Unicode, khoảng trắng,
 * dấu phân cách nghìn, phân số dạng a/b và ký hiệu phần trăm.
 */
export function parseNumber(input) {
  if (input === null || input === undefined) return NaN;
  let s = String(input).trim();
  if (s === '') return NaN;

  s = s
    .replace(/[−–—]/g, '-')   // − – — → -
    .replace(/\s+/g, '')
    .replace(/%$/, '');

  // "1.234,56" → "1234.56"  |  "1,5" → "1.5"  |  "1.234.567" → "1234567"
  if (s.includes(',') && s.includes('.')) {
    s = s.lastIndexOf(',') > s.lastIndexOf('.')
      ? s.replace(/\./g, '').replace(/,/g, '.')
      : s.replace(/,/g, '');
  } else if ((s.match(/,/g) || []).length > 1) {
    s = s.replace(/,/g, '');            // "1,234,567" → dấu phân cách nghìn
  } else if ((s.match(/\./g) || []).length > 1) {
    s = s.replace(/\./g, '');           // "1.234.567" → dấu phân cách nghìn
  } else {
    s = s.replace(',', '.');
  }

  const fraction = /^(-?\d+(?:\.\d+)?)\/(-?\d+(?:\.\d+)?)$/.exec(s);
  if (fraction) {
    const den = Number(fraction[2]);
    return den === 0 ? NaN : Number(fraction[1]) / den;
  }

  return /^-?\d+(\.\d+)?$/.test(s) ? Number(s) : NaN;
}

/**
 * Sai số cho phép của một câu.
 * Câu nào khai báo "tolerance" thì dùng đúng giá trị đó (cho phép học sinh nộp
 * đáp số chưa làm tròn). Câu không khai báo thì chỉ nới đúng bằng sai số dấu phẩy động.
 */
function toleranceOf(question) {
  const t = Number(question.tolerance);
  return Number.isFinite(t) && t > 0 ? t : 1e-9;
}

/** Kiểm tra một câu trả lời ngắn. */
export function checkShortAnswer(question, input) {
  const value = parseNumber(input);
  if (Number.isNaN(value)) return false;

  const targets = [question.answer, ...(question.accept || [])];
  const tol = toleranceOf(question);

  return targets.some((t) => {
    const target = parseNumber(t);
    return !Number.isNaN(target) && Math.abs(value - target) <= tol + 1e-9;
  });
}

/** Kiểm tra một câu trắc nghiệm. */
export function checkMultipleChoice(question, index) {
  return Number.isInteger(index) && index === question.answer;
}

export function isCorrect(question, type, response) {
  if (response === null || response === undefined || response === '') return false;
  return type === 'multiple-choice'
    ? checkMultipleChoice(question, response)
    : checkShortAnswer(question, response);
}

/** Đổi dấu chấm thập phân sang dấu phẩy kiểu Việt Nam và dùng dấu trừ toán học. */
export function formatNumberVi(value) {
  return String(value).replace('.', ',').replace(/^-/, '−');
}

/** Định dạng đáp án đúng để hiển thị. */
export function formatAnswer(question, type) {
  if (type === 'multiple-choice') {
    const i = question.answer;
    const label = 'ABCD'[i];
    if (!Number.isInteger(i) || !label || !question.choices || question.choices[i] === undefined) {
      return 'Dữ liệu đáp án bị lỗi';
    }
    return `${label}. ${question.choices[i]}`;
  }
  const unit = question.unit ? ` ${question.unit}` : '';
  return `${formatNumberVi(question.answer)}${unit}`;
}

/** Trộn mảng (Fisher-Yates) — trả về mảng mới. */
export function shuffle(list) {
  const arr = [...list];
  for (let i = arr.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [arr[i], arr[j]] = [arr[j], arr[i]];
  }
  return arr;
}
