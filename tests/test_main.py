# 가공 공정 가혹도 판별 모듈의 FastAPI 엔드포인트(/calculate_processability) 및 입력 데이터 예외 발생 시의 동적 폴백 처리 유효성을 검증하는 API 테스트 코드입니다.
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_calculate_processability_valid():
    payload = {
        "normal_vector_data": [0.1, -0.1, 0.2],
        "curvature_radius": 5.0,
        "material_stiffness": 100.0
    }
    res = client.post("/calculate_processability", json=payload)
    assert res.status_code == 200
    data = res.json()
    assert "level" in data
    assert data["is_fallback"] is False

def test_calculate_processability_invalid():
    payload = {
        "normal_vector_data": [0.1],
        "curvature_radius": 0.0,
        "material_stiffness": 100.0
    }
    res = client.post("/calculate_processability", json=payload)
    assert res.status_code == 200
    data = res.json()
    assert data["is_fallback"] is True
    assert data["level"] == 3

