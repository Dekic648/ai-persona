
import streamlit as st
import json
import os
from logic import generate_feedback

st.set_page_config(page_title="🎮 AI Gamer Persona Lab", layout="centered")

@st.cache_data
def load_personas():
    with open("ai_gamer_personas.json", "r") as f:
        return json.load(f)

personas = load_personas()
persona_names = [p["name"] for p in personas]

st.title("🧠 AI Gamer Persona Feedback")
st.markdown("Describe a mobile game feature and select which gamer personas you'd like feedback from.")

feature_idea = st.text_area("💡 Describe your game feature idea", height=150)

selected_names = st.multiselect(
    "🎭 Choose gamer personas:",
    options=persona_names,
    format_func=lambda name: next(p["name"] + " – " + p["type"] for p in personas if p["name"] == name)
)

if st.button("💬 Generate Feedback") and feature_idea and selected_names:
    api_key = os.getenv("OPENAI_API_KEY")
    
    if not api_key:
        st.error("❌ OPENAI_API_KEY not found. Please set it in Streamlit Cloud > Settings > Secrets.")
    else:
        for name in selected_names:
            persona = next(p for p in personas if p["name"] == name)
            st.subheader(f"{persona['name']} – *{persona['type']}*")
            st.markdown(f"🧠 **Motivations**: {', '.join(persona['motivations'])}")
            st.markdown(f"🎮 **Favorite Games**: {', '.join(persona['favorite_games'])}")
            st.markdown(f'💬 *"{persona["quote"]}"*')
            with st.spinner(f"Thinking like {name}..."):
                feedback = generate_feedback(feature_idea, persona["prompt"], api_key)
                st.markdown(f"🗣️ {feedback}")
