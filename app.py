import streamlit as st
from dotenv import load_dotenv
import os
from openai import OpenAI

# Load environment variables
load_dotenv()

client = OpenAI()

st.title("🧠 Mini ChatGPT Clone")
st.write("Talk to your AI assistant")

prompt = st.text_input("You:", "")

if prompt:
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    message = response.choices[0].message.content
    st.write(f"🤖: {message}")
