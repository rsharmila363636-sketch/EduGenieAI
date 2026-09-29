from utils import generate_text

def explain_concept(topic: str):
    prompt = f"Explain this topic in simple terms for a beginner:\n{topic}"
    return generate_text(prompt)