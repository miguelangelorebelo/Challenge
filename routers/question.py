from fastapi import APIRouter, HTTPException
from loguru import logger

from modules.llm_conti import ask_model
from schemas import Request, Result

router = APIRouter()


@router.post("/respond", response_model=Result, status_code=201)
async def question_api(request: Request,
                       model: str = "models/dolly_3b"):
    """
    Get response from the selected pretrained llm
    """

    if len(request.question) == 0:
        logger.info(f"Request length provided: {len(request.question)}")
        raise HTTPException(status_code=406, detail="Not Acceptable: Prompt has no length.")

    response, time = ask_model(prompt=request.question, model=model)
    logger.debug(f'Asking through API: {request.question}')
    return Result(
        response=response,
        elapsed_seconds=time
    )
