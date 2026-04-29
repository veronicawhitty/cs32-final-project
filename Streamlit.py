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
        st.session_state.buzzed = True
        st.session_state.message = "[BUZZ!]"
        st.rerun()

    if st.session_state.message:
        st.info(st.session_state.message)

    if st.session_state.buzzed:
        answer = st.text_input("Your answer:")

        if st.button("Submit"):
            if answer.strip().lower() == "quit":
                st.session_state.started = False
                st.success(f"Exiting game. Final score: {st.session_state.score}")
                st.stop()

            result = pb.check_answer(answer, question["answers"], question["prompts"])
            location_when_buzzed = 0
            for i in range(st.session_state.word_number):
                location_when_buzzed += len(words[i]) + 1

            if result == "correct":
                if location_when_buzzed < question["power_index"]:
                    points = 15
                    st.success(f"POWER! +15 points. The correct answer was "f"{question['display_answers']}.")

                else:
                    points = 10
                    st.success(f"Correct! +10 points. The correct answer was "f"{question['display_answers']}.")

                st.session_state.question_number += 1
                st.session_state.word_number = 0
                st.session_state.score += points
                st.session_state.buzzed = False
                st.session_state.message = ""

            elif result == "prompt":
                st.warning("PROMPT! Please be more specific.")

            else:
                st.error("Incorrect. Continuing to read the question.")
                st.session_state.buzzed = False

            if st.session_state.question_number >= len(st.session_state.questions):
                st.success(f"Game over! Final score: {st.session_state.score}")
                st.stop()

            st.rerun()

        else:
            time.sleep(0.3)

            if st.session_state.word_number < len(words):
                st.session_state.word_number += 1
            else:
                st.session_state.buzzed = True
                st.session_state.message = "End of question. Enter your final answer."

            st.rerun()
