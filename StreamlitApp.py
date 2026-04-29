### StreamlitApp.py
import random
import time
import streamlit as st
import Protobowl as pb
# COPY AND PASTE TO RUN THIS FILE: streamlit run /workspaces/cs32-final-project/StreamlitApp.py

st.title("CS32 Final Project: Python Protobowl)

if "started" not in st.session_state:
    st.session_state.started = False
    st.session_state.questions = []
    st.session_state.question_number = 0
    st.session_state.word_number = 0
    st.session_state.score = 0
    st.session_state.buzzed = False
    st.session_state.message = ""

demo_mode = st.checkbox("Demo mode", value = True)

if not st.session_state.started:
    st.write("Welcome to Python Protobowl: Harvard Edition!")
    st.write("RULES OF THE GAME:")
    st.write("Press Ctrl+C to buzz during a question.")
    st.write("Correct answers are worth 10 points. Questions answered correctly within the first sentences of the passage are worth 15 points.")
    st.write("In order to end the game, buzz in to any question and type 'quit'.")
