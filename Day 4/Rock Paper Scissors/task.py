import random

print("Welcome to the Rock Paper Scissors Game.")
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

human_play = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors 1 \n"))
computer_play = random.randint(0,2)

hand_signals = [rock, paper, scissors]


if 0 <=  human_play <= 2:
    print(f"Human plays \n  {hand_signals[human_play]}")
    print(f"Computer plays \n  {hand_signals[computer_play]}")
else:
    print("You typed an invalid number. You lose!")

if human_play == 0 and computer_play == 2:
    print("You wins.")
elif human_play == 1 and computer_play == 0:
    print("You wins.")
elif human_play == 2 and computer_play == 1:
    print("You win.")
elif human_play == computer_play:
    print("it's a draw.")
else:
    print("Computer wins")