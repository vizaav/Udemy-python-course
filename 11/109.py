from art import logo
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_wins = 0
dealer_wins = 0


class User:
    def __init__(self):
        self.cards = []
        self.score = 0
        self.is_bust = False


    def add_card(self, card):
        self.cards.append(card)
        self.score += card

    def check_bust(self):
        if self.score > 21:
            if 11 in self.cards:
                self.cards[self.cards.index(11)] = 1
                self.score -= 10
                self.check_bust()
            else:
                self.is_bust = True

    def check_blackjack(self):
        if self.score == 21:
            return True
        else:
            return False

    def reset(self):
        self.cards = []
        self.score = 0
        self.is_bust = False


"""
START
"""
print(logo)
loop = True
while loop:
    choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if choice == 'y':
        user = User()
        dealer = User()
        user.add_card(cards[random.randint(0, 12)])
        user.add_card(cards[random.randint(0, 12)])
        dealer.add_card(cards[random.randint(0, 12)])
        dealer.add_card(cards[random.randint(0, 12)])
        print(f"Your cards: {user.cards}, current score: {user.score}")
        print(f"Computer's first card: {dealer.cards[0]}")
        if user.check_blackjack():
            print("Blackjack! You win!")
            user_wins += 1
        else:
            while True:
                choice = input("Type 'y' to get another card, type 'n' to pass: ")
                if choice == 'y':
                    user.add_card(cards[random.randint(0, 12)])
                    user.check_bust()
                    if user.is_bust:
                        print(f"Your final hand: {user.cards}, final score: {user.score}")
                        print("You went over. You lose.")
                        dealer_wins += 1
                        break
                    else:
                        print(f"Your cards: {user.cards}, current score: {user.score}")
                else:
                    break
            if not user.is_bust:
                while True:
                    dealer.add_card(cards[random.randint(0, 12)])
                    dealer.check_bust()
                    if dealer.is_bust:
                        print(f"Computer's final hand: {dealer.cards}, final score: {dealer.score}")
                        print("Computer went over. You win!")
                        user_wins += 1
                        break
                    elif dealer.score > user.score:
                        print(f"Computer's final hand: {dealer.cards}, final score: {dealer.score}")
                        print("You lose.")
                        dealer_wins += 1
                        break
                    elif dealer.score == user.score:
                        print(f"Computer's final hand: {dealer.cards}, final score: {dealer.score}")
                        print("Draw.")
                        break
                    else:
                        continue
    else:
        print("Goodbye.")
        loop = False
    print(f"User wins: {user_wins}")
    print(f"Dealer wins: {dealer_wins}")