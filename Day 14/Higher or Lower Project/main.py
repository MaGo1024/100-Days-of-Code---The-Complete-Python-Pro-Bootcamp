# Display art.
from art import *
from game_data import data
import random

def format_data(account):
    """Takes the account data and returns the printable format."""
    account_name = account['name']
    account_desc = account['description']
    account_country = account['country']
    return f"{account_name}, a  {account_desc}, from {account_country}"

def check_answers(user_guess, a_followers, b_followers):
    """Takes the user guess and the follower count of account a dnd b and return if user guesses correctly."""
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"

print(logo)
# Generate a random account from the game data.
score = 0
game_continue = True
account_b = random.choice(data)

# Make the game repeatable
while game_continue:
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Compare B: {format_data(account_b)}.")

    # Ask user for a guess.
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # Clear the screen
    print("\n" * 20)
    print(logo)

    # Check if user is correct.
    ## Get follower count for each account
    a_follower_count = account_a['follower_count']
    b_follower_count = account_b['follower_count']
    ## Use if statement to check if user is correct.
    is_correct = check_answers(guess, a_follower_count, b_follower_count)
    # print(is_correct)

    # Give user feedback on their  guess.

    # Score keeping

    if is_correct:
        score += 1
        print(f"You're right!, Current score: {score}")
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        game_continue = False

    # Making the account at position B become the next account at position A.