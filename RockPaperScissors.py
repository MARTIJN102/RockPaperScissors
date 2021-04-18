# -- This function is made because I use this goodbye message twice in the code and I want the code to be as short as possible.
def goodbye():
    line = "-" * 51
    print(line)
    print("| Thanks for playing my Rock Paper Scissors game! |")
    print(line)
    line = "-" * 27
    print("| Author: Martijn Miedema |")
    print("|    Age: 20              |")
    print("|  Study: Programming     |")
    print(line)

# -- Theese are the imports needed for this rock paper scissors game.
import random
import os
import time

# -- Counts the amount of wins, looses and draw's.
wcount = 0
dcount = 0
lcount = 0

# -- Counts the amount of time that each object has been choosen by the computer.
rcount = 0
pcount = 0
scount = 0

# -- Counts the amount of games played.
gcount = 0

game = True

# -- Asks the user for his name and then prints a little welcome message.
UserName = input("Please enter your username: ").title()
os.system("cls")
print("Welcome " + UserName + ", I hope you enjoy the game!")
print("\nIf you want to know how many times you have\nlost, won or had a draw you can type stats.\n\nIf you want to know how many times the computer variates between\nRock, Paper and Scissors you can type debug.\n\nIf you want to save your stats you could also type save\nand it will save the current stats in a score.txt file.")

# -- The while loop makes the code run over and over again untill the user types quit, stop or leave then closes the terminal.
while game:

    print("\nBeatable Rock Paper Scissors game!")
    userInput = input("\nChoose your object: ").lower()
    number = random.randint(1,3)

    # -- If the input ins't = to Rock Paper or Scissors it wont count it as a game.
    if userInput == "rock" or userInput == "paper" or userInput == "scissors":
        gcount += 1

    # -- If the userInput != to one of the strings in this if statement it will tell the user to enter one of them instead.
    if userInput == "rock" or userInput == "paper" or userInput == "scissors":
        if number == 1:
            print("\nRock")
            rcount += 1
        elif number == 2:
            print("\nPaper")
            pcount += 1
        elif number == 3:
            print("\nScissors")
            scount += 1

        # -- Tells the player he lost.
        if number == 1 and userInput == "scissors" or number == 2 and userInput == "rock" or number == 3 and userInput == "paper":
            print("\nYou lost!")
            lcount += 1
            time.sleep(2.5)
            os.system("cls")

        # -- Tells the player he won.
        elif userInput == "scissors" and number == 2 or userInput == "paper" and number == 1 or userInput == "rock" and number == 3:
            print("\nYou won!")
            wcount += 1
            time.sleep(2.5)
            os.system("cls")

        # -- Tells the player it was a draw.
        elif userInput == "rock" and number == 1 or userInput == "paper" and number == 2 or userInput == "scissors" and number == 3:
            print("\nDraw!")
            dcount += 1
            time.sleep(2.5)
            os.system("cls")

    # -- If the user types stats the game will provide the amount of times he has won and lost and how many times it was a draw.
    elif userInput == "stats":
        if gcount >= 5:
            os.system("cls")
            winlossRatio = wcount / lcount
            print("\nHey " + UserName + ", Your stats are:")
            print("\nWins: " + str(wcount))
            print("Draws: " + str(dcount))
            print("Losses: " + str(lcount))
            print("\nWin/Loss ratio: " + str(winlossRatio))
            print("Total amount of games played: " + str(gcount))
        elif gcount < 5:
            print("\nYou need to play 5 games before you can use the stats function\nAmount played: " + str(gcount))


    # -- If the user wants to know how the program variates between the numbers this debug option will tell the user how many times the program choose for rock, paper and scissors.
    elif userInput == "debug":
        os.system("cls")
        print("\nList of variation between Rock, Paper and Scissors")
        print("Rock: " + str(rcount))
        print("Paper: " + str(pcount))
        print("Scissors: " + str(scount))

    # -- This code gives the player the option to save his score (Wins, Losses and amount of times it was a Draw).
    elif userInput == "save":
        os.system("cls")
        if gcount >= 5:
            line = "-" * 55
            winlossRatio = wcount / lcount
            f = open("score.txt","a+")
            for i in range(1):
                f.write("\n\n" + line)
                f.write("\nHey " + UserName + ", Your stats are:")
                f.write("\n\nWins: " + str(wcount))
                f.write("\nDraws: " + str(dcount))
                f.write("\nLosses: " + str(lcount))
                f.write("\n\nWin/Loss ratio: " + str(winlossRatio))
                f.write("\nTotal amount of games played: " + str(gcount))
            f.close()
            line = "-" * 31
            print(line)
            print("| Your stats have been saved! |")
            print(line + "\n")
            # -- To know more about this goodbye() code see line 2.
            goodbye()
            time.sleep(2.5)
            game = False
        else:
            print("\nYou need to play 5 games before you can use the stats function\nAmount played: " + str(gcount))

    # -- This elif statement makes the game variable equal to False so the while loop doesn't kep going on and on.
    elif userInput == "stop" or userInput == "leave" or userInput == "quit" or userInput == "exit":
        os.system("cls")
        # -- To know more about this goodbye() code see line 2.
        goodbye()
        time.sleep(2.5)
        game = False

    # -- This else statement tells the user he needs to enter one of the strings on line 27.
    else:
        line = "-" * 41
        print("\n" + line)
        print("| Please enter Rock, Paper or Scissors! |")
        print("| Or enter one of the following:        |")
        print("| stats                                 |")
        print("| debug                                 |")
        print("| save                                  |")
        print(line)
