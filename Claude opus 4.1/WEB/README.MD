# ⚡ Sudoku Constraint Solver

A sophisticated, single-file Sudoku solver that demonstrates advanced constraint satisfaction algorithms with real-time visualization. Built with modern web technologies and featuring a beautiful, accessible interface.

## 🌟 Features

### Core Algorithm
- **Arc Consistency (AC-3)**: O(n²d³) constraint propagation algorithm
- **Backtracking Search**: O(9^m) worst-case with MRV (Minimum Remaining Values) heuristic
- **Deterministic Generation**: Reproducible puzzles using Mulberry32 PRNG
- **Real-time Visualization**: Watch the solver think through each step

### User Interface
- **Modern Design**: Glassmorphism with smooth animations and gradients
- **Responsive Layout**: Works on desktop and mobile devices
- **Dark/Light Mode**: Automatic theme switching based on system preference
- **Accessibility**: Full keyboard navigation, ARIA labels, and reduced-motion support

### Interactive Features
- **Multiple Difficulty Levels**: Easy (45 clues) to Expert (22 clues)
- **Step-by-step Solving**: Watch the algorithm work in real-time
- **Hint System**: Get suggestions for any cell
- **Conflict Detection**: Real-time validation and error highlighting
- **Performance Metrics**: Track solving time, steps, and conflicts

## 🚀 Usage

### Quick Start
1. Open `Web.html` in any modern web browser
2. Click "Generate" to create a new puzzle
3. Use the number pad or keyboard to fill cells
4. Click "Solve" to watch the algorithm work

### Keyboard Shortcuts
- `G` - Generate new puzzle
- `S` - Solve complete puzzle
- `Space` - Single solving step
- `H` - Get hint for selected cell
- `C` - Clear puzzle
- `1-9` - Enter number in selected cell
- `Delete/0` - Clear selected cell
- `Arrow keys` - Navigate grid
- `?` - Toggle help

### Difficulty Levels
- **Easy**: 45 clues (36 empty cells)
- **Medium**: 35 clues (46 empty cells)
- **Hard**: 28 clues (53 empty cells)
- **Expert**: 22 clues (59 empty cells)

## 🧠 Algorithm Details

### Arc Consistency (AC-3)
The solver uses the AC-3 algorithm to propagate constraints efficiently:
- Maintains domains of possible values for each cell
- Eliminates impossible values based on neighbor constraints
- Reduces search space before backtracking

### Backtracking with MRV
- **MRV Heuristic**: Always chooses the cell with the fewest remaining possible values
- **Forward Checking**: Updates domains when placing numbers
- **Conflict Detection**: Tracks and displays constraint violations

### Puzzle Generation
1. Creates a complete, valid Sudoku solution
2. Removes clues while maintaining unique solution
3. Uses deterministic PRNG for reproducible results

## 🎨 Technical Implementation

### Architecture
- **Single File**: Complete application in one HTML file
- **Vanilla JavaScript**: No external dependencies
- **CSS Grid**: Modern layout system for responsive design
- **CSS Custom Properties**: Dynamic theming and animations

### Performance Optimizations
- **Efficient Data Structures**: Sets for domain management
- **Minimal DOM Updates**: Batch rendering operations
- **CSS Transforms**: Hardware-accelerated animations
- **Reduced Motion**: Respects user accessibility preferences

### Browser Compatibility
- Modern browsers with ES6+ support
- CSS Grid and Custom Properties
- Performance API for timing measurements

## 🧪 Self-Testing

The application includes a comprehensive test suite:
- **Deterministic Generation**: Same seed produces same puzzle
- **Valid Puzzle Generation**: All clues are valid
- **Solver Correctness**: Solves known puzzles correctly
- **Arc Consistency**: Propagates constraints correctly
- **Hint Generation**: Provides valid hints
- **Performance**: Generation < 1s, solving < 500ms

## 📱 Accessibility Features

- **Keyboard Navigation**: Full control without mouse
- **Screen Reader Support**: ARIA labels and semantic HTML
- **Focus Management**: Clear visual indicators
- **Reduced Motion**: Respects `prefers-reduced-motion`
- **High Contrast**: Enhanced visibility options
- **Print Styles**: Clean output for printing

## 🎯 Educational Value

This project demonstrates:
- **Constraint Satisfaction Problems**: Real-world application of CSP algorithms
- **Algorithm Visualization**: Making complex algorithms understandable
- **Modern Web Development**: Best practices for single-page applications
- **User Experience Design**: Balancing functionality with aesthetics
- **Performance Engineering**: Optimizing for both speed and user experience

---

# ⚡ 스도쿠 제약 조건 해결기

고급 제약 만족 알고리즘을 실시간 시각화로 보여주는 정교한 단일 파일 스도쿠 해결기입니다. 최신 웹 기술로 구축되었으며 아름답고 접근 가능한 인터페이스를 제공합니다.

## 🌟 주요 기능

### 핵심 알고리즘
- **아크 일관성 (AC-3)**: O(n²d³) 제약 전파 알고리즘
- **백트래킹 검색**: MRV(최소 잔여 값) 휴리스틱을 사용한 O(9^m) 최악의 경우
- **결정적 생성**: Mulberry32 PRNG를 사용한 재현 가능한 퍼즐
- **실시간 시각화**: 해결기가 각 단계를 생각하는 과정을 지켜보세요

