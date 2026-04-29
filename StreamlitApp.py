### StreamlitApp.py
import streamlit as st
from Protobowl import play_game

# COPY AND PASTE TO RUN THIS FILE: streamlit run /workspaces/cs32-final-project/StreamlitApp.py

# streamlit_app.py
import streamlit as st

from Protobowl import (
    prepare_questions,
    get_visible_question,
    score_answer,
)


st.title("Python Terminal Protobowl: Harvard Edition")

if "questions" not in st.session_state:
    st.session_state.questions = None
    st.session_state.question_index = 0
    st.session_state.word_index = 0
    st.session_state.score = 0
    st.session_state.buzzed = False
    st.session_state.message = ""

demo_mode = st.sidebar.checkbox("Demo mode", value=True)

if st.session_state.questions is None:
    st.write("Welcome to Python Terminal Protobowl: Harvard Edition!")

    if st.button("Start game"):
        st.session_state.questions = prepare_questions("questions.csv", demo_mode)
        st.rerun()

else:
    question = st.session_state.questions[st.session_state.question_index]
    words = question["text"].split()

    st.subheader(f"Score: {st.session_state.score}")
    st.write(get_visible_question(question, st.session_state.word_index))

    if st.button("Read next word"):
        if st.session_state.word_index < len(words):
            st.session_state.word_index += 1
        else:
            st.session_state.buzzed = True
            st.session_state.message = "End of question. Final answer?"
        st.rerun()

    if st.button("Buzz"):
        st.session_state.buzzed = True

    if st.session_state.buzzed:
        answer = st.text_input("Your answer:")

        if st.button("Submit answer"):
            if answer.lower().strip() == "quit":
                st.session_state.questions = None
                st.rerun()

            points, message = score_answer(
                question,
                answer,
                st.session_state.word_index
            )

            st.session_state.message = message

            if points is not None:
                st.session_state.score += points
                st.session_state.question_index += 1
                st.session_state.word_index = 0
                st.session_state.buzzed = False

                if st.session_state.question_index >= len(st.session_state.questions):
                    st.success(f"Game over! Final score: {st.session_state.score}")
                    st.stop()

            else:
                st.session_state.buzzed = False

            st.rerun()

    if st.session_state.message:
        st.info(st.session_state.message)
