from utils import generate_text

def summarize_text(text: str):
    prompt = f"Summarize this text in simple points:\n{text}"
    return generate_text(prompt)