### 사용자 인터페이스
- **모던 디자인**: 부드러운 애니메이션과 그라데이션이 있는 글래스모피즘
- **반응형 레이아웃**: 데스크톱과 모바일 기기에서 작동
- **다크/라이트 모드**: 시스템 설정에 따른 자동 테마 전환
- **접근성**: 전체 키보드 네비게이션, ARIA 라벨, 모션 감소 지원

### 인터랙티브 기능
- **다양한 난이도**: 쉬움(45개 단서)부터 전문가(22개 단서)까지
- **단계별 해결**: 알고리즘이 실시간으로 작동하는 것을 지켜보기
- **힌트 시스템**: 모든 셀에 대한 제안 받기
- **충돌 감지**: 실시간 검증 및 오류 강조 표시
- **성능 지표**: 해결 시간, 단계, 충돌 추적

## 🚀 사용법

### 빠른 시작
1. 최신 웹 브라우저에서 `Web.html` 열기
2. "Generate" 클릭하여 새 퍼즐 생성
3. 숫자 패드 또는 키보드를 사용하여 셀 채우기
4. "Solve" 클릭하여 알고리즘 작동 지켜보기

### 키보드 단축키
- `G` - 새 퍼즐 생성
- `S` - 전체 퍼즐 해결
- `Space` - 단일 해결 단계
- `H` - 선택된 셀에 대한 힌트 얻기
- `C` - 퍼즐 지우기
- `1-9` - 선택된 셀에 숫자 입력
- `Delete/0` - 선택된 셀 지우기
- `화살표 키` - 그리드 탐색
- `?` - 도움말 토글

### 난이도 수준
- **쉬움**: 45개 단서 (36개 빈 셀)
- **보통**: 35개 단서 (46개 빈 셀)
- **어려움**: 28개 단서 (53개 빈 셀)
- **전문가**: 22개 단서 (59개 빈 셀)

## 🧠 알고리즘 세부사항

### 아크 일관성 (AC-3)
해결기는 AC-3 알고리즘을 사용하여 제약을 효율적으로 전파합니다:
- 각 셀의 가능한 값 도메인 유지
- 이웃 제약에 기반한 불가능한 값 제거
- 백트래킹 전 검색 공간 축소

### MRV를 사용한 백트래킹
- **MRV 휴리스틱**: 항상 가능한 값이 가장 적은 셀 선택
- **전방 검사**: 숫자를 배치할 때 도메인 업데이트
- **충돌 감지**: 제약 위반 추적 및 표시

### 퍼즐 생성
1. 완전하고 유효한 스도쿠 해답 생성
2. 고유한 해답을 유지하면서 단서 제거
3. 재현 가능한 결과를 위한 결정적 PRNG 사용

## 🎨 기술적 구현

### 아키텍처
- **단일 파일**: 하나의 HTML 파일에 완전한 애플리케이션
- **바닐라 자바스크립트**: 외부 의존성 없음
- **CSS 그리드**: 반응형 디자인을 위한 최신 레이아웃 시스템
- **CSS 커스텀 속성**: 동적 테마 및 애니메이션

### 성능 최적화
- **효율적인 데이터 구조**: 도메인 관리를 위한 세트
- **최소 DOM 업데이트**: 배치 렌더링 작업
- **CSS 변환**: 하드웨어 가속 애니메이션
- **모션 감소**: 사용자 접근성 선호도 존중

### 브라우저 호환성
- ES6+ 지원을 하는 최신 브라우저
- CSS 그리드 및 커스텀 속성
- 타이밍 측정을 위한 성능 API

## 🧪 자체 테스트

애플리케이션에는 포괄적인 테스트 스위트가 포함되어 있습니다:
- **결정적 생성**: 같은 시드가 같은 퍼즐 생성
- **유효한 퍼즐 생성**: 모든 단서가 유효함
- **해결기 정확성**: 알려진 퍼즐을 올바르게 해결
- **아크 일관성**: 제약을 올바르게 전파
- **힌트 생성**: 유효한 힌트 제공
- **성능**: 생성 < 1초, 해결 < 500ms

## 📱 접근성 기능

- **키보드 네비게이션**: 마우스 없이 전체 제어
- **스크린 리더 지원**: ARIA 라벨 및 시맨틱 HTML
- **포커스 관리**: 명확한 시각적 표시
- **모션 감소**: `prefers-reduced-motion` 존중
- **고대비**: 향상된 가시성 옵션
- **인쇄 스타일**: 인쇄를 위한 깔끔한 출력

## 🎯 교육적 가치

이 프로젝트는 다음을 보여줍니다:
- **제약 만족 문제**: CSP 알고리즘의 실제 응용
- **알고리즘 시각화**: 복잡한 알고리즘을 이해하기 쉽게 만들기
- **최신 웹 개발**: 단일 페이지 애플리케이션을 위한 모범 사례
- **사용자 경험 디자인**: 기능성과 미학의 균형
- **성능 엔지니어링**: 속도와 사용자 경험 모두 최적화
