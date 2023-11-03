import os

import wget
from loguru import logger
from transformers import AutoTokenizer, AutoModelForCausalLM


def download_model(model_path, model_name):
    """Download a Hugging Face model and tokenizer to the specified directory"""
    # Check if the directory already exists
    if not os.path.exists(model_path):
        # Create the directory
        os.makedirs(model_path)

    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)

    # Save the model and tokenizer to the specified directory
    model.save_pretrained(model_path)
    tokenizer.save_pretrained(model_path)
    wget.download("https://huggingface.co/" + model_name + "/raw/main/instruct_pipeline.py", out=model_path)
    print('got pipeline script')


if __name__ == '__main__':
    # Download models
    download_model('models/dolly_3b/', "databricks/dolly-v2-3b")
    logger.info("Models downloaded")
    # download additional models...
