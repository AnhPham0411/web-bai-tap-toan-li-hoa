import { mathHtml, mathBlock, mathParagraphs } from '../math.js';
import { getChapterTheory } from '../data.js';
import { saveTheoryPosition, getTheoryPosition } from '../store.js';

const BOX_LABELS = {
  definition: 'Định nghĩa',
  theorem: 'Định lí',
  example: 'Ví dụ',
  note: 'Chú ý'
};

/** Bỏ tiêu đề khi nó chỉ lặp lại nhãn của khối (ví dụ nhãn "Định nghĩa" + tiêu đề "Định nghĩa"). */
function boxTitle(block) {
  const label = BOX_LABELS[block.type] || '';
  if (!block.title) return '';
  const same = block.title.trim().toLowerCase() === label.trim().toLowerCase();
  return same ? '' : `<div class="box-title">${mathHtml(block.title)}</div>`;
}

function renderBlock(block) {
  switch (block.type) {
    case 'heading':
      return `<h2 class="blk-heading">${mathHtml(block.text)}</h2>`;

    case 'text':
      return `<div class="blk blk-text">${mathParagraphs(block.content)}</div>`;

    case 'list':
      return `<div class="blk blk-list">
        ${block.title ? `<div class="list-title">${mathHtml(block.title)}</div>` : ''}
        <ul>${block.items.map((i) => `<li>${mathBlock(i)}</li>`).join('')}</ul>
      </div>`;

    case 'definition':
    case 'theorem':
    case 'note':
      return `<div class="box box-${block.type}">
        <div class="box-label">${BOX_LABELS[block.type]}</div>
        ${boxTitle(block)}
        ${mathParagraphs(block.content)}
      </div>`;

    case 'example':
      return `<div class="box box-example">
        <div class="box-label">${BOX_LABELS.example}</div>
        ${mathParagraphs(block.question)}
        <div style="margin-top:10px;padding-top:10px;border-top:1px solid var(--border)">
          <div class="box-label">Lời giải</div>
          ${mathParagraphs(block.solution)}
        </div>
      </div>`;

    case 'formula':
      return `<div class="blk formula-list">
        ${block.items.map((it) => `
          <div class="formula-row${it.label ? '' : ' no-label'}">
            ${it.label ? `<div class="f-label">${mathHtml(it.label)}</div>` : ''}
            <div class="f-math">${mathBlock(it.math)}</div>
          </div>`).join('')}
      </div>`;

    case 'table':
      return `<div class="blk">
        ${block.title ? `<div class="tbl-title">${mathHtml(block.title)}</div>` : ''}
        <div class="tbl-wrap"><table>
          <thead><tr>${block.headers.map((h) => `<th>${mathHtml(h)}</th>`).join('')}</tr></thead>
          <tbody>${block.rows.map((row) =>
            `<tr>${row.map((cell) => `<td>${mathHtml(cell)}</td>`).join('')}</tr>`).join('')}</tbody>
        </table></div>
      </div>`;

    default:
      return '';
  }
}

/** Danh sách phẳng mọi bài học để làm chức năng bài trước / bài sau. */
function flatLessons(index) {
  return index.chapters.flatMap((ch) =>
    ch.lessons.map((ls) => ({ chapterId: ch.id, lessonId: ls.id, title: ls.title }))
  );
}

function renderNav(index, chapterId, lessonId) {
  return index.chapters.map((ch) => `
    <div class="nav-group">
      <div class="nav-title">Chương ${ch.roman}. ${mathHtml(ch.title)}</div>
      ${ch.lessons.map((ls) => {
        const active = ch.id === chapterId && ls.id === lessonId;
        return `<a href="#/ly-thuyet/${ch.id}/${ls.id}" class="${active ? 'active' : ''}">${mathHtml(ls.title)}</a>`;
      }).join('')}
    </div>`).join('');
}

export async function renderTheory(ctx, params) {
  const { subject, index } = ctx;
  const saved = getTheoryPosition();

  let chapterId = params.chapterId || saved?.chapterId || index.chapters[0].id;
  let chapter = index.chapters.find((c) => c.id === chapterId) || index.chapters[0];
  chapterId = chapter.id;

  let lessonId = params.lessonId
    || (params.chapterId ? chapter.lessons[0].id : saved?.lessonId)
    || chapter.lessons[0].id;
  if (!chapter.lessons.some((l) => l.id === lessonId)) lessonId = chapter.lessons[0].id;

  const theory = await getChapterTheory(subject, chapter);
  const lesson = theory.lessons.find((l) => l.id === lessonId) || theory.lessons[0];

  saveTheoryPosition(chapterId, lesson.id);

  const all = flatLessons(index);
  const pos = all.findIndex((l) => l.chapterId === chapterId && l.lessonId === lesson.id);
  const prev = pos > 0 ? all[pos - 1] : null;
  const next = pos >= 0 && pos < all.length - 1 ? all[pos + 1] : null;

  return `
    <div class="theory-layout">
      <aside class="theory-nav">${renderNav(index, chapterId, lesson.id)}</aside>

      <article class="theory-body">
        <div class="eyebrow">Chương ${chapter.roman} · ${mathHtml(chapter.title)}</div>
        <h1>${mathHtml(lesson.title)}</h1>
        <p class="lesson-meta">${subject.name} — ${subject.term} · ${subject.book}</p>

        ${lesson.blocks.map(renderBlock).join('')}

        <div class="btn-row" style="margin-top:34px">
          <a class="btn btn-primary" href="#/luyen-tap?chuong=${chapterId}">Luyện tập chương ${chapter.roman}</a>
        </div>

        <nav class="lesson-pager">
          ${prev
            ? `<a class="btn btn-ghost" href="#/ly-thuyet/${prev.chapterId}/${prev.lessonId}">← ${mathHtml(prev.title)}</a>`
            : '<span></span>'}
          ${next
            ? `<a class="btn btn-ghost" href="#/ly-thuyet/${next.chapterId}/${next.lessonId}">${mathHtml(next.title)} →</a>`
            : '<span></span>'}
        </nav>
      </article>
    </div>`;
}
