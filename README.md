# 🤖 AI Benchmark Project (EN) / AI 벤치마킹 프로젝트 (KO)

> Version 1.0 — 2025‑09‑01
>
> This is a bilingual, fully aligned README. English comes first, followed by a Korean mirror with identical structure and terminology.

---

## 1) Project Overview | 프로젝트 개요

A comprehensive benchmark comparing different AI models’ capabilities to produce **masterpiece‑level, single‑file applications** that balance creativity with engineering discipline.

* **Python**: Constraint satisfaction & algorithmic elegance
* **Web**: Interactive, accessible single‑page applications
* **Real‑world testing**: Implementation under errors and subsequent fixes

> **Scope note**: The ratings herein reflect results from the specific prompts and artifacts in this repository; they are not universal model rankings.

---

## 2) Canonical Repository Layout | 표준 저장소 구조

```
AI_Benchmark/
├─ ChatGPT/
│  ├─ Python/
│  │  ├─ main.py                  # Poetica Grammar Expander
│  │  └─ README.md                # Python implementation notes
│  └─ Web/
│     ├─ Web.html                 # NeatRows CSV/JSON Deduper & Normalizer
│     └─ README.md                # Web implementation notes
│
├─ Claude-Opus-4.1/
│  ├─ Python/
│  │  ├─ main.py                  # L‑System Fractal Composer (primary)
│  │  ├─ wfc.py                   # Wave Function Collapse (supplement)
│     └─ README.md                # Python implementation notes
│  └─ Web/
│     ├─ Web.html                 # Sudoku Constraint Solver
│     └─ README.md                # Web implementation notes
│
├─ Gemini-2.5-Pro/
│  ├─ Python/
│  │  ├─ main.py                  # L‑System Fractal Composer
│  │  └─ README.md                # Python implementation notes
│  └─ Web/
│     ├─ Web.html                 # SVG Tiling Composer
│     └─ README.md                # Web implementation notes
│
├─ Prompts/
│  ├─ Prompt_Python.md            # Python ultra‑enhanced prompt
│  └─ Prompt_Web.md               # Web ultra‑enhanced prompt
│
└─ README.md                      # This file
```

**Naming rules**

* Folders use `Pascal-Case` with hyphens for model/version (e.g., `Claude-Opus-4.1`, `Gemini-2.5-Pro`).
* Documents use `README.md` (lowercase extension), not `README.MD`.
* Primary web entry is always `Web.html`.

---

## 3) Benchmark Results | 벤치마킹 결과

### Model Performance Comparison | 모델 성능 비교

| Model               | Python Implementation | Web Implementation | Error Resolution | Overall    |
| ------------------- | --------------------- | ------------------ | ---------------- | ---------- |
| **Claude Opus 4.1** | ⭐⭐⭐⭐⭐                 | ⭐⭐⭐⭐⭐              | ⭐⭐⭐⭐⭐            | **95/100** |
| **ChatGPT**         | ⭐⭐⭐⭐                  | ⭐⭐⭐⭐               | ⭐⭐⭐⭐             | **80/100** |
| **Gemini 2.5 Pro**  | ⭐⭐⭐⭐                  | ⭐⭐⭐⭐               | ⭐⭐⭐⭐             | **75/100** |

#### Highlights | 하이라이트

* **Claude Opus 4.1** (Winner): L‑System Fractal Composer (Python), Sudoku Constraint Solver (Web)
* **ChatGPT**: Poetica Grammar Expander (Python), NeatRows Deduper/Normalizer (Web)
* **Gemini 2.5 Pro**: L‑System Fractal Composer (Python), SVG Tiling Composer (Web)

---

## 4) Detailed Analysis | 상세 분석

### 4.1 Claude Opus 4.1

**Python** — L‑System Fractal Composer

* Mathematical visualization via Lindenmayer systems
* Deterministic output; presets (e.g., Koch, Dragon, Sierpiński)

**Web** — Sudoku Constraint Solver

* **AC‑3** arc consistency, backtracking with **MRV** & heuristics
* Real‑time visualization, reproducible puzzle generation (seeded PRNG)
* A11y: full keyboard, ARIA, reduced‑motion

**Strengths**: architecture, algorithmic depth, UI polish, docs, robust error handling

---

### 4.2 ChatGPT

**Python** — Poetica Grammar Expander

* Weighted grammar DSL, deterministic text generation
* Strong typing and error handling; doctest‑based self‑tests

