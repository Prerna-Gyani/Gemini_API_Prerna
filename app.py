import streamlit as st
import requests

st.title("Gemini API Demo (Very Basic)")

api_key = st.text_input("Enter your Gemini API Key:", type="password")
prompt = st.text_area("Ask something:")

if st.button("Generate"):
    if not api_key:
        st.error("Please enter your API key!")
    else:
        url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent"
        
        headers = {
            "Content-Type": "application/json"
        }

        body = {
            "contents": [{"parts": [{"text": prompt}]}]
        }

        params = {"key": api_key}

        response = requests.post(url, headers=headers, json=body, params=params)

        if response.status_code == 200:
            result = response.json()
            text = result["candidates"][0]["content"]["parts"][0]["text"]
            st.success(text)
        else:
            st.error(f"Error: {response.text}")
