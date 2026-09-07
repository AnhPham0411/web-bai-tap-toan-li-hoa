/**
 * Kiểm thử các module thuần logic của giao diện: store.js, math.js, grade.js.
 * Không cần trình duyệt — chỉ giả lập localStorage.
 *
 * Chạy:  node tests/frontend.test.mjs
 */
const mem = new Map();
globalThis.localStorage = {
  getItem: (k) => (mem.has(k) ? mem.get(k) : null),
  setItem: (k, v) => mem.set(k, String(v)),
  removeItem: (k) => mem.delete(k),
  clear: () => mem.clear(),
};

let fail = 0;
const ok = (name, cond, extra = '') => {
  console.log(`${cond ? 'PASS' : 'FAIL'}  ${name}${extra ? '  ' + extra : ''}`);
  if (!cond) fail++;
};

// ---------------------------------------------------------------- store.js
const store = await import('../assets/js/store.js');

// 1. Nâng cấp từ khoá cũ 'toan10.v1'
mem.clear();
localStorage.setItem('toan10.v1', JSON.stringify({
  theme: 'dark', activeSubjectId: 'toan10',
  results: [{ setId: 'mc', ratio: 0.8, correct: 8, total: 10 }],
  theory: { chapterId: 'c3', lessonId: 'b6' },
  setup: { setId: 'mc', count: 20 },
}));
ok('migrate: giữ theme', store.getTheme() === 'dark');
ok('migrate: giữ kết quả cũ cho Toán', store.getResults('toan10').length === 1);
ok('migrate: Hoá không thấy kết quả của Toán', store.getResults('hoa10').length === 0);
ok('migrate: giữ vị trí lý thuyết', store.getTheoryPosition('toan10')?.lessonId === 'b6');

// 2. Tách dữ liệu theo môn — đây chính là lỗi cũ
mem.clear();
store.saveResult('toan10', { setId: 'mc', ratio: 0.9, correct: 9, total: 10 });
store.saveResult('hoa10', { setId: 'mc', ratio: 0.2, correct: 2, total: 10 });
ok('tách môn: Toán chỉ thấy kết quả của Toán',
  store.getResults('toan10').length === 1 && store.getResults('toan10')[0].ratio === 0.9);
ok('tách môn: Hoá chỉ thấy kết quả của Hoá',
  store.getResults('hoa10').length === 1 && store.getResults('hoa10')[0].ratio === 0.2);
ok('tách môn: getBest không trộn điểm giữa hai môn',
  store.getBest('hoa10', 'mc').ratio === 0.2 && store.getBest('toan10', 'mc').ratio === 0.9);

store.saveTheoryPosition('toan10', 'c5', 'b13');
store.saveTheoryPosition('ly10', 'c2', 'b4');
ok('tách môn: vị trí lý thuyết không lẫn',
  store.getTheoryPosition('toan10').lessonId === 'b13' &&
  store.getTheoryPosition('ly10').lessonId === 'b4');

store.saveLastSetup('toan10', { count: 25 });
ok('tách môn: thiết lập đề riêng từng môn',
  store.getLastSetup('toan10').count === 25 && store.getLastSetup('ly10') === null);

// 3. localStorage bị khoá thì không được ném lỗi
const realSet = localStorage.setItem;
localStorage.setItem = () => { throw new Error('QuotaExceeded'); };
let threw = false;
try { store.setTheme('light'); } catch { threw = true; }
localStorage.setItem = realSet;
ok('localStorage bị khoá: không ném lỗi ra ngoài', !threw);

// ---------------------------------------------------------------- math.js
const math = await import('../assets/js/math.js');
ok('math: phân số', math.mathHtml('\\frac{1}{2}').includes('m-frac'));
ok('math: căn thức', math.mathHtml('\\sqrt{2}').includes('m-sqrt'));
ok('math: vectơ', math.mathHtml('\\overrightarrow{AB}').includes('m-vec'));
ok('math: chỉ số dưới hoá học', math.mathHtml('H_2SO_4') === 'H<sub>2</sub>SO<sub>4</sub>',
  math.mathHtml('H_2SO_4'));
ok('math: số mũ', math.mathHtml('x^{2}') === 'x<sup>2</sup>');
ok('math: ký hiệu độ', math.mathHtml('60^\\circ') === '60<sup>°</sup>', math.mathHtml('60^\\circ'));
ok('math: chặn thẻ HTML', !math.mathHtml('<img src=x onerror=alert(1)>').includes('<img'));
ok('math: thoát dấu nháy đơn', math.mathHtml("a'b").includes('&#39;'));
ok('math: nhóm { thiếu dấu đóng không treo', typeof math.mathHtml('\\frac{1') === 'string');
ok('math: lệnh lạ vẫn trả chuỗi', typeof math.mathHtml('\\unknowncmd{x}') === 'string');

