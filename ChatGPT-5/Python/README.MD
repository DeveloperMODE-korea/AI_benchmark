# Poetica — Tiny Weighted Grammar Expander

> **KR/EN Bilingual README** · **Python 3.11+**, **Single file**, **Stdlib‑only**, **Deterministic by seed**

---

## 목차 (Table of Contents)

1. 개요 (Overview)
2. 특징 (Features)
3. 빠른 시작 (Quickstart)
4. 사용법 (CLI Usage)
5. 예시 (Examples)
6. 문법 DSL 설명 (Grammar DSL)
7. JSON 출력 스키마 (JSON Output Schema)
8. 결정성 & 난수 (Determinism)
9. 성능 & 튜닝 (Performance & Tuning)
10. 테스트 (Testing)
11. 설계 노트 (Design Notes)
12. 문제 해결 (Troubleshooting)
13. 임베딩 가이드 (Embedding as a Library)
14. 보안 및 제약 (Security & Limitations)
15. FAQ
16. 라이선스 (License)

---

## 개요 (Overview)

**Poetica**는 가벼운 **가중치 기반 문법(DSL)** 로부터 텍스트를 **결정적(재현 가능)** 으로 생성하는, 단일 파일 파이썬 프로그램입니다. 좌측에서부터 비단말 기호를 확장하는 **가중 좌측최대 파생(Leftmost Derivation)** 을 사용하며, 결과를 **텍스트** 또는 **JSON 파생 트리**로 출력합니다. 코드는 의존성 없이 표준 라이브러리(`argparse`, `dataclasses`, `shlex`, `random`, `json`)만 사용하고, 읽기 쉬운 구조와 실용적 기능을 중시합니다.

Poetica는 **프롬프트/카피/게임 텍스트** 제작, **테스트 데이터** 생성, **템플릿 문장 다양화**, **학습용 문법 실험** 등 다양한 목적에 적합합니다. 모든 실행은 시드 기반으로 재현 가능하며, 좌재귀 또는 폭주 성장에 대비해 **명시적 안전 한계**를 제공합니다.

---

## 특징 (Features)

* 🧾 **미니 DSL**: `LHS -> alt1 | alt2 *3` 구문. 대안 끝의 `*k`로 가중치.
* 🌱 **결정적 실행**: `--seed` 지정 시 동일 입력은 동일 결과.
* 🌳 **파생 트리 JSON**: `--format json`으로 전체 트리 확인 가능.
* 🧰 **단일 파일·무의존성**: 설치 없이 바로 실행.
* 🧪 **자체 테스트 포함**: `python main.py --test`로 2초 내 검증.
* 🧯 **안전장치**: `--max-steps`, `--max-tokens`로 무한성장 방지.
* 🧠 **문장 미려화**: `smart_join()` 으로 구두점 앞 공백 제거 및 `'s` 결합.
* 🧩 **견고한 토크나이징**: `shlex`로 공백 포함 단말(예: "New York") 처리.
* 🧭 **명확한 오류**: `GrammarError`, `GenerationLimitError` 로 도메인 친화적 에러 메시지.

---

## 빠른 시작 (Quickstart)

```bash
python main.py --help
python main.py --seed 1 --format text
```

> 기본 실행은 내장 예시 문법을 사용합니다. 만약 `Undefined nonterminals: Name` 같은 오류가 보이면 사용자 정의 문법을 `--grammar` 로 넘기거나, 문법에 `Name` 규칙을 추가하세요. 아래 **권장 예시 문법**을 사용하면 안전합니다.

### 권장 예시 문법 (Recommended grammar)

**Bash/Zsh** (멀티라인 환경변수):

```bash
read -r -d '' G <<'GRAM'
S  -> NP VP . | Name VP . *2
NP -> Det N   | Det Adj N    | Name
VP -> V NP    | V Adv        | V
Det -> the | a
N   -> fox | dog | code | idea
Adj -> quick | elegant | careful
V   -> jumps | writes | tests | flows
Adv -> swiftly | beautifully | precisely
Name -> Alice | Bob | "Ada Lovelace"
. -> .
GRAM
python main.py --grammar "$G" --seed 7
```

**PowerShell**:

