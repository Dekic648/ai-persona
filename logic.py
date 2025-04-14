
import os
from openai import OpenAI

def generate_feedback(feature_idea: str, persona_prompt: str, api_key: str) -> str:
    client = OpenAI(api_key=api_key)

    full_prompt = persona_prompt + f"\n\nFeature idea: {feature_idea}\n\nFeedback:"

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a realistic mobile gamer persona."},
            {"role": "user", "content": full_prompt}
        ],
        temperature=0.7
    )

    return response.choices[0].message.content
