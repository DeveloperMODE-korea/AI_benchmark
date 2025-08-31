물론입니다. `Web.html` 파일에 대한 `README.md` 파일을 아래와 같이 한국어와 영어로 작성해 드립니다.

---

# SVG Tiling Composer (`Web.html`)

This document is available in English and Korean.

- [English](#english)
- [한국어 (Korean)](#한국어-korean)

---

## English

### 概要 (Overview)

**SVG Tiling Composer** is a sophisticated single-file web application for generating procedural SVG tiling patterns. This project showcases disciplined, modern front-end engineering with zero dependencies, running entirely offline in the browser.

It is designed as a masterwork of portability and reliability—a complete, interactive application contained within a single `.html` file.

### ✨ Features

-   **100% Standalone:** A single `Web.html` file with no external libraries, fonts, or network requests.
-   **Deterministic Generation:** Create unique, repeatable patterns using a numeric seed. The same seed always produces the same output.
-   **Multiple Pattern Types:** Choose from different tiling algorithms like Truchet (circles), Slashes, and Polka Dots.
-   **Interactive Controls:** Easily change the seed and pattern type, then generate, copy, or download the resulting SVG.
-   **Modern Theming:** Supports system-preferred, light, and dark modes, plus a high-contrast option for accessibility.
-   **Fully Accessible:** Designed with keyboard navigation, ARIA roles, and high-contrast compliance in mind.
-   **Built-in Diagnostics:** Includes in-page Help and a Self-Test panel to verify functionality and determinism.

### 🚀 How to Use

1.  Download the `Web.html` file.
2.  Open it in any modern web browser (e.g., Chrome, Firefox, Safari, Edge).
3.  The application is ready to use immediately. No internet connection or build steps required.

### ⌨️ Keyboard Shortcuts

-   **`G`**: Generate a new pattern.
-   **`C`**: Copy the current SVG code to the clipboard.
-   **`H`**: Toggle the Help panel.
-   **`T`**: Toggle and run the Self-Test suite.

### 🛠️ Technical Highlights

-   **Pure HTML/CSS/JS:** Built without any frameworks or libraries.
-   **Modern CSS:** Utilizes `@layer`, CSS Custom Properties (Design Tokens), Flexbox, and Grid for a clean and maintainable stylesheet.
-   **Scoped JavaScript:** All JS code is contained within a `<script type="module">` tag to prevent global namespace pollution.
-   **Performance-Aware:** Efficient SVG generation and DOM updates ensure a smooth user experience with zero console errors.

---

## 한국어 (Korean)

### 概要 (개요)

**SVG 타일링 컴포저**는 절차적으로 SVG 타일링 패턴을 생성하는 정교한 단일 파일 웹 애플리케이션입니다. 이 프로젝트는 의존성 없이, 완전히 오프라인 환경의 브라우저에서 실행되는 체계적이고 현대적인 프론트엔드 엔지니어링을 보여줍니다.

이동성과 신뢰성의 걸작으로 설계되었으며, 상호작용 가능한 완전한 애플리케이션이 단일 `.html` 파일 안에 담겨 있습니다.

### ✨ 주요 기능

-   **100% 독립 실행:** 외부 라이브러리, 폰트, 네트워크 요청이 없는 단일 `Web.html` 파일입니다.
-   **결정론적 생성:** 숫자 시드(Seed)를 사용하여 독특하고 반복 가능한 패턴을 만듭니다. 동일한 시드는 항상 동일한 결과를 생성합니다.
-   **다양한 패턴 타입:** 트루셰(Truchet, 원형), 슬래시(Slashes), 폴카 도트(Polka Dots) 등 다양한 타일링 알고리즘 중에서 선택할 수 있습니다.
-   **인터랙티브 컨트롤:** 시드와 패턴 타입을 쉽게 변경하고, 결과 SVG를 생성, 복사, 또는 다운로드할 수 있습니다.
-   **최신 테마 지원:** 시스템 설정, 라이트/다크 모드를 지원하며, 접근성을 위한 고대비 옵션도 제공합니다.
-   **완벽한 접근성:** 키보드 내비게이션, ARIA 역할, 고대비 규격을 고려하여 설계되었습니다.
-   **자체 진단 기능:** 앱 내 도움말과 자체 테스트 패널을 포함하여 기능과 결정론적 동작을 검증합니다.

### 🚀 사용 방법

1.  `Web.html` 파일을 다운로드합니다.
2.  최신 웹 브라우저(Chrome, Firefox, Safari, Edge 등)에서 파일을 엽니다.
3.  인터넷 연결이나 빌드 과정 없이 즉시 사용할 수 있습니다.

### ⌨️ 키보드 단축키

-   **`G`**: 새 패턴 생성.
-   **`C`**: 현재 SVG 코드를 클립보드에 복사.
-   **`H`**: 도움말 패널 토글.
-   **`T`**: 자체 테스트 패널 토글 및 실행.

### 🛠️ 기술적 특징

-   **순수 HTML/CSS/JS:** 프레임워크나 라이브러리 없이 제작되었습니다.
-   **모던 CSS:** `@layer`, CSS Custom Properties (디자인 토큰), Flexbox, Grid를 활용하여 깔끔하고 유지보수 가능한 스타일시트를 구현했습니다.
-   **스코프된 JavaScript:** 모든 JS 코드는 `<script type="module">` 태그 안에 작성되어 전역 네임스페이스 오염을 방지합니다.
-   **성능 고려:** 효율적인 SVG 생성과 DOM 업데이트로 콘솔 오류 없이 부드러운 사용자 경험을 보장합니다.