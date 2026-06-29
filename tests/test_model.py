# 가공 가혹도 연산 물리 모델의 곡률 반경 계측 수치 계산(가우시안 평활화 포함) 및 경계 조건(음수 곡률반경 등) 예외 판정 무결성을 검증하는 테스트 코드입니다.
from src.schemas import TopographyInput
from src.model import calculate_processability

def test_calculate_processability_normal():
    data = TopographyInput(
        normal_vector_data=[0.1, -0.1, 0.2],
        curvature_radius=5.0,
        material_stiffness=100.0
    )
    result = calculate_processability(data)
    assert result.level in [1, 2, 3, 4, 5]
    assert result.is_fallback is False

def test_calculate_processability_fallback_negative_radius():
    data = TopographyInput(
        normal_vector_data=[0.1],
        curvature_radius=0.0,
        material_stiffness=100.0
    )
    result = calculate_processability(data)
    assert result.is_fallback is True
    assert result.level == 3
    assert "error" in result.reason.lower()

def test_calculate_processability_fallback_empty_vectors():
    data = TopographyInput(
        normal_vector_data=[],
        curvature_radius=2.0,
        material_stiffness=100.0
    )
    result = calculate_processability(data)
    assert result.is_fallback is True
    assert result.level == 3
