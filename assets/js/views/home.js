import { mathHtml } from '../math.js';
import { getResults } from '../store.js';

export function renderHome(ctx) {
  const { manifest, subject, index, sets } = ctx;

  const totalQuestions = Object.values(sets)
    .reduce((sum, set) => sum + set.questions.length, 0);
  const totalLessons = index.chapters
    .reduce((sum, ch) => sum + ch.lessons.length, 0);

  const setStats = index.questionSets
    .map((s) => `<div class="stat"><span class="n">${sets[s.id].questions.length}</span><span class="l">Câu ${s.title.toLowerCase()}</span></div>`)
    .join('');

  const chapterCards = index.chapters.map((ch) => {
    const counts = index.questionSets.map((s) => {
      const n = sets[s.id].questions.filter((q) => q.chapter === ch.id).length;
      return `${n} ${s.title.toLowerCase()}`;
    }).join(' · ');

    return `
      <article class="card chapter-card">
        <div class="roman">Chương ${ch.roman}</div>
        <h3>${mathHtml(ch.title)}</h3>
        <p>${mathHtml(ch.summary)}</p>
        <div class="links">
          <a class="btn btn-sm" href="#/ly-thuyet/${ch.id}">Lý thuyết (${ch.lessons.length} bài)</a>
          <a class="btn btn-sm" href="#/luyen-tap?chuong=${ch.id}">Luyện tập</a>
        </div>
        <p style="margin:12px 0 0;font-size:13px;color:var(--text-muted)">${counts}</p>
      </article>`;
  }).join('');

  const availableSubjects = manifest.subjects
    .filter((s) => s.available)
    .map((s) => `
      <div class="subject-item ${s.id === subject.id ? 'active' : ''}">
        <div class="meta">
          <strong>${s.name}</strong>
          <small>${s.note || ''}</small>
        </div>
        ${s.id === subject.id 
          ? '<span class="badge badge-accent">Đang chọn</span>' 
          : `<button class="btn btn-sm switch-subj-btn" data-subj="${s.id}">Chọn môn này</button>`}
      </div>`).join('');

  const futureSubjects = [
    { name: "Toán 10 — Học kì 2", note: "Sẽ bổ sung: Hàm số bậc hai, Phương pháp toạ độ, Đại số tổ hợp, Xác suất." },
    { name: "Toán 11", note: "Chưa có dữ liệu." },
    { name: "Toán 12", note: "Chưa có dữ liệu." }
  ].map((s) => `
    <div class="subject-item disabled">
      <div class="meta">
        <strong>${s.name}</strong>
        <small>${s.note}</small>
      </div>
      <span class="badge">Sắp có</span>
    </div>`).join('');

  const recent = getResults().slice(0, 3);
  const recentHtml = recent.length ? `
    <section style="margin-top:44px">
      <h2>Lượt luyện tập gần đây</h2>
      <div class="subject-list">
        ${recent.map((r) => `
          <div class="subject-item">
            <div class="meta">
              <strong>${r.setTitle}</strong>
              <small>${r.chapters} · ${new Date(r.at).toLocaleString('vi-VN')}</small>
            </div>
            <span class="badge ${r.ratio >= 0.5 ? 'badge-ok' : 'badge-bad'}">
              ${r.correct}/${r.total} — ${Math.round(r.ratio * 100)}%
            </span>
          </div>`).join('')}
      </div>
    </section>` : '';

  setTimeout(() => {
    document.querySelectorAll('.switch-subj-btn').forEach((btn) => {
      btn.addEventListener('click', (e) => {
        const targetId = e.currentTarget.dataset.subj;
        const selectEl = document.getElementById('subject-select');
        if (selectEl) {
          selectEl.value = targetId;
          selectEl.dispatchEvent(new Event('change'));
        }
      });
    });
  }, 0);

  return `
    <section class="hero">
      <div class="eyebrow">${subject.book} · ${subject.term}</div>
      <h1>Học và luyện tập ${subject.name}</h1>
      <p>Lý thuyết đầy đủ theo từng bài, kèm hai dạng bài tập: trắc nghiệm bốn phương án và
         trả lời ngắn điền đáp số. 750 câu hỏi luyện tập cho ${subject.name}.</p>
      <div class="btn-row">
        <a class="btn btn-primary" href="#/luyen-tap">Bắt đầu luyện tập</a>
        <a class="btn" href="#/ly-thuyet">Xem lý thuyết</a>
      </div>
    </section>

    <div class="stat-row">
      <div class="stat"><span class="n">${index.chapters.length}</span><span class="l">Chương</span></div>
      <div class="stat"><span class="n">${totalLessons}</span><span class="l">Bài lý thuyết</span></div>
      ${setStats}
      <div class="stat"><span class="n">${totalQuestions}</span><span class="l">Tổng số câu hỏi</span></div>
    </div>

    <section>
      <h2>Nội dung theo chương</h2>
      <div class="card-grid" style="margin-top:16px">${chapterCards}</div>
    </section>

    ${recentHtml}

    <section style="margin-top:44px">
      <h2>Các môn học hiện có (Lớp 10)</h2>
      <p style="color:var(--text-muted);margin-top:0">Chương trình GDPT 2018 — Kết nối tri thức với cuộc sống.</p>
      <div class="subject-list">${availableSubjects}</div>
    </section>

    <section style="margin-top:44px">
      <h2>Sẽ mở rộng thêm</h2>
      <p style="color:var(--text-muted);margin-top:0">Cấu trúc dữ liệu đã sẵn sàng cho các lớp và học kì khác.</p>
      <div class="subject-list">${futureSubjects}</div>
    </section>`;
}
