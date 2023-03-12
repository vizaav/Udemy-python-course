# lists
import random

fruits = ["banana", "apple", "strawberry"]
print(fruits[0])
print(fruits[-3])
fruits.append("orange")
print(fruits[0])
print(fruits[-3])
fruits.extend(["grape", "kiwi"])
print("I'm going to eat that " + fruits[random.randint(0, len(fruits) - 1)] + "!")

# 🚨 Don't change the code below 👇
row1 = ["⬜️", "️⬜️", "️⬜️"]
row2 = ["⬜️", "⬜️", "️⬜️"]
row3 = ["⬜️️", "⬜️️", "⬜️️"]
mapa = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

# Write your code below this row 👇
coordinateX = int(position[0])
coordinateY = int(position[1])
mapa[coordinateY - 1][coordinateX - 1] = "X"

# Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")


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

#Write your code below this line 👇
asciiArt = [rock, paper, scissors]
userChoice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
if userChoice >= 3 or userChoice < 0:
    print("You typed an invalid number, you lose.")
    quit()
print(asciiArt[userChoice])
computerChoice = random.randint(0, 2)
print("Computer chose: " + str(computerChoice))
print(asciiArt[computerChoice])
if userChoice == computerChoice:
  print("Draw")
elif userChoice == 0:
    if computerChoice == 1:
      print("You lose")
    else:
      print("You win")
elif userChoice == 1:
    if computerChoice == 0:
      print("You win")
    else:
      print("You lose")
elif userChoice == 2:
    if computerChoice == 0:
      print("You lose")
    else:
      print("You win")