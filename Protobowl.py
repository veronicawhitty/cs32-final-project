### Protobowl.py

# IMPORT SOME LIBRARIES
import csv # To read our question database
import random # For question selection
import time # For incremental reading and "waiting" functionality

# STEP 1: LOAD QUESTIONS IN FROM THE CSV DATABASE
# Load in our questions from the csv file "questions.csv"
def load_questions(file):
    questions = []
    with open(file, encoding = 'utf-8') as file:
        # Operates like a regular reader, but maps the information in each row to
        # a dictionary whose keys are given by the optional fieldnames parameter
        reader = csv.DictReader(file)

        for row in reader:
            answers = []
            # Split answer options by semicolon (what I use in the CSV file to differentiate
            # between answers in circumstance where they are MULTIPLE acceptable answers)
            split_answers = row["Answer"].split(";")

            for answer in split_answers:
                answer = answer.strip()
                if answer:
                    answers.append(answer) # Figure out a way to standardize the answer in Step 2
            prompts = []

            if row["Prompts"]:
                split_prompts = row["Prompts"].split(";")
                for prompt in split_prompts:
                    prompt = prompt.strip()
                    if prompt:
                        prompts.appened(answer) # Figure out a way to standardize the answer in Step 2

            # Something here on the (*) for power scoring??
            # like....
            question_text = row["Question Text"]
            if "(*)" in question_text: # (*) is the common symbol used in Quizbowl to indicate a "power region," so I also utilize it in my database
                # Something here
                power_index = question_text.index("(*)")
                question_text_clean = question_text.replace("(*)", "")
            else:
                # Something similar here
                power_index = len(question_text)
                question_text_clean = question_text
                # We should probably add whatever we do to powers to the "questions" dictionary for proper storage??

    return questions


# STEP 2: STANDARDIZE THE TEXT IN OUR ANSWWERS SO THAT USER INPUTS DON'T UPSET PYTHON
def standardize(text):
    text = text.lower()
    clean_text = ""
    for character in text:
        if character.isalnum() or character.isspace(): # .isalnum means is alphanumeric!
            clean_text += character
        else:
            clean_text += " "
    return # I don't know what to return here just yet??

# STEP 3: ASK QUESTIONS TO USER INCREMENTALLY (WORD-BY-WORD)
def ask_question(question):
    words = question["text"].split()
    current_word_index = 0
    try:
        while current_word_index < len(words):
            # something
    except KeyboardInterrupt: # THIS IS HOW WE INTERRUPT!! Takes Ctrl+C as the default trigger mechanism.
        print("\n\n[BUZZ!]") # Tells the user they're buzzing
        return #something here

    print("\n") # Space things out
    return # something

# STEP 4: CREATE A FUNCTION TO CHECK THE USER'S ANSWER
def check_answer(user_answer, answers, prompts):
    user_answer = standardize(user_answer)
    for answer in answers:
        if answer == user_answer or answer in user_answer:
            return "correct"
        for prompt in prompts:
            if prompt == user_answer or prompt in user_answer:
                return "prompt"
            return "incorrect" # (if it's not a correct answer or a prompt, effectively an "else")

# STEP 5: FIGURE OUT MID-QUESTION BUZZING (& SCORING??)
def mid_question_buzz(something here):
    

# STEP 6: FIURE OUT END-OF-QUESTION

# STEP 7: ALLOW USERS TO "QUIT" WHEN THEY ARE DONE PLAYING

# STEP 8: FUNCTION THAT ACTUALLY RUNS THE GAME COMPLETELY
# def play_game():
# Input will ultimately be the csv file to run
if __name__ == "__main__":
    play_game("questions.csv") # Use the imported question database CSV
