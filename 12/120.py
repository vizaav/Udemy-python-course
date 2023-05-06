import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
answer = random.randint(1, 100)
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
if difficulty != 'easy' and difficulty != 'hard':
    print("Invalid input.")
    exit()
if difficulty == 'easy':
    attempts = 10
else:
    attempts = 5


def compare(correct_answer, guessed_number):
    if correct_answer == guessed_number:
        print("That's the right number! You win!")
        return False
    elif guessed_number > correct_answer:
        print("Too high.")
        print("Guess again.")
        return True
    elif guessed_number < correct_answer:
        print("Too low.")
        print("Guess again.")
        return True


looping = True

while looping:
    guess = int(input("Make a guess: "))
    looping = compare(answer, guess)
    if looping:
        attempts -= 1
        if attempts <= 0:
            print("No attempts left. You lose.")
            exit()
        print(f"You have {attempts} attempts left to guess the number.")
