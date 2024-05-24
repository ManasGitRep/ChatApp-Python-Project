import streamlit as st
from bot import get_response

st.title('My Chatbot')

# Create a text input for the user's message
prompt = st.text_input("You:", "")

# When the user submits a message, send it to the chatbot and display the response
if st.button("Send"):
    response = get_response(prompt)
    st.write(f"Chatbot: {response}")