```powershell
$G = @"
S  -> NP VP . | Name VP . *2
NP -> Det N   | Det Adj N    | Name
VP -> V NP    | V Adv        | V
Det -> the | a
N   -> fox | dog | code | idea
Adj -> quick | elegant | careful
V   -> jumps | writes | tests | flows
Adv -> swiftly | beautifully | precisely
Name -> Alice | Bob | "Ada Lovelace"
. -> .
"@
python .\main.py --grammar "$G" --seed 7
```

---

## 사용법 (CLI Usage)

```bash
python main.py [--seed SEED] [--start SYMBOL]
               [--max-steps N] [--max-tokens N]
               [--format {text,json}] [--verbose]
               [--grammar "<grammar text>"]
               [--test]
```

* `--seed`: 결정적 생성 시드 (기본: 1)
* `--start`: 시작 심볼 (기본: `S`)
* `--format`: `text` 또는 `json`
* `--verbose`: 파생 과정을 로그로 출력
* `--grammar`: 인라인 문법 텍스트 (미제공 시 내장 문법 시도)
* `--max-steps`, `--max-tokens`: 안전 제한치
* `--test`: doctest + unittest 실행 후 종료

---

## 예시 (Examples)

```bash
# 1) 텍스트 출력 (결정적)
python main.py --grammar "$G" --seed 1

# 2) 파생 트리 JSON 전체 보기
python main.py --grammar "$G" --format json

# 3) 파생 텍스트만 추출 (jq 사용)
python main.py --grammar "$G" --format json | jq -r .text

# 4) 확장 로그 보기
python main.py --grammar "$G" --verbose

# 5) 시작 심볼 변경
python main.py --grammar "$G" --start NP --seed 3

# 6) 안전 한계 조정
python main.py --grammar "$G" --max-steps 200 --max-tokens 400

# 7) 테스트 실행
python main.py --test
```

샘플 출력 (예시):

```
the elegant code flows.
```

---

## 문법 DSL 설명 (Grammar DSL)

* **규칙 형식**: `LHS -> alt1 | alt2 | ...`
* **비단말(Nonterminal)**: `UpperCamelCase` 토큰 (`S`, `NP`, `Det` 등)
* **단말(Terminal)**: 그 외 토큰. 공백 포함 토큰은 `"..."`로 감싸기 (예: `"New York"`).
* **가중치(Weight)**: 대안 끝에 `*k` (정수, k ≥ 1). 예: `VP -> V NP *2 | V` 는 첫 대안을 두 배로 선호.
* **주석**: `#` 로 시작하는 줄은 무시됩니다.
* **구두점**: `, . ; : ! ?` 같은 토큰은 출력 시 앞 공백 없이 붙습니다. `'s` 는 직전 단어와 결합됩니다.
* **정의 요건**: 사용된 모든 비단말은 최소 한 번 이상 **정의** 되어야 합니다. 미정의 시 `GrammarError`.

### 인용과 이스케이프 (Quoting & Escapes)

* 공백/특수문자가 포함된 단말은 반드시 `"..."`로 감쌉니다.
* 따옴표 내부의 따옴표는 표준 `shlex` 규칙에 따릅니다. 예: `"\"quoted\" word"`.

### 좌재귀 회피 팁 (Avoiding Left Recursion)

좌재귀는 폭주를 유발할 수 있습니다. 예:

```
Bad:  Expr -> Expr "+" Term | Term
Good: Expr -> Term ExprTail
      ExprTail -> "+" Term ExprTail | ε   # ε는 빈 대안을 의미(문법상 직접 표기 금지)
```

> Poetica는 빈 문자열(ε)을 직접 표기하지 않습니다. 대신 `Optional` 같은 비단말을 만들어 `Optional -> nothing | something` 형태로 우회하세요.

---

## JSON 출력 스키마 (JSON Output Schema)

```json
{
  "text": "the elegant code flows.",
  "tree": {
    "label": "S",
    "children": [
      { "label": "NP", "children": [
        { "label": "Det", "children": [{"terminal": "the"}] },
        { "label": "Adj", "children": [{"terminal": "elegant"}] },
        { "label": "N",   "children": [{"terminal": "code"}] }
      ]},
      { "label": "VP", "children": [
        { "label": "V", "children": [{"terminal": "flows"}] }
      ]},
      { "terminal": "." }
    ]
  }
}
```

