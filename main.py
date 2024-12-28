import random

def guessinggame():
    game = {"number": random.randint(1, 10)}
    while True:
        guess = int(input("guess a number from 1 to 10: "))
        
        if guess == game["number"]:
            print("Correct!")
            break
        else:
            print("Try again!")

guessinggame()
