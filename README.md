# CS32 Final Project: Python Protobowl

## Project Overview
This project recreates the core experience of the JavaScript-operated Protobowl.com as an interactive Quizbowl-style trivia game written in Python. In Python Protobowl, players are shown questions incrementally, word by word, can "buzz in" before the question is finished, and receive immediate feedback on their answers.

The project includes two playable versions:

1. A terminal-based version in `Protobowl.py`, which runs entirely in the terminal without any need for additional downloads
2. A browser-based Streamlit version in `App.py`, also accessible at the following link: https://cs32pythonprotobowl.streamlit.app/

Both versions use the same question database, answer-checking logic, prompting system, and power-scoring system.

## Motivation
Quizbowl was one of my favorite extracurricular activities in high school, and one of the highlights of the "Quizbowl experience" was indubitably competing with friends with Protobowl.com, a popular online practice tool for Quizbowl competitors. I wanted to build a project that captures the fast-paced, competitive feel of Quizbowl while exploring how real-time interaction between the user and Python can be handled in a terminal environment (via real-time buzzing.) This project also allows me to work on input handling, timing, and game state management in Python, all disciplines I am intrigued by.

As the project developed, I also added a browser-based Streamlit version in order to make the game more accessible and easier to play outside the terminal. This project allowed me to work on input handling, timing, game state management, answer checking, and user interface design in Python. Through it, I learned how to use the Streamlit package, which was quite rewarding.

## Project Functionality and Intended Features
This project implements a Quizbowl-style trivia game inspired by Protobowl.com. The program reads questions from a CSV database and presents them to the user word by word, simulating the incremental reveal used in real Quizbowl matches.

In the terminal version, the user can buzz in by pressing Ctrl+C while the question is being read. The program then pauses the question and prompts the user for an answer.

In the Streamlit version, the user can buzz by clicking a button in the browser. Because Streamlit reruns the script after user interactions, this version uses `st.session_state` to keep track of the current question, score, buzz status, and revealed words.

The game includes the following key features:
- **Incremental question reading**: Questions are displayed one word at a time to simulate live gameplay.
- **Buzzing system**: Users can interrupt the question at any time using a keyboard interrupt.
- **Power scoring**: If the user answers early enough (before a marked point in the question), they earn 15 points instead of 10.
- **Answer standardization**: User input is normalized to allow flexible matching (ignoring capitalization and punctuation).
- **Multiple acceptable answers**: Questions can have several valid answers stored in the CSV file. Common misspellings are accounted for on particularly difficult questions.
- **Prompting system**: If a user gives a partially correct answer, the program asks them to be more specific instead of marking it wrong.
- **Demo mode**: A fixed set of questions can be selected for consistent testing and demonstration.

The program keeps track of the user's score across multiple questions and runs until the user chooses to quit.

## Tech Stack
- Python 3 (CS32/CS50 IDE)
- CSV file input
- Streamlit package
- Terminal interface
- Browser-based interface

## Files
- `Protobowl.py`
  Contains the core game logic, including loading questions, standardizing answers, checking answers, scoring, demo mode, and the terminal version of the game.
- `App.py`
  Contains the Streamlit interface for the browser-based version of the game.
- `questions.csv`
  Stores the question database used by the game.
- `icon.png`
  Used as the browser tab icon for the Streamlit app.

## How to Use
The game is fully playable in the terminal. Core mechanics (buzzing, scoring, answer checking) are implemented and tested.

- The question will begin displaying gradually in the terminal
- Press 'Ctrl-C' (or follow the beginning instructions message) to buzz in
- Upon buzzing, type in your answer and click "return"
- The program will tell you if you are correct and update your score
- If you are incorrect, buzz as many times as needed until you achieve a correct answer OR until the question is finished being read
- Score updates as the game is played, with points awarded in 15s or 10s based on answer speed

## External Contributors and Use of AI Tools
I used ChatGPT as a supplementary tool during development of both `Protobowl.py` and `App.py`.

Specific areas of `Protobowl.py` where ChatGPT assisted include:
- Helping debug and refine parts of my code (specifically, how to create a 'demo mode' for my code explanations videos)
- Identifying a pesky indentation problem with my for loops in Step 4
- Thinking through how to structure the multiple-buzz feature so that code doesn't crash when a user buzzes twice

In `App.py`, I used ChatGPT more substantially because Streamlit’s rerun model was new to me. ChatGPT helped me understand how to use `st.session_state` to preserve game progress across reruns and how to use `st.empty()` containers to clear or replace interface elements. It also helped me resolve issues where buttons and input fields continued appearing after they were no longer relevant.

Specific areas of `App.py` where ChatGPT assisted include:
- Resolving persistent “floating” UI elements, such as buttons and input fields, caused by Streamlit’s rerun behavior
- Ensuring that the intro screen, including the rules and start button, properly disappears once gameplay begins
- Implementing a clean quit flow that displays the user’s final score and allows them to restart the game without refreshing the page
- Setting up the final score screen, restart button, and page configuration

I also used a tutorial from Geeksforgeeks.org to better understand the flush() method.

All computational logic and core structural code is done by me.

## Credits
Inspired by Protobowl and other quizbowl-style trivia games. An extra-special shoutout to Kevin Kwok and Ben Vest, the original programmers behind Protobowl.com, as well as Geoffrey Wu, the creator of the more modern and user-friendly QBReader interface, which has effectively replaced Protobowl in utility and thus serves as an additional reference point for this project.

## Installation
To run the project locally, make sure you have Python 3 installed.

Clone or download the repository, then make sure the following files are in the same folder:

- `Protobowl.py`
- `App.py`
- `questions.csv` (in order to access questions during gameplay)
- `icon.png`

If you want to run the Streamlit version locally, install Streamlit:

```bash
pip install streamlit
