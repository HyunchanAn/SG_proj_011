from .schemas import TopographyInput, ProcessabilityResult

def calculate_processability(input_data: TopographyInput) -> ProcessabilityResult:
    """
    3D stress-strain simplified physics model 기반 가공성 판별
    정상 벡터 데이터, 곡률 반경, 재질 강도를 기반으로 스트레스/변형률을 계산.
    단일 지점 곡률 튐 노이즈 방지를 위해 주변 법선 벡터 분포의 평균 편차를 평활화 가중치로 적용합니다.
    """
    try:
        if input_data.curvature_radius == 0:
            raise ValueError("Curvature radius cannot be 0.")
        if input_data.material_stiffness < 0:
            raise ValueError("Material stiffness cannot be negative.")
        if not input_data.normal_vector_data:
            raise ValueError("Normal vector data cannot be empty.")
        
        # Average deviation or magnitude of normal vectors (representing local surface variations)
        avg_normal = sum(abs(v) for v in input_data.normal_vector_data) / len(input_data.normal_vector_data)
        
        # Noise mitigation: Smooth curvature using local normal variation to prevent singular peak exceptions
        # If surrounding area is generally flat (low avg_normal), dampen extreme curvature spikes
        damping_factor = 1.0 / (1.0 + avg_normal) if avg_normal > 0 else 1.0
        smoothed_radius = abs(input_data.curvature_radius) * (1.0 + damping_factor * 0.2)
        
        # Strain is inversely proportional to the smoothed curvature radius
        strain = 1.0 / smoothed_radius
        
        # Stress = Stiffness * Strain * Surface Factor
        stress = input_data.material_stiffness * strain * (1.0 + avg_normal)
        
        if stress < 10.0:
            level = 1
            reason = "Stress is very low; highly flexible surface."
        elif stress < 50.0:
            level = 2
            reason = "Stress is low; flexible surface."
        elif stress < 100.0:
            level = 3
            reason = "Moderate stress; standard processability."
        elif stress < 500.0:
            level = 4
            reason = "High stress; hard material and complex topography."
        else:
            level = 5
            reason = "Very high stress; extremely hard material."
            
        return ProcessabilityResult(level=level, is_fallback=False, reason=reason)
        
    except Exception as e:
        # Dynamic fallback mechanism based on material stiffness
        fallback_level = 3
        if input_data.material_stiffness > 200:
            fallback_level = 4
        elif input_data.material_stiffness < 50:
            fallback_level = 2
            
        return ProcessabilityResult(
            level=fallback_level, 
            is_fallback=True, 
            reason=f"Dynamic fallback score applied due to processability calculation error: {str(e)}"
        )

