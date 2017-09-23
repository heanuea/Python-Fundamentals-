#Write a guessing game where the user must guess a secret number. 
# After every guess the program tells the user whether their number was too large or too small.
# At the end the number of tries needed should be printed.
# It counts only as one try if they input the same number multiple times consecutively.

import random

tries = []      #counts the attempts 
n = random.randint(1, 20)       #Picks a Random number between 1 and 20 
print("Guess a number between 1 and 20!")

while 1: 
    guess = int(input())

    if guess < n:
        print("Go higher")
        tries.append(guess)
    elif guess > n:
        tries.append(guess)
        print("Go Lower")
    else:
        tries.append(guess)
        print("BOOOM, You guessed in %d Attempts!" % len(set(tries)))
        break 
