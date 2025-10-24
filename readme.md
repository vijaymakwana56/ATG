# Local Command-Line Chatbot using Hugging Face (Flan-T5-Base)

A simple, fully local chatbot built in Python using the **Hugging Face Transformers** library.  
It uses **Google’s Flan-T5-Base** model — a small, instruction-tuned language model that can understand and answer natural language prompts directly from your terminal.

---

## Features

- Runs **completely offline** (no API keys or internet connection needed after the first model download)  
- Built with **modular Python structure**:
  - `model_loader.py` → handles model loading  
  - `chat_memory.py` → stores short conversation history  
  - `interface.py` → command-line interface for chatting  
- Uses a **sliding-window memory** (last few turns) for contextual replies  
- Gracefully exits with `/exit`  
- Optimized for CPU inference  

---

## Project Structure

ATG/
│
├── model_loader.py # Loads the Flan-T5-Base model and tokenizer
├── chat_memory.py # Implements short-term chat memory
├── interface.py # Command-line chatbot loop
└── README.md

## Install dependencies:

pip install transformers torch

Note: The first run will download the Flan-T5-Base model (~900 MB).
It will be cached locally for future use.

## How It Works
- The chatbot loads Flan-T5-Base via the text2text-generation pipeline.
- It remembers the last few turns of conversation using a simple sliding-window buffer.
- For each new user input, it sends a concise instruction prompt to the model.

## Usage
Run the chatbot from your terminal:

python interface.py

