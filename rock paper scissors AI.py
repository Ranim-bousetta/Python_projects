from random import randint
t=True
while t:
    p_wins=0
    c_wins=0
    w=3
    print(""" ...rock...
             ...paper...
            ...scissors...""")
    print(f"Player score: {p_wins},Computer score: {c_wins}")
    I=["ROCK","PAPER","SCISSORS"]
    while p_wins<w and c_wins<w:
        random_num = randint(0, 2)
        if (random_num == 0):
            computer = "ROCK"
        elif (random_num == 1):
            computer = "PAPER"
        else:
            computer = "SCISSORS"
        p1=input("(enter Player's choice):\n ")
        while p1=="" or not(p1.upper() in I) :
            p1=input("(enter Player's choice):\n ")
        print("computer now \n",computer)
        if (p1.upper()==I[0] and computer==I[1]) or (p1.upper()==I[1] and computer==I[2]) or (p1.upper()==I[2] and computer==I[0]):
            print("SHOOT Computer wins ")
            c_wins+=1
        elif p1.upper()==computer:
            print("It's a tie")
        else:
            print("Player wins ")
            p_wins+=1
        print(f"Player score: {p_wins},Computer score: {c_wins}")
    if p_wins>c_wins:
        print("yeeyyy you won!!")
    else:
        print("oh no the computer won :(")
    play_again=input("do you wanna play again?")
    if play_again.upper()=="YES":
        t=True
    else:
        t=False