**Web** — NeatRows CSV/JSON Deduper & Normalizer

* Parsing (CSV/JSON), normalization, hash‑based de‑dup
* Export: CSV/JSON, clipboard; seeded sampling

**Strengths**: functional style, maintainability, practical utility
**Weaknesses**: initial grammar parsing bugs; less complex than Claude

---

### 4.3 Gemini 2.5 Pro

**Python** — L‑System Fractal Composer

* Turtle‑style path tracing, ASCII grid rendering, presets

**Web** — SVG Tiling Composer

* Deterministic procedural SVG patterns (Truchet, slashes, dots)
* Modern CSS (@layer, tokens), responsive, minimal DOM churn

**Strengths**: efficiency, test coverage, creative visuals
**Weaknesses**: UI/UX depth behind Claude; narrower scope

---

## 5) Testing Methodology | 테스트 방법론

### 5.1 Evaluation Criteria (Weights) | 평가 기준 (가중치)

1. **Code Quality (30%)** — architecture, readability, maintainability, typing, error handling
2. **Algorithmic Sophistication (25%)** — complexity, elegance, performance, correctness
3. **User Experience (20%)** — design, accessibility, responsiveness, docs/help
4. **Error Resolution (15%)** — bug finding/fixing, edge cases, robustness
5. **Creativity & Innovation (10%)** — originality, educational value, technical novelty

### 5.2 Process | 절차

1. Initial implementation from shared prompts
2. Real‑world testing & bug discovery
3. Model‑guided fixes
4. Final evaluation

---

## 6) Getting Started | 시작하기 (Step‑by‑Step)

### 6.1 Prerequisites | 사전 요구사항

* **Python 3.11+** (for Python apps)
* **Modern web browser** (for Web apps)
* **No external dependencies** — all single‑file & self‑contained

### 6.2 Run — Python | 실행 — Python

```bash
# Claude — L‑System (primary)
cd Claude-Opus-4.1/Python
python main.py --test
python main.py koch --iterations 3

# ChatGPT — Poetica Grammar Expander
cd ../../ChatGPT/Python
python main.py --test
python main.py --grammar "S -> hello world"

# Gemini — L‑System
cd ../../Gemini-2.5-Pro/Python
python main.py --test
python main.py dragon --iterations 5
```

### 6.3 Run — Web | 실행 — Web

* **Claude**: open `Claude-Opus-4.1/Web/Web.html`
* **ChatGPT**: open `ChatGPT/Web/Web.html`
* **Gemini**: open `Gemini-2.5-Pro/Web/Web.html`

> Tip: Double‑click to open locally or serve via a simple static server if preferred.

---

## 7) Implementation Highlights | 구현 하이라이트

### Claude Opus 4.1 — Sudoku Constraint Solver

* **AC‑3** propagation, backtracking + **MRV**
* Real‑time step visualization
* Deterministic puzzle generation (seeded PRNG)
* Accessibility & metrics (time, steps, conflicts)

### ChatGPT — NeatRows CSV/JSON Deduper & Normalizer

* Flexible CSV/JSON parsing (delimiters/quotes)
* Normalization: trim, collapse spaces, case, drop empty rows
* Hash‑based de‑dup with configurable keys
* Export: JSON/CSV, clipboard; table preview; self‑tests

### ChatGPT — Poetica Grammar Expander

* Weighted grammar DSL, pure/immutable core
* Type‑hints, robust errors; doctests
* Derivation tree visualization; JSON export; CLI UX

### Gemini — SVG Tiling Composer

* Procedural, seeded SVG patterns; multiple algorithms
* Modern CSS and responsive UI
* SVG copy/download (seeded filenames); determinism checks

### Gemini — L‑System Fractal Composer

* Efficient string expansion; generator‑based tracing
* ASCII grid rendering; deterministic presets

---

## 8) Error Resolution Analysis | 오류 해결 분석

**Common issues**: type annotations, edge‑case guards, constraint logic, large‑input performance, a11y gaps, responsive glitches, missing feedback.

**Resolution effectiveness**

| Model               | Bug Detection | Fix Quality | Time to Resolution |
| ------------------- | ------------- | ----------- | ------------------ |
| **Claude Opus 4.1** | ⭐⭐⭐⭐⭐         | ⭐⭐⭐⭐⭐       | ⭐⭐⭐⭐⭐              |
| **ChatGPT**         | ⭐⭐⭐⭐          | ⭐⭐⭐⭐        | ⭐⭐⭐⭐               |
| **Gemini 2.5 Pro**  | ⭐⭐⭐⭐          | ⭐⭐⭐⭐        | ⭐⭐⭐⭐               |

