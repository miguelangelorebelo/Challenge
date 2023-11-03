from loguru import logger
from transformers import AutoTokenizer, AutoModelForCausalLM

from configs.model_config import DEFAULT_MODEL
from models.dolly_3b.instruct_pipeline import InstructionTextGenerationPipeline


class LoadModel:
    """
    Singleton pattern for single model load instead of loading at each prompt.
    """
    __pipeline = None
    __name = DEFAULT_MODEL

    def __init__(self, model=DEFAULT_MODEL):
        if LoadModel.__pipeline is None or LoadModel.__name != model:
            logger.info(f'Loading model: {model}')
            LoadModel.__name = model
            tokenizer = AutoTokenizer.from_pretrained(model, padding_side="left")
            model = AutoModelForCausalLM.from_pretrained(model)
            LoadModel.__pipeline = InstructionTextGenerationPipeline(
                model=model,
                tokenizer=tokenizer,
                device='cpu'
            )

    @staticmethod
    def get_model():
        if LoadModel.__pipeline is None:
            print('load model')
            LoadModel(LoadModel.__name)
        return LoadModel.__pipeline
