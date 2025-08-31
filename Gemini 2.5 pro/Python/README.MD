물론입니다. `L-System Fractal Composer` 프로그램을 위한 `README.md` 파일을 한국어와 영어로 작성해 드리겠습니다.

---

# L-System Fractal Composer

## (In English)

### Overview

**L-System Fractal Composer** is a single-file, dependency-free Python 3.11+ program that generates and visualizes 2D fractal structures using Lindenmayer systems (L-Systems). It is designed as a masterwork of programming—clear, cohesive, and elegant—balancing creative output with strict engineering discipline.

The program takes a simple set of rules (an axiom and production rules) and iteratively expands them to generate a complex string. This string is then interpreted by a "turtle" graphics engine to draw the resulting fractal pattern as ASCII art directly in your terminal.



### Features

-   **Single-File & Portable:** Runs anywhere with Python 3.11+ without any installation or external libraries.
-   **ASCII Visualization:** Renders fractals as clean, text-based art in the console.
-   **JSON Output:** Provides an option to output the generated path data in a structured JSON format for use in other applications.
-   **Built-in Presets:** Includes classic fractals like the Koch curve, Dragon curve, and Sierpinski triangle for immediate use.
-   **Highly Customizable:** Define your own axiom, rules, turn angles, and iteration depth to discover new patterns.
-   **Professional CLI:** A polished command-line interface powered by `argparse` with clear help, error handling, and options.
-   **Self-Contained Tests:** Includes a built-in `unittest` suite that can be run with a simple `--test` flag to verify correctness.
-   **Deterministic by Default:** Every run with the same inputs produces the exact same output.

### Requirements

-   Python 3.11 or newer.

### Installation

No installation is needed. Simply download the `main.py` file and run it with Python.

```bash
git clone <repository_url>
cd <repository_directory>
# Or just download main.py
```

### Usage

The script is controlled via command-line arguments.

#### 1. Displaying Help

To see all available commands and options, use the `--help` flag.

```bash
python main.py --help
```

#### 2. Running Built-in Tests

To ensure the program is working correctly, run the self-contained test suite.

```bash
python main.py --test
```

#### 3. Using Presets

You can easily generate a built-in fractal by providing its name.

```bash
# Generate the Koch curve
python main.py koch

# Generate the Dragon curve with more iterations
python main.py dragon --iterations 12

# Generate the Sierpinski triangle
python main.py sierpinski
```

#### 4. Using Custom Rules

Create your own fractal by providing an axiom and a set of rules.

```bash
# A simple fractal plant
python main.py "X" "X=F+[[X]-X]-F[-FX]+X" "F=FF" --angle 25 --iterations 5
```

#### 5. JSON Output

To get the raw path data instead of an ASCII drawing, use the `--format json` flag. This is useful for piping the output to other visualization tools.

```bash
python main.py koch --iterations 2 --format json
```

### Technical Design

This program is a demonstration of disciplined yet creative Python design. Its key principles include:

-   **Immutability:** Domain objects like `TurtleState` are immutable `dataclasses`, preventing side effects and making state management trivial.
-   **Functional Core:** The core logic (parsing, expansion, tracing) is composed of pure functions that are easy to test and reason about.
-   **Generators:** The `trace_path` function uses a generator to lazily produce path segments, which is memory-efficient for very large command strings.
-   **Clarity and Readability:** Every function and class is fully type-hinted and documented. The code structure is organized logically from top to bottom.
-   **Judicious Feature Use:** Advanced Python features like `match` statements and `itertools` are used only where they genuinely improve clarity and performance.

### License

This project is licensed under the MIT License.

---

## (In Korean / 한국어)

### 개요

**L-System 프랙탈 생성기**는 린덴마이어 시스템(L-System)을 사용하여 2D 프랙탈 구조를 생성하고 시각화하는 단일 파일, 의존성 없는 Python 3.11+ 프로그램입니다. 이 프로그램은 명확하고, 응집력 있으며, 우아한 프로그래밍의 정수를 보여주기 위해 설계되었으며, 창의적인 결과물과 엄격한 엔지니어링 원칙 사이의 균형을 맞춥니다.

프로그램은 간단한 규칙 집합(공리 및 생성 규칙)을 입력받아 반복적으로 확장하여 복잡한 문자열을 생성합니다. 이후 "거북이" 그래픽 엔진이 이 문자열을 해석하여 결과적인 프랙탈 패턴을 터미널에 직접 ASCII 아트로 그립니다.