---

## 9) Key Insights | 주요 통찰

* **Claude**: best end‑to‑end quality; strongest UI/UX & algorithmic rigor
* **ChatGPT**: functional clarity; practical utilities; strong error handling
* **Gemini**: efficient, creative, well‑tested; scope/UI less deep than Claude

**Shared strengths**: single‑file architecture, modern practices, validation, documentation/testing

**Shared gaps**: edge cases, perf tuning, a11y depth, real‑world stress

---

## 10) Future Benchmarking | 향후 벤치마킹

* **Problem domains**: ML algorithms, visualization, games, sysadmin tools
* **Metrics**: performance, memory, security, maintainability
* **Real‑world**: UAT, cross‑platform, a11y compliance, load

---

## 11) Contributing | 기여하기

* Add new AI models
* Propose challenge domains
* Suggest metrics
* Improve docs/analysis

Please open a PR describing: model, prompts used, artifacts produced, and test notes.

---

## 12) License | 라이선스

MIT License. See `LICENSE` if present; otherwise include the MIT text in PRs adding new modules.

---

# (KO) 한국어 미러

## 1) 프로젝트 개요 | Project Overview

창의성과 엔지니어링 규율을 동시에 만족하는 **마스터피스급 단일 파일 애플리케이션** 제작 능력을 AI 모델 간에 비교하는 벤치마크입니다.

* **Python**: 제약 만족/알고리즘적 우아함
* **Web**: 인터랙티브·접근 가능한 단일 페이지
* **실제 테스트**: 오류 상황 구현 및 수정 성과

> **범위 고지**: 본 평가는 본 저장소의 프롬프트/산출물에 한정된 결과로, 일반적 순위와 동일하지 않을 수 있습니다.

---

## 2) 표준 저장소 구조 | Canonical Repository Layout

(영문 섹션과 동일 — 동일 경로/규칙 사용)

---

## 3) 벤치마킹 결과 | Benchmark Results

| 모델                  | Python 구현 | Web 구현 | 오류 해결 | 종합         |
| ------------------- | --------- | ------ | ----- | ---------- |
| **Claude Opus 4.1** | ⭐⭐⭐⭐⭐     | ⭐⭐⭐⭐⭐  | ⭐⭐⭐⭐⭐ | **95/100** |
| **ChatGPT**         | ⭐⭐⭐⭐      | ⭐⭐⭐⭐   | ⭐⭐⭐⭐  | **80/100** |
| **Gemini 2.5 Pro**  | ⭐⭐⭐⭐      | ⭐⭐⭐⭐   | ⭐⭐⭐⭐  | **75/100** |

하이라이트는 영문 섹션과 동일합니다.

---

## 4) 상세 분석 | Detailed Analysis

* **Claude Opus 4.1**: L‑System Fractal Composer (Python), Sudoku Constraint Solver (Web)
* **ChatGPT**: Poetica Grammar Expander (Python), NeatRows (Web)
* **Gemini 2.5 Pro**: L‑System Fractal Composer (Python), SVG Tiling Composer (Web)

각 항목의 강·약점, 알고리즘/접근성 포인트는 상단 영문 섹션과 일치합니다.

---

## 5) 테스트 방법론 | Methodology

가중치/절차는 영문 섹션과 동일합니다.

---

## 6) 시작하기 (단계별) | Getting Started (Step‑by‑Step)

사전 요구사항/실행 방법은 영문 섹션의 경로/명령과 동일합니다.

---

## 7) 구현 하이라이트 | Implementation Highlights

각 구현 요약은 영문 섹션과 동일합니다.

---

## 8) 오류 해결 분석 | Error Resolution

공통 이슈/효과성 표는 영문 섹션과 동일합니다.

---

## 9) 주요 통찰 | Key Insights

요약은 영문 섹션과 동일합니다.

---

## 10) 향후 벤치마킹 | Future Benchmarking

계획 항목은 영문 섹션과 동일합니다.

---

## 11) 기여하기 | Contributing

PR 개요(모델/프롬프트/산출물/테스트 노트)를 포함해 주세요.

---

## 12) 라이선스 | License

MIT License (동일).

---

