
import streamlit as st
from personas import personas
from logic import generate_feedback

st.set_page_config(page_title="Mobile Gamer Feedback Lab", layout="centered")

st.title("🎮 Mobile Gamer Persona Feedback Lab")
st.markdown("Describe a mobile game feature and select which gamer personas you'd like feedback from.")

api_key = st.text_input("Enter your OpenAI API Key", type="password")

feature_idea = st.text_area("🧠 Describe your game feature idea here", height=150)

selected_personas = st.multiselect(
    "🎭 Choose personas to simulate:",
    options=list(personas.keys()),
    format_func=lambda name: f"{name} - {personas[name]['description']}"
)

if st.button("💬 Generate Feedback") and feature_idea and api_key:
    for name in selected_personas:
        st.subheader(name)
        with st.spinner(f"Thinking like {name}..."):
            feedback = generate_feedback(feature_idea, name, api_key)
            st.markdown(f"🗣️ {feedback}")
