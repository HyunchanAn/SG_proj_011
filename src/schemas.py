from pydantic import BaseModel, Field

class TopographyInput(BaseModel):
    normal_vector_data: list[float]
    curvature_radius: float
    material_stiffness: float
    

    
class ProcessabilityResult(BaseModel):
    level: int = Field(ge=1, le=5, description="1(가장 유연) ~ 5(매우 단단함)")
    is_fallback: bool = Field(default=False, description="경계값/에러로 인한 기본값 사용 여부")
    reason: str
