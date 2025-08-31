# Ultra‑Enhanced Prompt — Single‑File Web App (HTML + CSS + JS)

**New Global Rules (supersede prior variants)**

* **Single file only:** Deliver one `.html` file containing valid, semantic **HTML**, inline **CSS**, and inline **JavaScript**. Absolutely no external assets, fonts, libraries, or network fetches. Pure offline.
* **Web app (not CLI):** It must run entirely in the browser as a **real interactive web application**. Every visible control must function; no dead buttons or placeholder links.
* **Free topic:** The subject is your choice, but it must demonstrate disciplined creativity, real utility, and polished UX.
* **Zero tolerance for errors:** Opening DevTools must show **zero** console errors/warnings across supported browsers.
* **Deterministic by default:** If randomness is used, expose a visible **Seed** control; default seed must yield identical results across runs.

This brief preserves the original spirit — **extreme creativity within strict engineering discipline** — but targets a **single‑file, user‑facing web app**. The artifact must be **beautiful, convenient, and robust**, with **fully functional UI**, **predictable behavior**, and **no runtime surprises**.

---

## Objective

Create a *single‑file* HTML document (HTML5 + inline CSS & JS) that reads as a masterwork of front‑end engineering — **clear**, **cohesive**, **elegant**, and **intellectually impressive** — while operating as a **real web application**. Balance aesthetics and practicality: thoughtful visuals, meaningful interactions, and resilient code. Avoid gimmicks; embrace purposeful polish.

---

## Hard Constraints

1. **Single HTML file** only. All CSS/JS inline. No external images or fonts (embed SVGs inline or as data URIs if needed). No network calls.
2. **No errors:** DevTools must report **zero** console errors/warnings. Handle exceptions gracefully; never leave the app in a broken state.
3. **Determinism:** If randomness exists, include a visible **Seed** control. Identical seeds must produce identical outputs. Time‑based logic must be mockable.
4. **Accessibility‑first:** Keyboard operability; visible focus; contrast AA+; labels for all form controls; use ARIA only when native semantics are insufficient.
5. **Progressive enhancement:** Content is useful with HTML alone. CSS and JS enhance but never block core content.
6. **Performance budget:** First interaction ≤100ms on a typical laptop; no layout thrash. Respect `prefers‑reduced‑motion`.
7. **Line discipline:** Aim \~200–500 significant lines (excluding comments/test panel). Every line earns its place.
8. **Security & privacy:** No tracking; no unexpected clipboard writes; only explicit user‑initiated copy/download. Safeguard against HTML injection.
9. **Portability:** Must work without build steps. Open file → app runs.

---

## Problem Shape (pick one, or propose an equivalent scope)

* **Elegant utility:** task planner with constraint checks; schedule/packing visualizer; markdown‑to‑structured‑cards tool; compact CSV/JSON normalizer.
* **Generative/structured demo:** grammar/tiling/constraint playground with validators and a human‑readable “witness.”
* **Learning aid:** algorithm explainer (topological sort, pathfinding, parsing) with step‑through playback and clear invariants.
* **Data hygiene tool:** deterministic deduper/normalizer with previews, diffs, copy/export, and rollback.

The app must be **non‑trivial yet compact**, fully comprehensible after a focused read‑through.

---

## Design Requirements

* **Semantic scaffolding:** Use `header`, `nav`, `main`, `section`, `article`, `aside`, `footer`. Associate labels with inputs; meaningful `aria-*` only when needed.
* **Layout & theming:** Modern CSS only (Grid/Flex, logical properties). Define **design tokens** via CSS Custom Properties; provide **dark mode** and **high‑contrast** toggles. Keep typography rhythm and spacing deliberate.
* **Architecture:** Organize CSS with `@layer` (e.g., `reset`, `base`, `components`, `utilities`). Organize JS with `type="module"` scope or a single IIFE namespace to avoid globals.
* **State management:** Keep it simple and explicit. Prefer pure functions; reflect app state in the DOM; avoid hidden globals.
* **Interactions:** Every control must have handlers with graceful error messaging and helpful microcopy. Include tooltips/help where appropriate.
* **Deterministic UX:** Seeded randomness (if any). A tiny **Clock** abstraction toggles between fixed time and real time.
* **Documentation density:** An intro section, an in‑page **Help** panel, and concise inline comments explaining non‑obvious choices.
* **Internationalization‑ready:** Avoid locale‑specific formatting where possible; use `Intl` if needed; include a minimal language switch (e.g., `en` / `ko`).

