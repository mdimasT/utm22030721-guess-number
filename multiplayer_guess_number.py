import getpass
player1_wins = 0
player2_wins = 0

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
            # Player two guessed the correct number and still has attempts remaining
            print("")
            print("Congratulations,",player_2," you have won")
            print("Remaining points:",attempts)
            player2_wins = player2_wins + 1
            break

        elif attempts == 10 :
            # Player two has no attempts remaining
            print("")
            print("No points remaining, you have lost", player_2)
            print("The correct number was: ",number_to_guess)
            print("Congratulations,",player_1, "you have won")
            player1_wins = player1_wins + 1
            break


        else:
            # Player two guessed the wrong number
            print("")
            print("You have lost 10 points, try it again")
            attempts = attempts - 10
            print("You have ",attempts, "points left")
    
    print("")
    print("Would you like to play again? Enter no to exit the game or anything else to continue playing." )
    again  = input()

    if again.upper() == "NO":
        break

    
print("")
print("Game over")
print("Player 1 wins: ",player1_wins)# Display player one's win count
print("Player 2 wins: ",player2_wins)# Display player two's win count

    