from utils import generate_text

def get_answer(question: str):
    prompt = f"Answer this question clearly:\n{question}"
    return generate_text(prompt)