* 각 노드는 `{ "label": <비단말명>, "children": [...] }` 형태입니다.
* 단말 토큰은 `{ "terminal": <문자열> }` 로 표현됩니다.
* `text` 필드는 `smart_join()` 규칙이 적용된 최종 결과 문자열입니다.

---

## 결정성 & 난수 (Determinism)

* 난수는 `random.Random(seed)` 기반의 **정수 가중 선택**으로 구현되어 **부동소수 오차**의 영향이 없습니다.
* 동일한 **문법/시드/파라미터** 조합은 OS/환경에 상관없이 **항상 동일한 결과**를 만듭니다.
* 새로운 변주가 필요하면 **시드만 변경**하세요.

---

## 성능 & 튜닝 (Performance & Tuning)

* **복잡도**: `m`=확장 단계 수, `k`=평균 대안 수일 때 시간 `O(m * k)` / 메모리 `O(total_symbols)`.
* **튜닝 포인트**:

  * 긴 문장을 원하면 `--max-steps`, `--max-tokens` 값을 늘리세요.
  * 매우 가지가 많은 문법은 가중치로 확장을 유도해 평균 분기수를 낮추세요.
  * 좌재귀/순환은 가급적 제거하거나 재귀 깊이를 얕게 만드는 구조로 바꾸세요.
* 기본 입력 크기에서 **< 1초** 실행을 목표로 설계되었습니다.

---

## 테스트 (Testing)

```bash
python main.py --test
```

* **Doctest**: 작은 사용 예를 문서화하며 동시 검증합니다.
* **Unittest**: 정상 생성, 미정의 심볼 오류, 제한치 감지 등 **대표 시나리오 3가지 이상**을 검증합니다.
* 테스트는 2초 내 완료되도록 구성되어 CI에도 적합합니다.

---

## 설계 노트 (Design Notes)

* **좌측 최대 파생 + 가중 선택**: 추적 가능한 전개 순서 보장.
* **정수 기반 가중 선택**: 부동소수점 누적 오차 회피.
* **데이터 클래스**: `Rule/Production` 은 불변, `Node` 는 트리 조립을 위해 최소 가변.
* **`shlex` 토크나이저**: 인용된 단말과 쉘 친화적 입력을 안전 파싱.
* **출력 미려화**: `smart_join()` 으로 자연스러움 확보 (구두점/소유격 처리).
* **명확한 계층**: 상수 → 타입 → 핵심 로직 → CLI → 테스트의 일관된 파일 흐름.

---

## 문제 해결 (Troubleshooting)

* **`Undefined nonterminals: X`**: 문법에서 사용한 모든 비단말을 정의했는지 확인하세요.
* **Windows PowerShell에서 따옴표 문제**: 멀티라인 문자열은 `@"..."@` 구문을 사용하세요.
* **문장에 공백 포함 토큰이 깨짐**: 단말을 반드시 `"..."` 로 감싸세요.
* **끝나지 않는 확장/매우 긴 시간**: 좌재귀, 순환, 과한 분기를 의심하고 가중치/한계를 조정하세요.
* **구두점 앞에 공백이 생김**: 구두점이 단일 토큰인지 확인하세요. 예: `.` 를 다른 토큰과 합치지 마세요.

---

## 임베딩 가이드 (Embedding as a Library)

Poetica는 모듈로 임포트하여 사용할 수 있습니다.

```python
from main import parse_grammar, expand

G = """
S -> hello , world .
"""

grammar = parse_grammar(G)
text, tree = expand(grammar, seed=42)
print(text)  # hello, world.
```

* **불변성**: `Rule`/`Production` 은 불변이므로 캐싱/공유에 안전합니다.
* **트리 가공**: `tree.to_dict()` 로 직렬화하여 시각화/후처리에 활용하세요.

---

## 보안 및 제약 (Security & Limitations)

* **파일/네트워크 I/O 없음**: 의도치 않은 부작용이 없습니다.
* **임의 코드 실행 없음**: DSL은 순수 선언형입니다.
* **빈 문자열(ε) 직접 표기 불가**: `Optional` 패턴으로 우회 구현 필요.
* **매우 큰 문법**: 메모리 사용량이 커질 수 있습니다. 규칙을 모듈화하거나 가중치로 탐색을 제한하세요.

---

## FAQ