---

## Interaction & Keyboard Shortcuts (recommended)

* **Shortcuts:** `R`=Run, `H`=Help, `T`=Self‑Test, `C`=Copy, `?`=Toggle shortcuts panel. Ignore shortcuts while typing in inputs.
* **Focus flow:** Tab order follows visual order; Escape closes dialogs; focus returns to the invoking control.
* **Feedback:** Use non‑blocking toasts and inline hints; never rely solely on color to convey meaning.

---

## Testing & Verification (in‑page)

* Include a collapsible **Self‑Test** panel that runs ≥ 3 checks:

  * **Nominal** (typical user flow succeeds).
  * **Edge** (limits/empty states handled).
  * **Error** (invalid input yields friendly messages; app remains stable).
* Display pass/fail counts and a succinct report **in‑page** (no external test libs).
* Provide a **Reset** action restoring the initial state without page reloads.
* Include an **Accessibility checklist** (rendered or comment) confirming headings outline, labels, focus, contrast, reduced motion, and no keyboard traps.

---

## Performance & Complexity

* Annotate non‑trivial algorithms with **Big‑O** comments and typical vs worst‑case notes.
* Avoid forced synchronous reflows; batch DOM updates; prefer CSS transitions over JS‑driven animations.
* Keep memory modest; prefer streaming/iterative transforms for lists.
* Expose a small **Metrics** readout (e.g., runs, last latency, nodes rendered) when `Debug` is enabled.

---

## Output & UX

* **Beauty & convenience:** Harmonious typography, steady spacing rhythm, and a coherent color system. Controls should be obvious and forgiving.
* **Status & feedback:** Toasts for success/error; inline validation messages; no silent failures.
* **Export:** If structured output exists, provide **Copy to Clipboard** and **Export to `<pre>`/download**. Respect user intent.
* **Print:** Include `@media print` for a clean, legible summary.

---

## Required Postscript (in the same file as an HTML comment)

Provide a concise **Explanation** (≤ 200 words) covering:

* Why the problem is elegant and non‑trivial.
* How design balances creativity with rigor.
* Which HTML/CSS/JS features improved clarity, accessibility, or performance.
* Why the page feels “masterful.”

---

## Scoring Rubric (User‑Centric)

* **Aesthetics (25%)** — Visual harmony, typography, color, spacing, responsive balance.
* **Usability & Convenience (25%)** — Intuitive flows, forgiving inputs, clear affordances, discoverability.
* **Accessibility (20%)** — Keyboard first, labels, focus, contrast, reduced motion, no traps.
* **Reliability & Correctness (15%)** — Zero console errors, robust edge/error handling, deterministic seed behavior.
* **Performance & Polish (15%)** — Snappy interactions, stable layout (no CLS), thoughtful micro‑interactions, clean print output.

> **Fail gates:** Any console error/warning, broken controls, inaccessible critical UI, or non‑deterministic seeded behavior → **automatic disqualification**.

---

## Guardrails (avoid)

* Div‑soup; ARIA where native semantics suffice; color‑only states; hidden focus rings.
* Blocking scripts or long main‑thread tasks; JS layout thrash; timing‑dependent logic without mocks.
* Overly clever one‑liners; magic numbers; CSS specificity wars or `!important` abuse.
* External assets, frameworks, or fonts; network fetches; non‑portable features.

---

## Submission Format

Provide **one** `.html` file containing:

1. The complete, runnable **single‑file web app** (`<html>` + inline `<style>` + inline `<script type="module">`).
2. A built‑in **Help** panel and **Self‑Test** panel.
3. A short **Explanation** block at the end in an HTML comment.

---

## Starter Skeleton (optional for the AI to emit)

