import subprocess, os

from art import logo

#HINT: You can call clear() to clear the output in the console.
print(logo)
print("Welcome to the secret auction program.")
looping = True
bids = {}
while looping:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    if name in bids:
        print("Name already exists")
        continue
    bids[name] = bid
    more_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    os.system('cls' if os.name == 'nt' else 'clear')

    if more_bidders == "no":
        looping = False
        max_bid = 0
        winner = ""
        for name in bids:
            if bids[name] > max_bid:
                max_bid = bids[name]
                winner = name
        print(f"The winner is {winner} with a bid of ${max_bid}")
    elif more_bidders == "yes":
        continue

