# NeatRows — CSV/JSON Deduper & Normalizer (Single‑File: `Web.html`)

> **One HTML file. Zero dependencies. 100% offline.**

---

## 🧭 Table of Contents

* [🇰🇷 한국어 안내](#-한국어-안내)
* [🇺🇸 English Guide](#-english-guide)

---

## 🇰🇷 한국어 안내

### 개요

`Web.html`은 **CSV/JSON 데이터를 정규화하고(공백·대소문자·키 표준화) 중복을 제거**한 뒤, 미리보기/복사/다운로드를 제공하는 **단일 파일 웹 앱**입니다. 모든 로직과 스타일, 스크립트가 **한 파일**에 포함되어 있으며, **네트워크 연결 없이 오프라인**에서 동작합니다.

### 핵심 특징

* **단일 파일**: `Web.html` 하나만 열면 실행됩니다. 설치/빌드/의존성 없음.
* **결정적 동작(Deterministic)**:

  * **Seed** 값으로 샘플링 결과가 항상 동일합니다.
  * **Realtime Clock** 스위치로 타임스탬프를 실시간/고정 시간 중 선택.
* **데이터 정규화**: Trim, 공백 축약, 값/키 소문자화, 빈 행 제거.
* **중복 제거**: 키(쉼표 구분)를 지정하면 해당 키 조합으로 중복 제거. 비우면 전체 행 기준.
* **입력 형식**: CSV(구분자/따옴표/헤더 설정) 또는 JSON(객체 배열) 자동 처리.
* **미리보기 & 내보내기**: 테이블 미리보기(최대 15행), **JSON/CSV 다운로드**, **클립보드 복사**.
* **접근성 중심**: 키보드 전용 사용 가능, 고대비/감쇠 모션, 명확한 포커스 링, ARIA 라이브 상태.
* **국제화(i18n)**: **한국어/영어** UI 지원.
* **자체 점검(Self‑Test)**: 정상/엣지/오류 경로 테스트 내장.
* **성능 지표**: 실행 횟수, 처리 지연(ms), 렌더 노드 수 표시.
* **인쇄 최적화**: 불필요 패널 숨김, 본문 가독성 향상.

### 빠른 시작

1. `Web.html` 파일을 더블클릭하여 브라우저(Chrome/Edge/Firefox/Safari)로 엽니다.
2. **Data** 영역에 CSV 또는 JSON(객체 배열) 데이터를 붙여넣습니다.
3. **Options**에서 형식(CSV/JSON), 정규화 옵션, 중복 제거 키를 설정합니다.
4. 상단에서 **Seed**(필요 시)와 **Realtime Clock**을 조정합니다.
5. **Run (R)** 버튼을 클릭하면 처리 결과가 **Preview** 및 \*\*Raw(JSON)\*\*에 표시됩니다.
6. **Copy (C)** 또는 **Download**(JSON/CSV)를 사용해 결과를 가져갑니다.

### 입력 예시

**CSV**

```csv
id,name,email
1,Ada,ada@example.com
2,Grace,grace@example.com
2,Grace , Grace@example.com
3,alan,alan@example.com
```

**JSON**

```json
[
  {"id":1,"name":"Ada","email":"ada@example.com"},
  {"id":2,"name":"Grace","email":"grace@example.com"},
  {"id":2,"name":"Grace ","email":"Grace@example.com"},
  {"id":3,"name":"alan","email":"alan@example.com"}
]
```

### 키보드 단축키

* **R**: 실행 (Run)
* **H**: 도움말 토글 (Help)
* **T**: 자체 테스트 실행 (Self‑Test)
* **C**: Raw(JSON) 복사 (Copy)
* **?**: 단축키 패널 토글
* **Esc**: 열려 있는 패널 닫기

### 결정성(Determinism)

* **Seed** 입력값이 같으면, **샘플 미리보기** 결과 순서가 항상 동일합니다.
* 내장 PRNG(`mulberry32`)와 **Fisher‑Yates** 셔플로 구현.
* **Realtime Clock**을 끄면 고정된 타임스탬프를 사용하여 내보내기 파일명이 항상 재현됩니다.

### 접근성 & 사용성

* 모든 입력에 레이블 제공, 포커스 이동 순서 시각 순서와 일치.
* `aria-live`로 상태 전달(결과/지표/토스트), 색상만으로 의미 전달하지 않도록 배지/텍스트 병기.
* `prefers-reduced-motion` 존중, **고대비(High Contrast)** 모드 제공.

### 성능 & 복잡도

* **CSV 파싱**: 인용부호/이스케이프 처리 포함 **O(n)** 1패스.
* **정규화/중복 제거**: 해시셋 기반 키 시그니처로 **O(m)**.
* 미리보기는 최대 15행으로 제한(전체 내보내기는 전체 레코드 사용).

### 내보내기 & 인쇄

* **Download**: JSON/CSV 중 선택, 파일명에 ISO 타임스탬프 포함.
* **Copy**: Raw(JSON) 텍스트를 클립보드로.
* **Print**: 도움말/테스트/입력 패널 숨김, 결과 중심 출력.

### 보안/프라이버시

* 네트워크 요청 없음(오프라인). 클립보드는 **사용자 동작 시**에만 접근.
* HTML 인젝션 방지를 위해 텍스트 콘텐츠로 렌더링(테이블 셀/프리뷰).

### 문제 해결 (Troubleshooting)

* **JSON 오류**: "JSON must be an array" 또는 구문 오류 → 루트가 배열인지 확인.
* **CSV 이상**: 따옴표/구분자 설정 재확인, 헤더 유무 체크.
* **파일 다운로드 안 됨**: 브라우저의 팝업/다운로드 차단 해제.
* **콘솔 경고/오류**: 이 앱은 0 경고/오류를 목표로 설계됨. 재현 가능한 경우 이슈 섹션 참고.

### 브라우저 지원

* 최신 Chrome/Edge/Firefox/Safari(데스크톱/모바일) 지향. Internet Explorer 미지원.

### 커스터마이징 팁

* 색상·간격·테마 토큰: `:root`의 CSS 커스텀 프로퍼티 수정.
* 미리보기 행 수/기본 Seed/고정 시각: 스크립트 상단 상수 변경.
* 언어 추가: `STR` 오브젝트에 번역 키 추가.

### 파일 구조

```
./Web.html  ← 이 저장소의 전부 (HTML+CSS+JS 단일 파일)
```

### 라이선스

* **MIT License**. 소스 코드/문서 재사용 시 라이선스 고지 유지.

### 변경 기록

* **v1.0.0** — 첫 공개 버전 (단일 파일, 결정적 샘플링, a11y, Self‑Test 포함)

---

## 🇺🇸 English Guide

### Overview

`Web.html` is a **single‑file web app** that **normalizes** (trim/space collapse/case) and **deduplicates** CSV/JSON data, then offers preview/copy/download — all **offline** in one file. No builds, no dependencies.

### Highlights

* **Single file**: open `Web.html` and you’re set. No install/build/CDN.
* **Deterministic**:

  * A visible **Seed** ensures identical sampling order for the same input.
  * **Realtime Clock** toggle switches between fixed and system time.
* **Normalization**: trim, collapse spaces, lowercase values/keys, drop empty rows.
* **Dedupe**: enter comma‑separated keys to deduplicate by; empty means full‑row signature.
* **Input formats**: CSV (configurable delimiter/quote/header) or JSON (array of objects).
* **Preview & export**: table preview (up to 15 rows), **JSON/CSV download**, **Copy to clipboard**.
* **Accessibility‑first**: keyboard‑operable, high‑contrast, reduced motion, visible focus, ARIA live regions.
* **i18n**: **English/Korean** UI.
* **Self‑Test**: built‑in checks for nominal/edge/error and determinism.
* **Metrics**: runs, last latency, DOM nodes rendered.
* **Print**: hides auxiliary panels for clean output.

### Quick Start

1. Open `Web.html` in a modern browser (Chrome/Edge/Firefox/Safari).
2. Paste CSV or a JSON array into **Data**.
3. Configure **Options** (format/normalization/keys).
4. Adjust **Seed** and **Realtime Clock** if needed.
5. Click **Run (R)** to transform; inspect **Preview**/**Raw**.
6. Use **Copy (C)** or **Download** (JSON/CSV) to export.

### Input Examples

See the CSV/JSON samples above (identical across languages).

### Keyboard Shortcuts

* **R**: Run — **H**: Help — **T**: Self‑Test — **C**: Copy Raw — **?**: Shortcuts — **Esc**: Close panels

### Determinism

* Same **Seed** ⇒ identical **sample preview order** every time.
* Implemented with a tiny `mulberry32` PRNG and **Fisher‑Yates** shuffle.
* With Realtime Clock **off**, export filenames use a fixed timestamp.

### Accessibility & UX

* Proper labels and DOM order; `aria-live` updates for results/toasts/metrics.
* High contrast mode and reduced‑motion compliance.
* Status badges never rely on color alone.

### Performance & Complexity

* **CSV parse** handles quotes/escapes in **O(n)** single pass.
* **Normalize/Dedupe** are **O(m)** over records via hash signatures.
* Preview limited to 15 rows for snappy paint; exports include the full set.

### Export & Print

* **Download** as JSON/CSV (ISO timestamp in the filename).
* **Copy** raw JSON to clipboard.
* **Print** presents a clean summary.

### Security & Privacy

* No network access. Clipboard used **only** on explicit user action.
* Outputs rendered as text to avoid HTML injection.

### Troubleshooting

* **Invalid JSON**: root must be an array; fix syntax and try again.
* **CSV issues**: verify delimiter/quote/header settings.
* **Download blocked**: allow downloads/pop‑ups for local files.
* **Console noise**: design aims for zero warnings/errors; please report reproducible cases.

### Browser Support

* Recent Chrome/Edge/Firefox/Safari (desktop/mobile). Internet Explorer not supported.

### Customization Tips

* Theme tokens in `:root`; adjust spacing/colors/contrast as needed.
* Change default seed/preview rows/fixed time in script constants.
* Add locales by extending the `STR` map.

### File Layout

```
./Web.html  ← the entire app (HTML+CSS+JS in a single file)
```

### License

* **MIT License**. Keep license notice in copies/substantial portions.

### Changelog

* **v1.0.0** — Initial public release (deterministic sampler, a11y, self‑tests)
