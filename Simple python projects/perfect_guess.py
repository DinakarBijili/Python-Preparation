import random 
randNum = random.randint(1,100)
guess = 0

print("---------WELCOME TO GUESS GAME---------")
print("YOU HAVE 10 CHANCES TO GUESS THE NUMBER....\n")

while (guess < 10):
    user = int(input("Guess a number between 1 to 100: \n"))
    guess += 1
    
    if user > randNum:
        print("Too High! Please enter lower number")
        
    elif user < randNum:
        print("Too Low! Enter higher number ")
        
    else:
        print("Congrats you Won the game in",guess,"guessess")
        break
    
print("OPPs ! YOU Reached TO GUESSING LIMITS.THE GUESS NUMBER WAS ->>",randNum)
