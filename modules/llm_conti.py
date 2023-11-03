import time

from loguru import logger

from configs.model_config import MAX_TOKENS
from utils.model_loader import LoadModel


def ask_model(prompt: str, model: str, max_tokens=MAX_TOKENS):
    logger.debug("ask_model triggered")

    # Keep track of time
    start_time = time.time()

    # Load Model
    logger.debug("Loading model")
    loader = LoadModel(model)
    pipeline = loader.get_model()

    # Run prompt
    logger.debug(f"Prompt: {prompt}")
    result = pipeline(
        prompt,
        max_new_tokens=max_tokens
    )

    # Extract result
    answer = result[0]["generated_text"]
    logger.debug(f"Result: {answer}")

    elapsed_time = time.time() - start_time

    return answer, elapsed_time
