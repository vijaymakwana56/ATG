# model_loader.py
from transformers import pipeline

def load_chat_model(model_name="distilgpt2"):
    """
    Load a small text generation model for local inference.
    """
    generator = pipeline("text-generation", model=model_name)
    return generator