from random import randint
t=True
while  t:
    x=randint(1,10)
    guess=int(input("guess a number between 1 and 10: "))
    while x!=guess:
        if x>guess:
            print("too low try again")
            guess=int(input("guess a number between 1 and 10: "))
        elif x<guess:
            print("too high try again")
            guess=int(input("guess a number between 1 and 10: "))
    if  x==guess:
        print("you won!!")
        play_again=input("do you want to play again?")
        if play_again.upper()== "YES":
              t=True
        else:
            t=False
            print("Thank you for playing!")
	
        
    
