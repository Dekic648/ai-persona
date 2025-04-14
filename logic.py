
import os
import google.generativeai as genai

def generate_feedback(feature_idea: str, persona_prompt: str, api_key: str) -> str:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-pro")
    prompt = persona_prompt + f"\n\nFeature idea: {feature_idea}\n\nFeedback:"
    response = model.generate_content(prompt)
    return response.text
