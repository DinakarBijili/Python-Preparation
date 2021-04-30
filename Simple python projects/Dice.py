import random

print("---------DICE ROLLINGR GAME----------")
while True:
    randNum = random.randint(1,6)
    user = input("Press Enter to Roll the Dice : ")
    print("Press q to Quit -")
    print("\n")
    if user == "q":
        print("Hope You Enjoyed!")
        quit()
    elif randNum == 1:
        print("-------")
        print("       ")
        print("   o   ")
        print("       ")
        print("-------")

    
    elif randNum == 2:
        print("-------")
        print(" o     ")
        print("       ")
        print("     o ")
        print("-------")

    elif randNum == 3:
        print("-------")
        print(" o     ")
        print("   o   ")
        print("     o ")
        print("-------")

    elif randNum == 4:
        print("-------")
        print(" o   o ")
        print("       ")
        print(" o   o ")
        print("-------")
    elif randNum == 5:
        print("-------")
        print(" o   o ")
        print("   o   ")
        print(" o   o ")
        print("-------") 
    else:
        print("-------")
        print(" o o o ")
        print("       ")
        print(" o o o ")
        print("-------")


