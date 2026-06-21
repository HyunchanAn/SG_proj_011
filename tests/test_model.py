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
        curvature_radius=-1.0,
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