**Q. 왜 결과가 매번 같나요?**
A. `--seed` 기본값 때문에 결정적입니다. 다른 결과가 필요하면 시드를 변경하세요.

**Q. 좌재귀 문법은 어떻게 처리하나요?**
A. 좌재귀는 무한 성장을 유발할 수 있으니 우회전개로 변형하거나 안전 한계를 조정하세요.

**Q. JSON 트리 구조를 다른 언어에서 사용하고 싶어요.**
A. `--format json` 출력은 범용적이므로 어떤 언어에서도 파싱이 가능합니다.

**Q. 대안에 가중치를 주는 가장 쉬운 방법은?**
A. 빈도 비례로 `*k` 를 부여하세요. 예: 흔한 표현에 `*5`, 희귀 표현에 `*1`.

---

## 라이선스 (License)

MIT License. 필요 시 조직 정책에 맞게 교체하십시오.

---

# English Section

## Overview

**Poetica** is a single‑file, dependency‑free **weighted grammar expander**. It performs **leftmost derivation** with weighted alternatives and can output either a polished string or a full **JSON derivation tree**. All runs are deterministic via a seed and protected by explicit safety limits. Ideal for prompt/copy generation, test data, templated variations, and teaching CFG concepts.

## Features

* Mini DSL: `LHS -> alt1 | alt2 *3`, trailing `*k` for weights
* Deterministic by `--seed`
* JSON derivation tree via `--format json`
* Single file, stdlib only
* Built‑in fast tests: `python main.py --test`
* Safety limits: `--max-steps`, `--max-tokens`
* Smart punctuation joiner; robust `shlex` tokenization
* Clear domain errors: `GrammarError`, `GenerationLimitError`

## Quickstart

```bash
python main.py --help
python main.py --seed 1 --format text
```

If you see `Undefined nonterminals: Name`, pass a custom grammar via `--grammar` or add a `Name` rule. Use the **Recommended grammar** shown earlier.

## CLI Usage

```bash
python main.py [--seed SEED] [--start SYMBOL]
               [--max-steps N] [--max-tokens N]
               [--format {text,json}] [--verbose]
               [--grammar "<grammar text>"]
               [--test]
```

## Examples

```bash
# Deterministic text generation
python main.py --grammar "$G" --seed 1

# Full derivation tree
python main.py --grammar "$G" --format json

# Verbose expansion trace
python main.py --grammar "$G" --verbose

# Switch start symbol
python main.py --grammar "$G" --start NP --seed 3
```

Sample output:

```
the elegant code flows.
```

## Grammar DSL

* Rules: `LHS -> alt1 | alt2 | ...`
* Nonterminals: `UpperCamelCase`
* Terminals: everything else; quote multi‑word tokens
* Weights: `*k` at the end of an alternative (k ≥ 1)
* Punctuation tokens are attached without leading spaces; `'s` is glued
* All referenced nonterminals must be defined at least once

### Quoting & Escapes

* Wrap tokens containing spaces/special characters with quotes, e.g., `"New York"`.
* Escapes follow Python `shlex` rules.

### Avoiding Left Recursion

Left recursion may cause runaway derivations. Prefer right‑factored or iterative forms. Poetica does not allow empty productions directly; model optionality via an explicit nonterminal.

## JSON Output Schema

See the KR section for a complete example. Nodes have `{label, children}`; terminals are `{terminal: str}`. The `text` field contains the final, neatly joined string.

## Determinism

Weighted choice uses integer arithmetic over a seeded `random.Random`, avoiding floating‑point drift. Identical inputs and parameters always yield identical outputs across platforms. Vary the seed to obtain new variations.

## Performance & Tuning

Time is `O(m * k)`; memory is `O(total_symbols)`. Increase `--max-steps`/`--max-tokens` for longer outputs; add weights to steer expansion; eliminate deep recursion when possible. Typical runs complete well under one second.

## Testing

```bash
python main.py --test
```

Includes doctests and unittests covering success, undefined symbols, and limit detection.

## Troubleshooting

* `Undefined nonterminals`: define all referenced nonterminals.
* Quoting issues on Windows: use PowerShell here‑strings (`@"..."@`).
* Spaces in tokens: quote them.
* Excessive growth: tune limits, refactor grammar, add weights.

## License

MIT.
