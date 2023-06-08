import random

while True:
    print("")
    print("Enter the first number")
    try:
        fn = int(input())
        print("")
        print("Enter the second number")
        sn = int(input())

        if fn < sn:
            break
        else:
            print("")
            print("Remember the first number has to have a higher value than the second one")
    except ValueError:
        print("")
        print("Invalid input. Please enter valid numbers.")

randomNumber = random.randint(fn, sn)
attempts = 100

print(randomNumber)

while True:
    print("")
    print("Guess the number:")
    try:
        number = int(input())

        if number == randomNumber and attempts != 0:
            print("")
            print("Congratulations!!, you won with", attempts, "points")
            break

        elif attempts == 0:
            print("")
            print("No points remaining, you have lost")
            print("The correct number was:", randomNumber)
            break

        else:
            print("")
            print("You have lost 10 points, try again")
            attempts -= 10
            print("You have", attempts, "points left")
    except ValueError:
        print("")
        print("Invalid input. Please enter a valid number.")
