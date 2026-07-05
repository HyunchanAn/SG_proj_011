from pydantic import BaseModel, Field, field_validator

class TopographyInput(BaseModel):
    normal_vector_data: list[float]
    curvature_radius: float
    material_stiffness: float
    
    @field_validator("curvature_radius")
    @classmethod
    def check_curvature(cls, v):
        # 3D 곡률 해석을 위한 물리 최소 한계 곡률반경 (0.01mm) 정의
        if abs(v) < 0.01:
            raise ValueError("곡률 반경이 물리적 연산 한계(0.01mm) 미만으로 극단적으로 작아 공정 해석이 불가능합니다.")
        return v
    
class ProcessabilityResult(BaseModel):
    level: int = Field(ge=1, le=5, description="1(가장 유연) ~ 5(매우 단단함)")
    is_fallback: bool = Field(default=False, description="경계값/에러로 인한 기본값 사용 여부")
    reason: str
