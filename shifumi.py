import random

choice_ia = ["R", "S", "P"]
ia = ["David", "Eytan", "Shiran"]
name_ia = random.choice(ia)
name = input("welcome Player ! What is your Name ?\n")
print(f"Nice to meet you {name}, my name is {name_ia}")
rules = input("I'm challenging you to a ShiFuMi Game !\nRead the rules first ?\t Y\\N\n")
if rules == "Y":
    print("""I's a classic Rock/Paper/Scissor Game where you play against the IA.
- Rock beats Scissor but loose against Paper.
- Scissor beats Paper but loose against Rock.
- Paper beats Rock but loose against Scissor.
You start the Game with 3 credits. It ends when you get to 0.
the Game stores your wins.

OK ! So let's play already !""")
if rules == "N":
    print("OK ! So let's play already !")

count = 3
record = -1
choice_name = ""
option_ia = ""


def high_score():           # return the number of wins
    global record
    record += 1
    return record


def end_game():             # take the user out game
    print(f"{name}, you haven't any credit left\n\nGAME OVER\n")
    print(f"{name}, your highest score is {high_score()}")
    exit()


def start_the_game():       # take input from user and random from ia
    global choice_name
    global option_ia
    choice_name = input(f"{name}, What is your move ?\n(R)ock\t(S)cissor\t(P)aper\n")
    option_ia = random.choice(choice_ia)
    for x in range(3,0,-1):
        print(x)


start_the_game()


def Shi():                  # first part of the validation
    global count
    if choice_name == "R" and option_ia == "R":
        print("Rock vs Rock")
        print("No Winner")
    elif choice_name == "S" and option_ia == "R":
        print("Scissor vs Rock")
        print(f"too Bad {name}, You Lost")
        count -=1
        if count == 0:
            end_game()
    elif choice_name == "P" and option_ia == "R":
        print("Paper vs Rock")
        print(f"Yeah {name}, you Win !")
        count += 1
        high_score()
    else:
        Fu()


def Fu():                   # second part of the validation
    global count
    if choice_name == "S" and option_ia == "S":
        print("Scissor vs Scissor")
        print("Taiko")
    elif choice_name == "P" and option_ia == "S":
        print("Paper vs Scissor")
        print(f"{name}, You are a Loser !")
        count -= 1
        if count == 0:
            end_game()
    elif choice_name == "R" and option_ia == "S":
        print("Rock vs Scissor")
        print(f"{name}, you are a Winner !")
        count += 1
        high_score()
    else:
        Mi()


def Mi():                   # third part of the validation
    global count
    if choice_name == "P" and option_ia == "P":
        print("Paper vs Paper")
        print(f"{name_ia} is not impressed")
    elif choice_name == "R" and option_ia == "P":
        print("Rock vs Paper")
        print(f"{name_ia} won this one !")
        count -= 1
        if count == 0:
            end_game()
    elif choice_name == "S" and option_ia == "P":
        print("Scissor vs Paper")
        print(f"{name_ia} lost this one !")
        count += 1
        high_score()


Shi()

print(f"{name}, You have {count} credits left")


def poq():                  # check if the user wants out
    play_or_quit = input("Play (A)gain or (Q)?")
    if play_or_quit == "Q":
        print(f"Bye, {name}, your highest score is {high_score()}")
        exit()
    elif play_or_quit == "A":
        start_the_game()
        Shi()
        print(f"\n{name}, You have {count} credits left")
        poq()


poq()


# for later : implement difference between ias. like one cant play rock (take 1 from the list)


