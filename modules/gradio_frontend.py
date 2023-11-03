import gradio as gr

from configs.model_config import AVAILABLE_MODELS, DEFAULT_MODEL
from utils import CustomFlagger
from .llm_conti import ask_model

demo = gr.Interface(fn=ask_model,
                    inputs=["text", gr.Dropdown(AVAILABLE_MODELS, label="model", value=DEFAULT_MODEL)],
                    outputs=[gr.Textbox(label="Answer"), gr.Number(label="Elapsed Time")],
                    title="ContiGPT",
                    flagging_options=['Incorrect', 'Vague'],
                    flagging_callback=CustomFlagger())
