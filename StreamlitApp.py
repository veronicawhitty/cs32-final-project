### StreamlitApp.py
import streamlit as st
from Protobowl import play_game

# COPY AND PASTE TO RUN THIS FILE: streamlit run /workspaces/cs32-final-project/StreamlitApp.py

st.title("CS32 Final Project: Python Protobowl")
import streamlit as st
import Protobowl as pb


st.title("Python Terminal Protobowl: Harvard Edition")

questions = pb.load_questions("questions.csv")
questions = pb.select_demo_questions(questions)

if "question_number" not in st.session_state:
    st.session_state.question_number = 0
    st.session_state.word_number = 0
    st.session_state.score = 0
    st.session_state.buzzed = False

question = questions[st.session_state.question_number]
words = question["text"].split()

st.write(f"Score: {st.session_state.score}")

st.write(" ".join(words[:st.session_state.word_number]))

if st.button("Read next word"):
    st.session_state.word_number += 1

if st.button("Buzz"):
    st.session_state.buzzed = True

if st.session_state.buzzed:
    user_answer = st.text_input("Your answer:")

    if st.button("Submit"):
        result = pb.check_answer(
            user_answer,
            question["answers"],
            question["prompts"]
        )

        if result == "correct":
            st.session_state.score += 10
            st.write(f"Correct! The answer was {question['display_answers']}.")
            st.session_state.question_number += 1
            st.session_state.word_number = 0
            st.session_state.buzzed = False

        elif result == "prompt":
            st.write("PROMPT! Please be more specific.")

        else:
            st.write("Incorrect. Continuing to read the question.")
            st.session_state.buzzed = False
