### StreamlitApp.py
# https://cs32pythonprotobowl.streamlit.app/

import random
import time
import streamlit as st
import Protobowl as pb
# COPY AND PASTE TO RUN THIS FILE: streamlit run Streamlit.py

st.set_page_config(
    page_title = "Python Protobowl",
    page_icon = "icon.png")
st.image("logo.png", width=100)
st.title("CS32 Final Project: Python Protobowl")

if "started" not in st.session_state:
    st.session_state.started = False
    st.session_state.ready_to_read = False
    st.session_state.game_over = False
    st.session_state.final_score = 0
    st.session_state.questions = []
    st.session_state.question_number = 0
    st.session_state.word_number = 0
    st.session_state.score = 0
    st.session_state.buzzed = False
    st.session_state.message = ""
    st.session_state.answer_key = 0

intro_area = st.empty()

if not st.session_state.started:
    with intro_area.container():
        demo_mode = st.checkbox("Demo mode", value=True)

        st.write("Welcome to Python Protobowl: Harvard Edition!")
        st.write("**RULES OF THE GAME:**")
        st.write("Press the **Buzz** button during a question.")
        st.write("Correct answers are worth 10 points.")
        st.write("Questions answered correctly within the power region are worth 15 points.")
        st.write("To end the game, buzz in to any question and type 'quit'.")

        if st.button("Start game"):
            questions = pb.load_questions("questions.csv")

            if demo_mode:
                questions = pb.select_demo_questions(questions)
            else:
                random.seed(4)
                questions = random.sample(questions, len(questions))

            st.session_state.started = True
            st.session_state.ready_to_read = False
            st.session_state.game_over = False
            st.session_state.final_score = 0
            st.session_state.questions = questions
            st.session_state.question_number = 0
            st.session_state.word_number = 1
            st.session_state.score = 0
            st.session_state.buzzed = False
            st.session_state.message = ""
            st.session_state.answer_key += 1

            intro_area.empty()
            time.sleep(0.2)
            st.rerun()

    st.stop()

intro_area.empty()

if st.session_state.game_over:
    st.success(f"Game over! Final score: {st.session_state.final_score}")

    if st.button("Start over"):
        st.session_state.started = False
        st.session_state.ready_to_read = False
        st.session_state.game_over = False
        st.session_state.final_score = 0
        st.session_state.questions = []
        st.session_state.question_number = 0
        st.session_state.word_number = 0
        st.session_state.score = 0
        st.session_state.buzzed = False
        st.session_state.message = ""
        st.session_state.answer_key += 1
        st.rerun()

    st.stop()

if not st.session_state.ready_to_read:
    st.session_state.ready_to_read = True
    st.rerun()

if st.session_state.question_number >= len(st.session_state.questions):
    st.session_state.final_score = st.session_state.score
    st.session_state.game_over = True
    st.rerun()

question = st.session_state.questions[st.session_state.question_number]
words = question["text"].split()

st.subheader(f"Score: {st.session_state.score}")

new_words = words[:st.session_state.word_number]
st.write(" ".join(new_words))

if not st.session_state.buzzed:
    if st.button("Buzz"):
        st.session_state.buzzed = True
        st.session_state.message = "BUZZ!"
        st.session_state.answer_key += 1
        st.rerun()

if st.session_state.message:
    st.info(st.session_state.message)

answer_area = st.empty()

if st.session_state.buzzed:
    with answer_area.container():
        answer = st.text_input(
            "Your answer:",
            key=f"answer_{st.session_state.answer_key}"
        )

        submit = st.button(
            "Submit",
            key=f"submit_{st.session_state.answer_key}"
        )

    if submit:
        if answer.strip().lower() == "quit":
            st.session_state.final_score = st.session_state.score
            st.session_state.game_over = True
            st.session_state.ready_to_read = False
            st.session_state.buzzed = False
            st.session_state.answer_key += 1
            answer_area.empty()
            st.rerun()

        result = pb.check_answer(answer, question["answers"], question["prompts"])

        location_when_buzzed = 0
        for i in range(st.session_state.word_number):
            location_when_buzzed += len(words[i]) + 1

        if result == "correct":
            if location_when_buzzed < question["power_index"]:
                points = 15
                st.session_state.message = (
                    f"POWER! +15 points. The correct answer was "
                    f"{question['display_answers']}."
                )
            else:
                points = 10
                st.session_state.message = (
                    f"Correct! +10 points. The correct answer was "
                    f"{question['display_answers']}."
                )

            st.session_state.score += points
            st.session_state.question_number += 1
            st.session_state.word_number = 1
            st.session_state.buzzed = False
            st.session_state.answer_key += 1
            answer_area.empty()
            st.rerun()

        elif result == "prompt":
            user_guess = answer.strip()
            st.session_state.message = (
                f'PROMPT! "{user_guess}" is too vague — please be more specific.'
            )
            st.session_state.answer_key += 1
            answer_area.empty()
            st.rerun()

        else:
            st.session_state.message = "Incorrect. Continuing to read the question."
            st.session_state.buzzed = False
            st.session_state.answer_key += 1
            answer_area.empty()
            st.rerun()

else:
    answer_area.empty()

    if st.session_state.word_number < len(words):
        time.sleep(0.3)
        st.session_state.word_number += 1
        st.rerun()
    else:
        st.session_state.buzzed = True
        st.session_state.message = "End of question. Enter your final answer."
        st.session_state.answer_key += 1
        st.rerun()
