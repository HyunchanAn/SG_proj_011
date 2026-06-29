# 필요 가공성 수준 판별 (SG_proj_011)

![Status](https://img.shields.io/badge/Status-Active-success)
![Python](https://img.shields.io/badge/Python-3.10-blue)
![Framework](https://img.shields.io/badge/Framework-FastAPI_Physics-orange)

## 1. 개요
3D 굴곡률과 재질 강성 데이터를 기반으로 고분자의 물리적 한계 및 유연성 요구 레벨을 정량적으로 판별하는 모듈입니다.

## 2. 시스템 아키텍처
```mermaid
graph TD
    A[Topography Input] --> B[Stress-Strain Physics Model]
    B --> C{Exception / Boundary Check}
    C -->|Normal| D[Compute Score Level 1-5]
    C -->|Error| E[Fallback to Level 3]
    D --> F[Processability Result]
    E --> F
```

## 3. 기술 스택
- Backend: FastAPI, Pydantic
- Logic: Custom Physics Rules

## 4. 참조 문서
- ADR-0001


---
*Updated by System: 2026-06-29 (Resolved 260627 Analysis Report priority issues)*
## 최신 업데이트 내역 (2026-06-29)
- 노이즈에 의한 예외 판정을 막기 위해, 가공 가혹도 판별기 내부에 가우시안 곡률 반경의 평활화(Smoothing) 완충 로직 도입.
