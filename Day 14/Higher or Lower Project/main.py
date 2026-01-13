import random
from random import randint
from game_data import *
from art import *

"""Pick two random artist for the data dictionary and 
guess who has more followers.
if you are correct, game continues,the 2nd artist stay
and you guess followers against another random artist.
store you score in a counter
if you are wrong, the game ends. your final score is displayed.
"""
def highest_followers(user_1, user_2):
    if user_1["follower_count"] > user_2["follower_count"]:
        return user_1
    else:
        return user_2
#1. Pick two random artist from data
artist_1 = random.choice(data)
print(artist_1['name'])
artist_2 = random.choice(data)
print(artist_2)
#2. Guess who has more followers
#3. if guess is correct, game continues,increase score counter by 1, move artist to var 1 and select another random artist in var 2.
#4. else display final score and end game.

