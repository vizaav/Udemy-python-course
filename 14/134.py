from art import logo, vs
from game_data import data
from random import randint


class Account:
    def __init__(self, **info):
        self.name = info['name']
        self.follower_count = int(info['follower_count'])
        self.description = info['description']
        self.country = info['country']


def compare(account_a, account_b):
    if account_a.follower_count > account_b.follower_count:
        return 'a'
    elif account_a.follower_count < account_b.follower_count:
        return 'b'
    else:
        return 'equal'

correct_guesses = 0
accounts = []
for account in data:
    accounts.append(Account(**account))

print(logo)

while True:
    account_a = accounts[randint(0, len(accounts) - 1)]
    account_b = accounts[randint(0, len(accounts) - 1)]
    while account_a == account_b:
        account_b = accounts[randint(0, len(accounts) - 1)]
    print(f"Compare A: {account_a.name}, a {account_a.description}, from {account_a.country}.")
    print(vs)
    print(f"Against B: {account_b.name}, a {account_b.description}, from {account_b.country}.")
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    if guess == compare(account_a, account_b):
        correct_guesses += 1
        print(f"You're right! Current score: {correct_guesses}.")
    else:
        print(f"Sorry, that's wrong. Final score: {correct_guesses}.")
        break



