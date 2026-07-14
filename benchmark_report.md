# Benchmark & E2E Test Report

- **Repository**: SG_proj_011
- **Date**: 2026-07-14 22:44:34

## 1. E2E Testing Summary
✅ **Status**: PASSED

### Test Logs (Snippet)
```text
============================= test session starts ==============================
platform darwin -- Python 3.13.9, pytest-9.0.3, pluggy-1.5.0
rootdir: /Users/hyunchanan/Documents/GitHub/SG_proj_011
configfile: pyproject.toml
testpaths: tests
plugins: anyio-4.12.1, cov-7.1.0, hypothesis-6.155.7, hydra-core-1.3.2, respx-0.23.1
collected 5 items

tests/test_main.py ..                                                    [ 40%]
tests/test_model.py ...                                                  [100%]

================================ tests coverage ================================
_______________ coverage: platform darwin, python 3.13.9-final-0 _______________

Name              Stmts   Miss  Cover   Missing
-----------------------------------------------
src/__init__.py       0      0   100%
src/main.py          10      0   100%
src/model.py         40     13    68%   15, 34-35, 39-47, 56, 58
src/schemas.py        9      0   100%
-----------------------------------------------
TOTAL                59     13    78%
============================== 5 passed in 4.73s ===============================

```

## 2. Models Detected
- No pre-trained weights or models detected in this repository.
