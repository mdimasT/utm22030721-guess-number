import random

while True:
    print("")
    print("Enter the first number")
    fn = int(input())
    print("")
    print("Enter the second number")
    sn = int(input())

    if fn % 1 == 0 and fn < sn and fn != str and sn != str:
        break

    else:
        print("")
        print("Remember the first number has to have a higher value than the second one and exclude decimals")

randomNumber = random.randint(fn,sn)

attempts = 100

print(randomNumber)

while True:
    print("")
    print("Guess the number:")
    number = int(input())
    

    if number == randomNumber and attempts != 0:
        print("")
        print("Congratulations!!, you won with", attempts, "points")
        
        break

    elif attempts == 10:
        print("")
        print("No points remaining, you have lost")
        print("The correct number was: ",randomNumber)
        break

    else:
        print("")
        print("You have lost 10 points, try it again")
        attempts = attempts - 10
        print("You have ",attempts, "points left")
   



    
    