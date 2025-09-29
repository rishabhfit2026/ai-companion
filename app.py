# app.py (No Memory Version - Final with Credit)

import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os
from personality import SYSTEM_PROMPT # Import the updated personality prompt

# --- SETUP AND INITIALIZATION ---
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


# --- HELPER FUNCTION ---

def get_gemini_response(user_input, chat_history):
    """Gets a conversational response from the Gemini model."""
    history_str = "\n".join([f"{msg['role']}: {msg['content']}" for msg in chat_history])
    
    # Build the final prompt with the chat history
    prompt = SYSTEM_PROMPT.replace("{{chat_history}}", history_str)
    prompt += f"\nfriend: {user_input}"

    try:
        # Use the corrected model name from the list you generated
        model = genai.GenerativeModel('models/gemini-pro-latest') 
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        st.error(f"Error getting response from Gemini: {e}")
        return "I'm not sure how to respond to that right now, sorry!"

# --- STREAMLIT UI ---
st.set_page_config(page_title="Chat with Evelyn", page_icon="✨")
st.title("Chat with Evelyn ✨")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "Evelyn", "content": "Hey! So glad to see you. How has your day been? 😊"}]

# Display chat messages from history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if user_input := st.chat_input("What's on your mind?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "friend", "content": user_input})
    # Display user message
    with st.chat_message("friend"):
        st.markdown(user_input)

    # Display AI response
    with st.chat_message("Evelyn"), st.spinner("Evelyn is typing..."):
        # Get AI response (no memory functions are called)
        ai_response = get_gemini_response(user_input, st.session_state.messages)
        st.markdown(ai_response)
        
    # Add AI response to chat history
    st.session_state.messages.append({"role": "Evelyn", "content": ai_response})


# --- FOOTER ---
# This code adds the footer at the bottom of the page.
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: grey;'>© 2025 Evelyn, created by Rishabh Singh Rajput. All rights reserved.</div>",
    unsafe_allow_html=True
)