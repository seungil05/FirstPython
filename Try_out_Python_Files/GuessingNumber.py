import random
import math

#Returns after User input
lower = int(input("Enter a lower number:- "))
upper = int(input("Enter a upper number: "))

#Generate a random number
x = random.randint(lower, upper)
print("\n\tXou've only", round(math.log(upper - lower+1, 2)), " chances to guess integer!\n")

count = 0

while count < math.log(upper - lower + 1, 2):
    count += 1
    guess = int(input("Enter your guess: "))
    if guess == x:
        print("You guessed it!")
        break
    elif guess > x:
        print("Your guess is too high!")
    else:
        print("Your guess is too low!")
    print("\n")

if count >= math.log(upper - lower + 1, 2):
    print("You failed to guess the integer!")
    print("The integer was:", x)
    print("\n")
    print("You have used", count, "chances!")
    print("\n")

