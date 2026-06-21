# SG_proj_011

필요 가공성 수준 판별 (Processability Level Determination) 모듈입니다.

## 아키텍처

- `src/schemas.py`: Pydantic 기반의 데이터 입출력 규격 (TopographyInput -> ProcessabilityResult).
- `src/model.py`: 3D stress-strain simplified physics 모델을 활용한 가공성 점수 계산 및 Fallback 처리.
- `src/main.py`: FastAPI 기반의 API 엔드포인트.
