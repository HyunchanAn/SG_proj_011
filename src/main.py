from fastapi import FastAPI
from loguru import logger

from src.model import calculate_processability
from src.schemas import ProcessabilityResult, TopographyInput

app = FastAPI(title="SG_proj_011 - Processability Level Determination")

@app.post("/calculate_processability", response_model=ProcessabilityResult)
def get_processability(req: TopographyInput):
    logger.info("011 API: Received processability calculation request.")
    result = calculate_processability(req)
    return result

