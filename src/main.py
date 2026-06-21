from fastapi import FastAPI
from .schemas import TopographyInput, ProcessabilityResult
from .model import calculate_processability

app = FastAPI(title="SG_proj_011: Processability Level Determination")

@app.post("/analyze", response_model=ProcessabilityResult)
def analyze_processability(input_data: TopographyInput) -> ProcessabilityResult:
    """
    Evaluate the processability level based on 3D stress-strain simplified physics model.
    """
    return calculate_processability(input_data)
