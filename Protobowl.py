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
                    answers.append(standardize(answer)) # Figure out a way to standardize the answer in Step 2
            prompts = []

            if row["Prompts"]:
                split_prompts = row["Prompts"].split(";")
                for prompt in split_prompts:
                    prompt = prompt.strip()
                    if prompt:
                        prompts.append(standardize(prompt)) # Figure out a way to standardize the answer in Step 2

            # Handle (*) for power scoring
            question_text = row["Question Text"]
            if "(*)" in question_text: # (*) is the common symbol used in Quizbowl to indicate a "power region," so I also utilize it in my database
                power_index = question_text.index("(*)")
                question_text_clean = question_text.replace("(*)", "")
            else:
                power_index = len(question_text)
                question_text_clean = question_text
                # We should probably add whatever we do to powers to the "questions" dictionary for proper storage??

            questions.append({
                "text": question_text_clean,
                "answers": answers,
                "prompts": prompts,
                "power_index": power_index
            })

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
    return " ".join(clean_text.split()) # Remove extra spaces, too!


# STEP 3: ASK QUESTIONS TO USER INCREMENTALLY (WORD-BY-WORD)
def ask_question(question):
    words = question["text"].split()
    current_word_index = 0
    try:
        while current_word_index < len(words):
            print(words[current_word_index], end=" ", flush = True)
            # See if we can make a boolean flush
            time.sleep(0.5)
            current_word_index += 1
            # something
    except KeyboardInterrupt: # THIS IS HOW WE INTERRUPT!! Takes Ctrl+C as the default trigger mechanism.
        print("\n\n[BUZZ!]") # Tells the user they're buzzing
        return mid_question_buzz(question, current_word_index, words)

    print("\n") # Space things out
    return score_final(question)


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
def mid_question_buzz(question, current_word_index, words):
    # Estimate character index for power scoring
    location_when_buzzed = 0
    for i in range(current_word_index):
        location_when_buzzed += len(words[i]) + 1

    # Ask the player for their answer after they buzz
    while True:
        user_answer = quit_input("Your answer: ").strip()
        result = check_answer(user_answer, question["answers"], question["prompts"])
        if result == "correct":
            if location_when_buzzed < question["power_index"]:
                print("POWER! +15 points.\n")
                return 15 # 15 points!
            else:
                print("Correct! +10 points.\n")
                return 10 # 10 points!
        elif result == "prompt":
            print("PROMPT! Please be more specific.")
            continue
        else:
            print("Incorrect. Continuing to read the question....\n")
            break

    # Resume printing the question from the buzz point
    while current_word_index < len(words):
        print(words[current_word_index])
        time.sleep(0.3)
        current_word_index += 1
    print("\n")

    return score_final(question)


# STEP 6: FIURE OUT END-OF-QUESTION
def score_final(question, buzzed = False):
    while True:
        user_answer = quit_input("Final answer: ").strip()
        result = check_answer(user_answer, question["answers"], question["prompts"])
        if result == "correct":
            print("Correct! +10 points.\n")
            return 10 # 10 points!
        elif result == "prompt":
            print("Prompt: please be more specific.")
            continue
        else:
            print(f"Wrong. The correct answer was: {question['answers'][0]}\n")
            return 0


# STEP 7: ALLOW USERS TO "QUIT" WHEN THEY ARE DONE PLAYING
def quit_input(prompt_text = ""):
    # Get user input AND exit is they type 'quit'
    user_input = input(prompt_text).strip()
    if user_input.lower() in ["quit"]:
        print("Exiting game. Goodbye!") # Should we print the score here? CAN we print the score here? IDK.
        exit(0) # Stop the program
    return user_input

# STEP 8: FUNCTION THAT ACTUALLY RUNS THE GAME COMPLETELY
def play_game(file):
    questions = load_questions(file)
    score = 0

    # Something here introducing the rules of the game
    print("\n\nWelcome to Python Terminal Protobowl: Harvard Edition!\n")
    print("RULES OF THE GAME:")
    print("Press Ctrl+C to buzz during a question.")
    print("Correct answers are worth 10 points. Questions answered correctly within the first sentences of the passage are worth 15 points.")
    print("In order to end the game, buzz in to any question and type 'quit'.\n") #Revise once I figure out how to trigger game end successfully!!

    # Make python give the user some time to read the rules and get ready
    time.sleep(5)
    print('Beginning game in 5....')
    time.sleep(1)
    print('....4....')
    time.sleep(1)
    print('....3....')
    time.sleep(1)
    print('....2....')
    time.sleep(1)
    print('....1....')
    time.sleep(1)
    print('BEGINNING GAME NOW!\n')
    time.sleep(.5) # Pause so user can mentally prepare lol

    while True:
        question = random.choice(questions)
        # Could we maybe make it so the same question can't randomly be chosen twice in a row? IDK how to do that necessarily -- seeding??
        points = ask_question(question)
        score += points
        print(f"Score: {score}\n")
        time.sleep(1)

# Input will ultimately be the csv file to run
if __name__ == "__main__":
    play_game("questions.csv") # Use the imported question database CSV
