from .schemas import TopographyInput, ProcessabilityResult

def calculate_processability(input_data: TopographyInput) -> ProcessabilityResult:
    """
    3D stress-strain simplified physics model 기반 가공성 판별
    정상 벡터 데이터, 곡률 반경, 재질 강도를 기반으로 스트레스/변형률을 계산.
    """
    try:
        if input_data.curvature_radius == 0:
            raise ValueError("Curvature radius cannot be 0.")
        if input_data.material_stiffness < 0:
            raise ValueError("Material stiffness cannot be negative.")
        if not input_data.normal_vector_data:
            raise ValueError("Normal vector data cannot be empty.")
        
        # Simplified Physics Calculation
        # Strain is inversely proportional to the absolute curvature radius.
        strain = 1.0 / abs(input_data.curvature_radius)
        
        # Average deviation or magnitude of normal vectors could represent local surface variation.
        avg_normal = sum(abs(v) for v in input_data.normal_vector_data) / len(input_data.normal_vector_data)
        
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
        # Fallback mechanism for boundary/error values
        return ProcessabilityResult(
            level=3, 
            is_fallback=True, 
            reason=f"Fallback score applied due to error: {str(e)}"
        )
