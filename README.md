# CS32 Final Project: Python Terminal Protobowl

## Project Overview
This project aims to recreate the core experience of the JavaScript-operated Protobowl.com as an interactive trivia game that runs entirely in the Python terminal. In Python Terminal Protobowl, players are shown questions incementally word-by-word, can "buzz in" at any time, and receive immediate feedback on their answers. The goal is to recreate the core gameplay experience of Protobowl in a simplified form that works entirely in the Python terminal, modifying the aspects of the traditional game when needed to accommodate the irregular formatting that Python requires.

## Motivation
Quizbowl was one of my favorite extracurricular activities in high school, and one of the highlights of the "Quizbowl experience" was indubitably competing with friends with Protobowl.com, a popular online practice tool for Quizbowl competitors. I wanted to build a project that captures the fast-paced, competitive feel of Quizbowl while exploring how real-time interaction between the user and Python can be handled in a terminal environment (via real-time buzzing.) This project also allows me to work on input handling, timing, and game state management in Python, all diciplines I am intrigued by.

## Intended Features
- CSV file reading for question database
- Incremental question display (word-by-word printing of questions)
- Answer input and checking
- Score tracking aross questions
- Continuous game loop for repeated play
- "Quit" option for when users have completed playing

## Tech Stack
- Python (CS32/CS50 IDE)
- Terminal interface

## Installation
- Make sure you have Python 3 installed
- Place `questions.csv` in the same directory as `Protobowl.py`
- Use 'Ctrl-C' to buzz in when playing the game

## How to Use
The game is fully playable in the terminal. Core mechanics (buzzing, scoring, answer checking) are implemented and tested.

- The question will begin displaying gradually in the terminal
- Press 'Ctrl-C' (or follow the beginning instructions message) to buzz in
- Upon buzzing, type in your answer and click "return"
- The program will tell you if you are correct and update your score
- If you are incorrect, buzz as many times as needed until you achieve a correct answer OR until the question is finished being read
- Score updates as the game is played, with points awarded in 15s or 10s based on answer speed

## External Contributors and Use of AI Tools
I used ChatGPT as a supplementary tool during development. Specifically, I used it to:
- Help debug and refine parts of my code (specifically, how to create a 'demo mode' for my code explanations videos)
- Get suggestions for organizing my code into functions and improving readability
- Think through how to structure the multiple-buzz feature so that code doesn't crash when a user buzzes twice


## Credits
Inspired by Protobowl and other quizbowl-style trivia games. An extra-special shoutout to Kevin Kwok and Ben Vest, the original programmers behind Protobowl.com, as well as Geoffrey Wu, the creator of the more modern and user-friendly QBReader interface, which has effectively replaced Protobowl in utility and thus serves as an additional reference point for this project.
