# TODO-1: Ask the user for input

from art import logo
print(logo)

# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
from art import logo
print(logo)

bids = {}
auction = True

while auction:
    name = input("What is your name? ")
    bid = int(input("What's your bid? $"))
    bids[name] = bid

    continue_bidding = input("Is there a new bid? Type 'yes' or 'no': ").lower()
    print("\n" * 20)

    if continue_bidding == "no":
        auction = False


# Find the highest bidder
highest_bid = 0
winner = ""

for bidder, amount in bids.items():
    if amount > highest_bid:
        highest_bid = amount
        winner = bidder

print(f"The highest bidder is {winner} with ${highest_bid}")
