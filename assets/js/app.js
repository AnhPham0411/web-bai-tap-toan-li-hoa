import { bootstrap } from './data.js';
import { getTheme, setTheme, getActiveSubjectId } from './store.js';
import { renderHome } from './views/home.js';
import { renderTheory } from './views/theory.js';
import * as practice from './views/practice.js';

const app = document.getElementById('app');
let ctx = null;

/* ---------- Chế độ sáng / tối ---------- */

function applyTheme(theme) {
  document.documentElement.dataset.theme = theme;
  const icon = document.querySelector('[data-theme-icon]');
  if (icon) icon.textContent = theme === 'dark' ? '☀' : '◐';
}

function initTheme() {
  applyTheme(getTheme());
  document.getElementById('theme-toggle').addEventListener('click', () => {
    const next = document.documentElement.dataset.theme === 'dark' ? 'light' : 'dark';
    setTheme(next);
    applyTheme(next);
  });
}

/* ---------- Chọn môn học ---------- */

function initSubjectSelect() {
  const selectEl = document.getElementById('subject-select');
  if (!selectEl) return;
  selectEl.value = getActiveSubjectId();
  selectEl.addEventListener('change', async (e) => {
    const newSubId = e.target.value;
    app.innerHTML = '<div class="loading">Đang nạp môn học mới…</div>';
    ctx = await bootstrap(newSubId);
    location.hash = '#/';
    await route();
  });
}

/* ---------- Router ---------- */

function parseHash() {
  const raw = location.hash.replace(/^#/, '') || '/';
  const [pathPart, queryPart] = raw.split('?');
  const segments = pathPart.split('/').filter(Boolean);
  return { segments, query: new URLSearchParams(queryPart || '') };
}

function setActiveNav(name) {
  document.querySelectorAll('#site-nav a').forEach((a) => {
    a.classList.toggle('active', a.dataset.nav === name);
  });
}

function showError(err) {
  app.innerHTML = `
    <div class="card" style="border-left:3px solid var(--bad)">
      <h2>Không tải được nội dung</h2>
      <p>${err.message}</p>
      <p style="color:var(--text-muted);font-size:14.5px">
        Trang này đọc dữ liệu bằng <code>fetch</code> nên cần chạy qua một web server cục bộ. Xem hướng dẫn trong <code>README.md</code>.
      </p>
    </div>`;
  console.error(err);
}

async function route() {
  const { segments, query } = parseHash();
  const [first, ...rest] = segments;

  try {
    if (!first) {
      setActiveNav('home');
      app.innerHTML = renderHome(ctx);
      return;
    }

    if (first === 'ly-thuyet') {
      setActiveNav('theory');
      app.innerHTML = '<div class="loading">Đang tải bài học…</div>';
      app.innerHTML = await renderTheory(ctx, { chapterId: rest[0], lessonId: rest[1] });
      return;
    }

    if (first === 'luyen-tap') {
      setActiveNav('practice');
      const sub = rest[0];

      if (sub === 'lam-bai') {
        if (!practice.hasSession()) { location.hash = '#/luyen-tap'; return; }
        app.innerHTML = practice.renderQuiz();
        practice.bindQuiz(ctx, app);
        return;
      }

      if (sub === 'ket-qua') {
        if (!practice.hasSession()) { location.hash = '#/luyen-tap'; return; }
        app.innerHTML = practice.renderResult();
        practice.bindResult(ctx, app);
        return;
      }

      practice.clearSession();
      app.innerHTML = practice.renderSetup(ctx, query);
      practice.bindSetup(ctx, app);
      return;
    }

    app.innerHTML = `
      <div class="empty">
        <h2>Không tìm thấy trang</h2>
        <p><a href="#/">Về trang chủ</a></p>
      </div>`;
  } catch (err) {
    showError(err);
  }
}

/* ---------- Khởi động ---------- */

(async function start() {
  initTheme();
  try {
    ctx = await bootstrap();
    initSubjectSelect();
  } catch (err) {
    showError(err);
    return;
  }
  window.addEventListener('hashchange', route);
  await route();
})();
