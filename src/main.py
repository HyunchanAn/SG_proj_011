from fastapi import FastAPI, HTTPException
from src.schemas import TopographyInput, ProcessabilityResult
from src.model import calculate_processability

app = FastAPI(title="SG_proj_011 - Processability Level Determination")

@app.post("/calculate_processability", response_model=ProcessabilityResult)
def get_processability(req: TopographyInput):
    result = calculate_processability(req)
    return result

