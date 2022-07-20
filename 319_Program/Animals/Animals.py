def calculate():
    animals = int(0)
    legs = int(0)
    rabbit = int(0)
    chicken = int(0)
    maxLegs = int(0)
    minLegs = int(0)

    animals = int(input("Enter the number of animals: "))

    maxLegs = animals*4
    minLegs = animals*2

    print("max legs: ", maxLegs)
    print("min legs: ", minLegs)

    legs = int(input("Enter number of legs: "))

    while legs > maxLegs or legs < minLegs:
        legs = int(input("Enter a valid number of legs: "))

    rabbit = animals
    while (rabbit * 4 + chicken*2) > legs:
        rabbit = rabbit -1
        chicken = chicken + 1

    print("Number of rabbits: ", rabbit)
    print("Number of chickens: ", chicken)

if __name__ == "__main__":
    print("Welcome!")
    calculate()
    print("Goodbye!")