import getpass

#Start of loop asking players if they would like to play again.
while True:
    
    #Player one is asked for his name.
    print("Player 1, please enter your name")
    player_1 = input()

    print("")
    #Player two is asked for his name.
    print("Player 2, please enter your name")
    player_2 = input()

    print("")
    print(player_1,":")
    #Player one is asked for the number to guess.
    number_to_guess = int(getpass.getpass("Enter the number to guess"))
    print("")

    attempts = 100

    #start of the loop that will allow player two to guess.
    while True:
    
        print(player_2,":")
        print("Guess the number")
        number = int(input())
        print("")

        if number == number_to_guess and attempts != 0:
            print("")
            print("Congratulations,",player_2," you have won")
            print("Remaining points:",attempts)
            break

        elif attempts == 10 :
            print("")
            print("No points remaining, you have lost", player_2)
            print("The correct number was: ",number_to_guess)
            break

        else:
            print("")
            print("You have lost 10 points, try it again")
            attempts = attempts - 10
            print("You have ",attempts, "points left")
    
    print("")
    print("Would you like to play again?")
    again  = input()

    if again.upper() == "NO":
        break