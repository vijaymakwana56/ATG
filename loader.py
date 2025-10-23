# model_loader.py
from transformers import pipeline

def load_chat_model(model_name="google/flan-t5-base"):
    print("Device set to use CPU")
    generator = pipeline("text2text-generation", model=model_name)
    return generator