### 주요 기능

-   **단일 파일 및 이식성:** Python 3.11+만 있으면 어디서든 설치나 외부 라이브러리 없이 실행됩니다.
-   **ASCII 시각화:** 프랙탈을 콘솔에 깔끔한 텍스트 기반 아트로 렌더링합니다.
-   **JSON 출력:** 생성된 경로 데이터를 다른 애플리케이션에서 사용할 수 있도록 구조화된 JSON 형식으로 출력하는 옵션을 제공합니다.
-   **내장 프리셋:** 코흐 곡선, 드래곤 커브, 시에르핀스키 삼각형과 같은 클래식 프랙탈이 포함되어 바로 사용할 수 있습니다.
-   **높은 사용자 정의 기능:** 자신만의 공리, 규칙, 회전 각도, 반복 깊이를 정의하여 새로운 패턴을 발견할 수 있습니다.
-   **전문적인 CLI:** `argparse`로 구현된 세련된 커맨드 라인 인터페이스는 명확한 도움말, 오류 처리 및 다양한 옵션을 제공합니다.
-   **자체 포함 테스트:** 간단한 `--test` 플래그로 실행하여 정확성을 검증할 수 있는 내장 `unittest` 스위트가 포함되어 있습니다.
-   **결정론적 기본 동작:** 동일한 입력에 대해 실행할 때마다 항상 동일한 결과가 생성됩니다.

### 요구 사항

-   Python 3.11 또는 그 이상 버전.

### 설치

별도의 설치 과정이 필요 없습니다. `main.py` 파일을 다운로드하여 Python으로 실행하기만 하면 됩니다.

```bash
git clone <repository_url>
cd <repository_directory>
# 또는 main.py 파일만 다운로드
```

### 사용법

스크립트는 커맨드 라인 인자를 통해 제어됩니다.

#### 1. 도움말 확인

사용 가능한 모든 명령어와 옵션을 보려면 `--help` 플래그를 사용하세요.

```bash
python main.py --help
```

#### 2. 내장 테스트 실행

프로그램이 올바르게 작동하는지 확인하려면 자체 포함된 테스트 스위트를 실행하세요.

```bash
python main.py --test
```

#### 3. 프리셋 사용하기

내장된 프랙탈의 이름을 지정하여 쉽게 생성할 수 있습니다.

```bash
# 코흐 곡선 생성
python main.py koch

# 드래곤 커브를 더 많은 반복으로 생성
python main.py dragon --iterations 12

# 시에르핀스키 삼각형 생성
python main.py sierpinski
```

#### 4. 사용자 정의 규칙 사용하기

공리와 규칙 집합을 제공하여 자신만의 프랙탈을 만들 수 있습니다.

```bash
# 간단한 프랙탈 식물
python main.py "X" "X=F+[[X]-X]-F[-FX]+X" "F=FF" --angle 25 --iterations 5
```

#### 5. JSON 출력

ASCII 그림 대신 원시 경로 데이터를 얻으려면 `--format json` 플래그를 사용하세요. 이 출력은 다른 시각화 도구로 파이핑할 때 유용합니다.

```bash
python main.py koch --iterations 2 --format json
```

### 기술적 설계

이 프로그램은 절제되면서도 창의적인 파이썬 설계의 모범 사례를 보여줍니다. 핵심 원칙은 다음과 같습니다.

-   **불변성(Immutability):** `TurtleState`와 같은 도메인 객체는 불변 `dataclass`로 구현되어 부작용을 방지하고 상태 관리를 단순화합니다.
-   **함수형 코어:** 핵심 로직(파싱, 확장, 추적)은 테스트하고 이해하기 쉬운 순수 함수로 구성됩니다.
-   **제너레이터(Generators):** `trace_path` 함수는 제너레이터를 사용하여 경로 세그먼트를 지연 생성함으로써 매우 긴 명령어 문자열에 대해서도 메모리를 효율적으로 사용합니다.
-   **명확성과 가독성:** 모든 함수와 클래스에는 타입 힌트와 문서가 완벽하게 작성되어 있습니다. 코드 구조는 위에서 아래로 논리적으로 구성되어 있습니다.
-   **현명한 기능 사용:** `match` 문이나 `itertools`와 같은 고급 파이썬 기능은 명확성과 성능을 실질적으로 향상시키는 경우에만 사용되었습니다.

### 라이선스

이 프로젝트는 MIT 라이선스에 따라 배포됩니다.
