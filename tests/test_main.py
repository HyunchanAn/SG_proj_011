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
        "curvature_radius": -1.0,
        "material_stiffness": 100.0
    }
    res = client.post("/calculate_processability", json=payload)
    assert res.status_code == 200
    data = res.json()
    assert data["is_fallback"] is True
    assert data["level"] == 3

