import json
from utils import generate_text

def clean_json(text):
    return text.replace("```json", "").replace("```", "").strip()

def generate_quiz(text: str):
    prompt = f"""
    Generate 3 MCQs from the following text.
    Return JSON format:
    [
      {{
        "question": "...",
        "options": ["A","B","C","D"],
        "answer": "correct option"
      }}
    ]
    TEXT:
    {text}
    """

    response = generate_text(prompt)
    
    try:
        clean = clean_json(response)
        return json.loads(clean)
    except:
        return {"error": response}