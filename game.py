import random
#rock paper scissors game 
while True:
    choices=["rock","paper","scissors"]
    computer= random.choice(choices)
    player=None
    while player not in choices:
        player=input("rock,paper or scissors?: ").lower()
    if player==computer:
        print("player :",player)
        print("computer :",computer)
        print("Draw !")
    elif player=="rock":
        if computer=="paper":
            print("player :",player)
            print("computer :",computer)
            print("You lost")
        else:
            print("player :",player)
            print("computer :",computer)
            print("You won")
    elif player=="paper":
        if computer=="scissors":
            print("player :",player)
            print("computer :",computer)
            print("You lost")
        else:
            print("player :",player)
            print("computer :",computer)
            print("You won")
    else:
        if computer=="rock":
            print("player :",player)
            print("computer :",computer)
            print("You lost")
        else:
            print("player :",player)
            print("computer :",computer)
            print("You won")
    play_again=input("Play again?(Y/N)").lower()
    if play_again!="y":
        break
print("Bye!")