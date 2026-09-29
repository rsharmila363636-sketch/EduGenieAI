import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("AQ.Ab8RN6KXC10CfURyKM9cH3aoCCmTOmr5dp7hSO-aLZHmPMQ1dQ"))

def generate_text(prompt):
    try:
        response = client.models.generate_content(
            model="gemini-1.5-flash",
            contents=prompt
        )
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"