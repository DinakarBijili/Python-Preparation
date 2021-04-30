# A simple example of tic tac toe game

# For storing user choices
choices = []

# For initializing the board with numbers
for i in range(0, 9):
    choices.append(str(i))

Play = True
winner = False
iterations = 0      # To terminate the loop

# For drawing board on to the terminal
def printBoard():
    print('\n=============')
    print('| ' + choices[0] + ' | ' + choices[1] + ' | ' + choices[2] + ' |')
    print('=============')
    print('| ' + choices[3] + ' | ' + choices[4] + ' | ' + choices[5] + ' |')
    print('=============')
    print('| ' + choices[6] + ' | ' + choices[7] + ' | ' + choices[8] + ' |')

    print('=============\n')
FirstPlayer = input( "Enter FirstPlayer  name [X]: ").upper()
SecondPlayer = input("Enter SecondPlayer name [0]: ").upper()

# Play the game while the winner is not decided or the game is drawn
while not winner and iterations < 9:
    printBoard()

    iterations += 1 # increase the iterations if we Enter some thing

    

    if Play == True:
        print(FirstPlayer ,"[X] TURN: ", end = '')
    else:
        print(SecondPlayer ,"[0] TURN: ", end = '')

    try:
        playerInput = int(input())
        if playerInput >= 9:
            print("Please enter a valid number from the board")
            continue
    except:
        print('Please enter a valid number from the board')
        continue

    # Check if userInput already has 'X' or 'O'
    if choices[playerInput] == 'X' or choices[playerInput] == 'O':
        print('Illegal move, try again!')
        continue

    if Play:
        choices[playerInput] = 'X'
    else:
        choices[playerInput] = 'O'

    Play = not Play

    # Winning conditions
    for index in range(0, 3):
        # For [0,1,2], [3,4,5], [6,7,8]
        if (choices[index * 3] == choices[((index * 3) + 1)] and choices[index * 3] == choices[((index * 3) + 2)]):
            winner = True
            printBoard()

        # For [0,3,6], [1,4,7], [2,5,8]
        if(choices[index] == choices[index + 3] and choices[index + 3] == choices[index + 6]):
            winner = True
            printBoard()
    
    if((choices[0] == choices[4] and choices[4] == choices[8]) or
      (choices[2] == choices[4] and choices[4] == choices[6])):
        winner = True
        printBoard()

if winner:
    print('Player ' + str(int(Play + 1)) + ' wins!')
else:
    print('Game drawn')
