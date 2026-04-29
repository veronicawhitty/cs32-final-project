# CS32 Final Project: Python Terminal Protobowl

## Project Overview
This project aims to recreate the core experience of the JavaScript-operated Protobowl.com as an interactive trivia game that runs entirely in the Python terminal. In Python Terminal Protobowl, players are shown questions incementally word-by-word, can "buzz in" at any time, and receive immediate feedback on their answers. The goal is to recreate the core gameplay experience of Protobowl in a simplified form that works entirely in the Python terminal, modifying the aspects of the traditional game when needed to accommodate the irregular formatting that Python requires.

## Motivation
Quizbowl was one of my favorite extracurricular activities in high school, and one of the highlights of the "Quizbowl experience" was indubitably competing with friends with Protobowl.com, a popular online practice tool for Quizbowl competitors. I wanted to build a project that captures the fast-paced, competitive feel of Quizbowl while exploring how real-time interaction between the user and Python can be handled in a terminal environment (via real-time buzzing.) This project also allows me to work on input handling, timing, and game state management in Python, all diciplines I am intrigued by.

## Project Functionality and Intended Features
This project implements a terminal-based Quizbowl-style trivia game inspired by Protobowl.com. The program reads questions from a CSV database and presents them to the user word-by-word, simulating the incremental reveal used in real Quizbowl matches.

At any point while the question is being read, the user can "buzz in" by pressing Ctrl+C. The program then pauses the question and prompts the user for an answer.

The game includes the following key features:
- **Incremental question reading**: Questions are displayed one word at a time to simulate live gameplay.
- **Buzzing system**: Users can interrupt the question at any time using a keyboard interrupt.
- **Power scoring**: If the user answers early enough (before a marked point in the question), they earn 15 points instead of 10.
- **Answer standardization**: User input is normalized to allow flexible matching (ignoring capitalization and punctuation).
- **Multiple acceptable answers**: Questions can have several valid answers stored in the CSV file. Common mispellings are accounted for on particularly difficult questions.
- **Prompting system**: If a user gives a partially correct answer, the program asks them to be more specific instead of marking it wrong.
- **Demo mode**: A fixed set of questions can be selected for consistent testing and demonstration.

The program keeps track of the user's score across multiple questions and runs until the user chooses to quit.

## Tech Stack
- Python (CS32/CS50 IDE)
- Terminal interface

## Installation
- Make sure you have Python 3 and questions.csv installed on your device
- Place `questions.csv` in the same directory as `Protobowl.py` in order to access questions during gameplay

## How to Use
The game is fully playable in the terminal. Core mechanics (buzzing, scoring, answer checking) are implemented and tested.

- The question will begin displaying gradually in the terminal
- Press 'Ctrl-C' (or follow the beginning instructions message) to buzz in
- Upon buzzing, type in your answer and click "return"
- The program will tell you if you are correct and update your score
- If you are incorrect, buzz as many times as needed until you achieve a correct answer OR until the question is finished being read
- Score updates as the game is played, with points awarded in 15s or 10s based on answer speed

## External Contributors and Use of AI Tools
I used ChatGPT as a supplementary tool during development of both protobowl.py and streamlit.py.

In protobowl.py, I used it to:
- Help debug and refine parts of my code (specifically, how to create a 'demo mode' for my code explanations videos)
- Identify a pesky indentation problem with my for loops in Step 4
- Think through how to structure the multiple-buzz feature so that code doesn't crash when a user buzzes twice

In streamlit.py, I used it to:
- Resolve persistent “floating” UI elements (such as buttons and input fields) caused by Streamlit’s rerun behavior
- Ensure that the intro screen (rules and start button) properly disappears once gameplay begins
- Implement a clean quit flow that displays the user’s final score and allows them to restart the game without refreshing the page

I also used a tutorial from Geeksforgeeks.org to better understand the flush() method.

All computational logic and core structural code is done by me.


## Credits
Inspired by Protobowl and other quizbowl-style trivia games. An extra-special shoutout to Kevin Kwok and Ben Vest, the original programmers behind Protobowl.com, as well as Geoffrey Wu, the creator of the more modern and user-friendly QBReader interface, which has effectively replaced Protobowl in utility and thus serves as an additional reference point for this project.
