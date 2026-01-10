from random import randint
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

# Function to check the user's guess against the actual answer
def check_answer(user_guess, actual_answer, turns):
    """Checks answers against guess, returns the number of turns left."""
    if user_guess > actual_answer:
       print("You guessed too high")
       return turns - 1
    elif user_guess < actual_answer:
        print("You guessed too low")
        return turns - 1
    else:
        print(f"You guessed correctly! The answer is  {user_guess}.")

# Function to set difficulty
def set_difficulty():
    level = input("Choose a difficulty level (easy or hard): ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS



def game():
    print(logo)
    # Choosing a number between 1 and 100
    print("Welcome to the Guessing Game!")
    print("I am thinking of a number between 1 and 100.")
    answer = randint(1, 100)
    print(f"Pssst, the correct answer is {answer}.")

    # Let the user guess a number
    turns = set_difficulty()

    guess = 0
    # Repeat guessing functionality if they are wrong
    while guess != answer:
        print(f"You have {turns} turns left")
        guess = int(input("Guess the number: "))
        turns = check_answer(guess, answer, turns)
        # Track the number of turns, and reduce by 1 if they get it wrong
        if turns == 0:
            print("You ran out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again.")

game()
