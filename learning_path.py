from utils import generate_text

def get_learning_path(topic: str):
    prompt = f"""
    Create a structured learning path for {topic}.
    Include:
    - Beginner to advanced topics
    - Timeline
    - Resources
    """
    return generate_text(prompt)