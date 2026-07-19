# 필요 가공성 수준 판별 (SG_proj_011)

![Status](https://img.shields.io/badge/Status-Active-success)
![Python](https://img.shields.io/badge/Python-3.10-blue)
![Hardware](https://img.shields.io/badge/Hardware-Mac_M2_Pro_%7C_Win_RTX5080-lightgrey)
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
*Last Updated: 2026-07-19 (Hybrid Environment & MSA Integration)*
