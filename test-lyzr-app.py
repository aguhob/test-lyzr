import streamlit as st
from lyzr-experimental-automata import VoiceBot
st.set_page_config(page_title="VoiceAgent", page_icon="🎤")
openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
vb = VoiceBot(api_key=openai_api_key)
def text_to_notes(text):
    
    notes = vb.text_to_notes(text)
    return notes

def tts(text, model="tts-1-hd", voice="echo"):
    
    response= vb.text_to_speech(text)
    return response

st.selectbox('Select Input type', page_options)
st.button("Submit")

page_options = ['Record Audio', 'Upload Audio','Text']

# Sidebar
selected_page = st.selectbox('Select Input type', page_options)

# Based on the selected page, display the content accordingly
if selected_page == 'Record Audio':
    recordaudio()
elif selected_page == 'Upload Audio':
    uploadaudio()
else:
    Textaudio()
