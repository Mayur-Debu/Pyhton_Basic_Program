guess=1
guess_num=15
while(guess<6):
    number=int(input("ENTER YOUR GUESS: "))
    if guess==5:
        print("game over\n")
        break
    else:
        guess+=1
        if number==guess_num:
            print("YOU WON in "+str(guess)+" Guesses")
            break
        elif number>guess_num:
            print("Enter something lesser")
        else:
            print("Enter something greater")