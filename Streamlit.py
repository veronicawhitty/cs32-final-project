### StreamlitApp.py
import random
import time
import streamlit as st
import Protobowl as pb
# COPY AND PASTE TO RUN THIS FILE: streamlit run Streamlit.py

st.title("CS32 Final Project: Python Protobowl")

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
    st.write("**RULES OF THE GAME:**")
    st.write("Press Ctrl+C to buzz during a question.")
    st.write("Correct answers are worth 10 points. Questions answered correctly within the first sentences of the passage are worth 15 points.")
    st.write("In order to end the game, buzz in to any question and type 'quit'.")

if st.button("Start game"):
    questions = pb.load_questions("questions.csv")

    if demo_mode:
        questions = pb.select_demo_questions(questions)
    else:
        random.seed(4)
        questions = random.sample(questions, len(questions)) # I AM CONFUSED ABOUT THIS LINE

    st.session_state.started = True
    st.session_state.questions = questions
    st.session_state.question_number = 0
    st.session_state.word_number = 0
    st.session_state.score = 0
    st.session_state.buzzed = False
    st.session_state.message = ""
    st.rerun()

else:
    question = st.session_state.questions[st.session_state.question_number]
    words = question["text"].split()
    st.subheader(f"Score: {st.session_state.score}")

    new_words = words[:st.session_state.word_number]
    st.write(" ".join(new_words))

    if st.button("Buzz"):