ok('math: chỉ số dưới rồi mũ (ion)', math.mathHtml('SO_4^{2-}') === 'SO<sub>4</sub><sup>2-</sup>', math.mathHtml('SO_4^{2-}'));
ok('math: chữ Hy Lạp sau dấu _', math.mathHtml('x_\\alpha') === 'x<sub>α</sub>', math.mathHtml('x_\\alpha'));
ok('math: enthalpy chuẩn', math.mathHtml('\\Delta_r H^0_{298}') === 'Δ<sub>r</sub> H<sup>0</sup><sub>298</sub>', math.mathHtml('\\Delta_r H^0_{298}'));
ok('math: nhiệt độ Celsius', math.mathHtml('30^\\circ C') === '30<sup>°</sup> C', math.mathHtml('30^\\circ C'));
ok('math: mũ 2 sau vectơ', math.mathHtml('\\vec{a}^2').includes('m-vec'), math.mathHtml('\\vec{a}^2'));
ok('math: m/s^2', math.mathHtml('m/s^2') === 'm/s<sup>2</sup>');

ok('math: bọc công thức $...$', math.mathHtml('$x + 1 = 0$') === '<span class="m-math">x + 1 = 0</span>', math.mathHtml('$x + 1 = 0$'));
ok('math: khối $$...$$', math.mathHtml('$$y = ax + b$$') === '<span class="m-display">y = ax + b</span>', math.mathHtml('$$y = ax + b$$'));
ok('math: thoát ký tự \\$', math.mathHtml('Giá \\$10') === 'Giá $10', math.mathHtml('Giá \\$10'));
ok('math: phân số không ngoặc \\frac12', math.mathHtml('\\frac12').includes('m-frac'), math.mathHtml('\\frac12'));
ok('math: căn không ngoặc \\sqrt3', math.mathHtml('\\sqrt3').includes('m-sqrt'), math.mathHtml('\\sqrt3'));
ok('math: vectơ không ngoặc \\vec a', math.mathHtml('\\vec a') === '<span class="m-vec">a</span>', math.mathHtml('\\vec a'));
ok('math: vectơ không \\vec0', math.mathHtml('\\vec0') === '<span class="m-vec">0</span>', math.mathHtml('\\vec0'));
ok('math: gạch trên \\bar a', math.mathHtml('\\bar a') === '<span class="m-obar">a</span>', math.mathHtml('\\bar a'));
ok('math: trung bình \\overline x', math.mathHtml('\\overline x') === '<span class="m-obar">x</span>', math.mathHtml('\\overline x'));
ok('math: tập số \\mathbb{R}', math.mathHtml('\\mathbb{R}') === 'ℝ', math.mathHtml('\\mathbb{R}'));
ok('math: tập số \\mathbb R', math.mathHtml('\\mathbb R') === 'ℝ', math.mathHtml('\\mathbb R'));
ok('math: chỉ số tiếng Việt', math.mathHtml('\\overline{x}_{mới}') === '<span class="m-obar">x</span><sub>mới</sub>', math.mathHtml('\\overline{x}_{mới}'));


// ---------------------------------------------------------------- grade.js
const grade = await import('../assets/js/grade.js');
ok('grade: chọn A (chỉ số 0) được tính là đã trả lời',
  grade.isCorrect({ answer: 0 }, 'multiple-choice', 0) === true);
ok('grade: chọn sai', grade.isCorrect({ answer: 2 }, 'multiple-choice', 0) === false);
ok('grade: chưa trả lời', grade.isCorrect({ answer: 0 }, 'multiple-choice', null) === false);
ok('grade: dấu phẩy thập phân', grade.isCorrect({ answer: '2.5' }, 'short-answer', '2,5') === true);
ok('grade: có tolerance thì nhận đáp số chưa làm tròn',
  grade.isCorrect({ answer: '0.67', tolerance: 0.01 }, 'short-answer', '0,6667') === true);
ok('grade: không tolerance thì bắt đúng tuyệt đối',
  grade.isCorrect({ answer: '0.67' }, 'short-answer', '0,6667') === false);
ok('grade: chấp nhận phân số', grade.isCorrect({ answer: '0.5' }, 'short-answer', '1/2') === true);
ok('grade: chia 0 không vỡ', grade.isCorrect({ answer: '1' }, 'short-answer', '1/0') === false);
ok('grade: chuỗi rác', grade.isCorrect({ answer: '1' }, 'short-answer', 'abc') === false);
ok('grade: đáp án hỏng không làm vỡ hiển thị',
  grade.formatAnswer({ answer: 9, choices: ['a', 'b', 'c', 'd'] }, 'multiple-choice')
    .includes('lỗi'));
ok('grade: hiển thị đáp số kiểu Việt kèm đơn vị',
  grade.formatAnswer({ answer: '-2.5', unit: 'm/s' }, 'short-answer') === '−2,5 m/s',
  grade.formatAnswer({ answer: '-2.5', unit: 'm/s' }, 'short-answer'));

console.log(`\n${fail === 0 ? 'TẤT CẢ ĐỀU PASS' : fail + ' TEST HỎNG'}`);
process.exit(fail === 0 ? 0 : 1);