```html
<!doctype html>
<html lang="en" data-theme="auto" data-contrast="normal">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title><Concise App Name></title>
  <meta name="description" content="Single-file web app masterpiece." />
  <style>
    /* @layer reset, base, components, utilities */
    @layer reset, base, components, utilities;
    @layer reset {
      *,*::before,*::after{box-sizing:border-box} html,body{margin:0}
      body{font:system-ui, -apple-system, Segoe UI, Roboto, Ubuntu, Cantarell, Noto Sans, Arial, sans-serif; line-height:1.5}
    }
    @layer base {
      :root{
        --bg:#0b0b0b; --fg:#e7e7e7; --muted:#9aa0a6; --accent:#7dd3fc; --danger:#ef4444; --ok:#10b981;
        --space-1:.25rem; --space-2:.5rem; --space-3:1rem; --space-4:1.5rem; --radius:.75rem; --shadow:0 6px 24px rgba(0,0,0,.25);
        --ring: 2px solid var(--accent);
      }
      @media (prefers-color-scheme: light) { :root{ --bg:#ffffff; --fg:#111827; --muted:#6b7280; --accent:#2563eb } }
      [data-contrast="high"]{ --accent:#22d3ee; --fg:#ffffff; --bg:#000000; }
      body{background:var(--bg); color:var(--fg); padding:var(--space-3)}
      main{max-width:1040px;margin-inline:auto;display:grid;gap:var(--space-3)}
      a{color:var(--accent)}
    }
    @layer components {
      .card{background:color-mix(in oklab, var(--bg), #fff 6%); border:1px solid color-mix(in oklab, var(--bg), #fff 12%); border-radius:var(--radius); box-shadow:var(--shadow); padding:var(--space-3)}
      .grid{display:grid;gap:var(--space-3)}
      @container (min-width: 720px){ .grid{grid-template-columns:1fr 1fr} }
      .toolbar{display:flex;gap:.5rem;align-items:center;flex-wrap:wrap}
      .btn{border:1px solid color-mix(in oklab, var(--bg), #fff 20%); background:color-mix(in oklab, var(--bg), #fff 10%); color:var(--fg); padding:.6rem .9rem; border-radius:.6rem; cursor:pointer}
      .btn:focus-visible{outline:var(--ring); outline-offset:2px}
      .kbd{font-family:ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; background:color-mix(in oklab, var(--bg), #fff 12%); padding:.1rem .4rem; border-radius:.35rem}
      .switch{display:inline-flex;align-items:center;gap:.4rem}
      .meter{font-variant-numeric:tabular-nums}
    }
    @layer utilities{
      .sr-only{position:absolute;width:1px;height:1px;padding:0;margin:-1px;overflow:hidden;clip:rect(0,0,0,0);white-space:nowrap;border:0}
      .muted{color:var(--muted)}
      .right{margin-left:auto}
      .cluster{display:flex;gap:.5rem;align-items:center;flex-wrap:wrap}
    }
    @media (prefers-reduced-motion: reduce){ *{animation-duration:0.001ms !important; animation-iteration-count:1 !important; transition-duration:0.001ms !important} }
    @media print{ .toolbar, #selftest, #help { display:none !important } }
  </style>
</head>
<body>
  <header class="card">
    <h1><span aria-hidden>✨</span> <span id="title">Concise App Name</span></h1>
    <p class="muted" id="subtitle">Single-file, no dependencies. Deterministic by default.</p>
  </header>
  <main>
    <section class="card">
      <h2>Controls</h2>
      <div class="toolbar" role="toolbar" aria-label="App controls">
        <label>Seed <input id="seed" type="number" value="42" aria-describedby="seed-help"/></label>
        <span id="seed-help" class="sr-only">Change to alter deterministic output</span>
        <button id="run" class="btn">Run (R)</button>
        <button id="reset" class="btn">Reset</button>
        <div class="switch"><input id="clock" type="checkbox"/> <label for="clock">Realtime Clock</label></div>
        <div class="switch"><input id="contrast" type="checkbox"/> <label for="contrast">High Contrast</label></div>
        <div class="switch"><input id="debug" type="checkbox"/> <label for="debug">Debug</label></div>
        <label class="right">Lang
          <select id="lang" aria-label="Language">
            <option value="en">English</option>
            <option value="ko">한국어</option>
          </select>
        </label>
        <button id="helpToggle" class="btn" aria-expanded="false" aria-controls="help">Help (H)</button>
      </div>
    </section>

    <section id="output" class="card" aria-live="polite" aria-busy="false">
      <h2>Output</h2>
      <pre id="results" class="muted">Press Run to begin.</pre>
      <div class="cluster">
        <button id="copy" class="btn">Copy (C)</button>
        <button id="download" class="btn">Download JSON</button>
        <span class="meter" id="metrics" aria-live="polite">runs=0 • last=–ms</span>
      </div>
    </section>

    <aside id="help" class="card" hidden>
      <h2>Help</h2>
      <p>Use <span class="kbd">Tab</span> to navigate. Change the seed for deterministic variations. Everything works offline. No errors permitted.</p>
      <ul>
        <li>Shortcuts: <span class="kbd">R</span> run, <span class="kbd">H</span> help, <span class="kbd">T</span> tests, <span class="kbd">C</span> copy.</li>
        <li>Toggle <em>Realtime Clock</em> to use the system time instead of a fixed timestamp.</li>
      </ul>
    </aside>

    <aside id="selftest" class="card" hidden>
      <h2>Self‑Test</h2>
      <div id="testResults" role="status" aria-live="polite">Not run.</div>
      <div class="toolbar"><button id="runTests" class="btn">Run Tests (T)</button></div>
    </aside>
  </main>

  <script type="module">
    // ————— Utilities & Determinism —————
    const qs=(s,el=document)=>el.querySelector(s);
    const seedEl=qs('#seed');
    const outEl=qs('#results');
    const output=qs('#output');
    const metricsEl=qs('#metrics');

    function mulberry32(a){ // tiny deterministic PRNG
      return function(){let t=a+=0x6D2B79F5; t=Math.imul(t ^ t>>>15, t | 1); t^=t+Math.imul(t ^ t>>>7, t | 61); return ((t ^ t>>>14)>>>0)/4294967296 }
    }

    const Clock=(()=>{ // togglable fixed vs realtime clock
      let fixed=Date.UTC(2024,0,1); // Jan 1, 2024 UTC
      return {
        now(realtime){ return realtime ? Date.now() : fixed; },
        set(ts){ fixed=Number(ts)||fixed; }
      };
    })();

    // ————— i18n (lightweight) —————
    const STR={
      en:{ title:'Concise App Name', subtitle:'Single-file, no dependencies. Deterministic by default.', run:'Run (R)', reset:'Reset', help:'Help (H)', copy:'Copy (C)', download:'Download JSON', outputPlaceholder:'Press Run to begin.' },
      ko:{ title:'간결한 앱 이름', subtitle:'단일 파일, 외부 의존성 없음. 기본 결정적 동작.', run:'실행 (R)', reset:'초기화', help:'도움말 (H)', copy:'복사 (C)', download:'JSON 다운로드', outputPlaceholder:'실행을 눌러 시작하세요.' }
    };
    const langEl=qs('#lang');
    function applyLang(){
      const L=STR[langEl.value]||STR.en;
      qs('#title').textContent=L.title; qs('#subtitle').textContent=L.subtitle;
      qs('#run').textContent=L.run; qs('#reset').textContent=L.reset; qs('#helpToggle').textContent=L.help;
      qs('#copy').textContent=L.copy; qs('#download').textContent=L.download;
      if(outEl.textContent.trim()===''||outEl.textContent.includes('Press Run')||outEl.textContent.includes('실행을 눌러')) outEl.textContent=L.outputPlaceholder;
    }

    // ————— Core demo logic (deterministic sample) —————
    function generate(seed, realtime){
      const rng=mulberry32(Number(seed)||42);
      const items=Array.from({length:8},(_,i)=>({ id:i+1, value:Math.round(rng()*100)}));
      const ts=new Date(Clock.now(realtime)).toISOString();
      const summary={ min:Math.min(...items.map(x=>x.value)), max:Math.max(...items.map(x=>x.value)), avg:(items.reduce((a,b)=>a+b.value,0)/items.length).toFixed(2)};
      return {ts, items, summary};
    }

    function render(data){
      const lines=[
        `timestamp: ${data.ts}`,
        'Generated values (deterministic):',
        ...data.items.map(x=>`  #${x.id}: ${x.value}`),
        '',
        `min=${data.summary.min}, max=${data.summary.max}, avg=${data.summary.avg}`
      ];
      outEl.textContent=lines.join('\n');
    }

    // ————— UI glue —————
    const state={ runs:0 };
    const contrastEl=qs('#contrast');
    const debugEl=qs('#debug');
    const clockEl=qs('#clock');

    function setBusy(el,flag){ el.setAttribute('aria-busy', String(!!flag)); }
    function toast(msg,isErr=false){
      const t=document.createElement('div');
      Object.assign(t.style,{position:'fixed',insetInline:'auto 1rem',insetBlockStart:'1rem',padding:'.5rem .75rem',borderRadius:'.5rem',background:isErr?'#ef4444':'#10b981',color:'#fff',boxShadow:'0 6px 20px rgba(0,0,0,.25)',zIndex:9999});
      t.textContent=msg; document.body.appendChild(t); setTimeout(()=>t.remove(), 1300);
    }

    function run(){
      const t0=performance.now(); setBusy(output,true);
      const data=generate(seedEl.value, clockEl.checked); render(data);
      setBusy(output,false);
      state.runs++; const dt=Math.round(performance.now()-t0);
      metricsEl.textContent=`runs=${state.runs} • last=${dt}ms`;
      if(debugEl.checked) console.debug('run()', {seed:seedEl.value, realtime:clockEl.checked, dt});
    }

    function reset(){ seedEl.value=42; outEl.textContent=(STR[langEl.value]||STR.en).outputPlaceholder; state.runs=0; metricsEl.textContent='runs=0 • last=–ms'; }

    function copy(){
      navigator.clipboard.writeText(outEl.textContent||'').then(()=> toast('Copied')).catch(()=> toast('Copy failed', true));
    }

    function download(){
      const blob=new Blob([JSON.stringify({text:outEl.textContent},null,2)],{type:'application/json'});
      const a=document.createElement('a'); a.href=URL.createObjectURL(blob); a.download='output.json'; a.click(); setTimeout(()=>URL.revokeObjectURL(a.href),500);
    }

    function toggleHelp(){
      const el=qs('#help'); const btn=qs('#helpToggle');
      const hidden=el.hasAttribute('hidden'); if(hidden){ el.removeAttribute('hidden'); btn.setAttribute('aria-expanded','true'); }
      else { el.setAttribute('hidden',''); btn.setAttribute('aria-expanded','false'); }
    }

    function applyContrast(){ document.documentElement.dataset.contrast=contrastEl.checked?'high':'normal'; }

    // ————— Self tests —————
    function selfTests(){
      const log=[]; let pass=0, fail=0; const assert=(c,m)=>{ (c?pass:fail) && log.push((c?'✔ ':'✘ ')+m) };
      // nominal
      const a=generate(42,false); assert(a.items.length===8,'Nominal: generates 8 values');
      // edge: seed coercion
      const b=generate('',false); assert(Number.isFinite(b.summary.min),'Edge: empty seed coerces');
      // error path: copy safe when empty
      const tmp=outEl.textContent; outEl.textContent='';
      try{ copy(); assert(true,'Copy: no throw on empty'); } catch{ assert(false,'Copy: threw on empty'); }
      outEl.textContent=tmp;
      // determinism
      const c1=generate(7,false), c2=generate(7,false); assert(JSON.stringify(c1.items)===JSON.stringify(c2.items),'Determinism: same seed same values');
      // metrics update
      const prev=state.runs; run(); assert(state.runs===prev+1,'Metrics: runs counter increments');
      qs('#testResults').textContent=`pass=${pass}, fail=${fail}\n`+log.join('\n');
    }

    // ————— Keyboard shortcuts —————
    document.addEventListener('keydown', (e)=>{
      const tag=e.target && (e.target.tagName||'').toLowerCase();
      const typing=tag==='input' || tag==='textarea' || e.isComposing; if(typing) return;
      if(e.key==='r' || e.key==='R'){ e.preventDefault(); run(); }
      else if(e.key==='h' || e.key==='H'){ e.preventDefault(); toggleHelp(); }
      else if(e.key==='t' || e.key==='T'){ e.preventDefault(); selfTests(); }
      else if(e.key==='c' || e.key==='C'){ e.preventDefault(); copy(); }
    });

    // ————— Wire up events —————
    qs('#run').addEventListener('click', run);
    qs('#reset').addEventListener('click', reset);
    qs('#copy').addEventListener('click', copy);
    qs('#download').addEventListener('click', download);
    qs('#helpToggle').addEventListener('click', toggleHelp);
    qs('#runTests').addEventListener('click', selfTests);
    contrastEl.addEventListener('change', applyContrast);
    langEl.addEventListener('change', applyLang);

    // Initialize
    applyLang(); applyContrast(); run();
  </script>

  <!--
  Explanation (≤200 words):
  This single-file app demonstrates disciplined, deterministic generation with a seeded PRNG, a togglable fixed/real-time clock, semantic structure, layered tokens, and accessible controls. CSS uses @layer and modern features (Grid/Flex, color-mix/oklab) with high-contrast and print modes. JS confines state to module scope, provides keyboard shortcuts, a metrics readout, export/copy actions, and an in-page self-test covering nominal/edge/error/determinism. No console errors, no external assets; every button works (Run/Reset/Help/Copy/Download/Tests). The layout is responsive and motion-respectful. The design balances beauty (rhythm, spacing, accent) with rigor (determinism, a11y, explicit state). The artifact remains compact yet expressive — a portable demonstration of disciplined creativity.
  -->
</body>
</html>
```
