
import openai
from personas import personas

def generate_feedback(feature_idea: str, persona_name: str, api_key: str) -> str:
    openai.api_key = api_key
    prompt = personas[persona_name]["prompt"] + "\n\nFeature idea: " + feature_idea + "\n\nFeedback:"
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful and realistic mobile gamer persona."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )
    return response['choices'][0]['message']['content']
