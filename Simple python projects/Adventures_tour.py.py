print("---------WELCOME TO ADVENTURES TOUR---------")
name = input("Enter your Name: ")
age = int(input("Enter your age: "))

health = 10

while age >= 18:
    print("You are old enough to Play!",name)

    want_to_play = input("Do you want to play (yes/no)? \n" ).lower()
    if want_to_play == "yes":
        print("You are Starting with",health,"healths")
        print("Lets Go!\n")

        left_or_right = input("First choice....Go left or right(left/right)? \n").lower()
        if left_or_right == "left":
            ans = input("You are on the right path and reach a lake...Do you swim across or go around (across/around)? \n").lower()

            if ans == "around":
                print("You went around and reached the other side of the lake")
            elif ans == "across":
                print("You managed to get across, but were bit by a fist and lost 5 healths.")                  
                health -= 5
                print("Remaining health left ->>",health)
            else:
                print("Please Check your Spelling....")
            ans = input("Now you notice a house and a bridge. Which way you want to go (house/bridge)? \n").lower()
            if ans == "bridge":
                print("The bridge was broken and you fell for it and you lost....")
                print("BETTER LUCK NEXT TIME. TRY AGAIN...")
                break
            elif ans == "house":
                print("You are Still Surving....Keep Going...")
            ans = input("You went to house and you saw 2 Doors in which in 1st door their was a dark room and on the 2nd door their was a full of water. which door you want go(1/2)? \n")
            
            if ans == "1":
                print("water cames out with full presure and you fell for it and Lost the Game!")
                print("BETTER LUCK NEXT TIME. TRY AGAIN...")
                break
            elif ans == "2":
                print('In Dark room their are Full of Dogs and you fell for it and lost 5 health Points...')
                health -= 5
                if health <= 0:
                    print("YOU LOST THE GAME! Better Luck next time.")
                else:
                    print("You Still have ",health,"points to survive")
                ans = input("Congrats you are going well...Now you saw a Forest and Road. Which way you want to go(forest/road)? ").lowar()
                if ans == "road":
                    print("OPPs you are on the wrong Track of the road their is no escape from the road beacuse their is an end road Block! GAME OVER")
                    print("BETTER LUCK NEXT TIME. TRY AGAIN...")
                    break
                elif ans == "forest":
                    print("Congrats you came to Safe Place and Won the Game! ")
                    print("THANKS FOR PLAYING.....HOPE YOU ENJOYED")
                    break
        else:
            print("You Choose the wrong path and fell down and you Lost the Game....")
            break
    else:
        break
else:
    print("You are not old enough to play")
        
