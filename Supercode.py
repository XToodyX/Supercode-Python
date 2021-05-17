import random

colorinfo = "1: Red \n" \
            "2: Green \n" \
            "3: Blue \n" \
            "4: Orange \n" \
            "5: Yellow \n" \
            "6: Gray"

def generateNumbers(difficulty):
    if difficulty == "e":
        posiblevalues = [1,2,3,4,5,6]
        randnumbers = []
        # Creates a list(randnumers) of 4 numbers from posiblevalues,
        # which exists only once in the list(randnumbers)
        for x in range(4):
            number = posiblevalues[random.randint(0, len(posiblevalues)-1)]
            randnumbers.append(number)
            posiblevalues.remove(number)

        return randnumbers

    elif difficulty == "h":
        return [random.randint(1,6) for x in range(4)]

def playhard(solNumbers):
    # Player has 8 attempts to find
    # the correct color sequence
    print("To get help write help")
    for rounds in range(8):
        pass

def playeasy(solNumbers):
    # Player has 8 attempts to find
    # the correct color sequence
    print("To get help write help")
    for rounds in range(8):
        print("Hallo")
        PYinput = ""

        while PYinput != "help" and PYinput not in ["1","2","3","4","5","6"]:
            PYinput = str(input(">").lower())

if __name__ == '__main__':

    # Ask for level of difficulty Easy or Hard
    difficulty = ""
    while difficulty != "e" and difficulty != "h":
        difficulty = input("Please choose the level of difficulty Easy(E) or Hard(H) \n>")[0].lower()

    # Generates random numbers from 1-6
    # based on the difficulty
    randomNumbers = generateNumbers(difficulty)

    # Try-Block am Ende hinzufügen
    if difficulty == "e":
        playeasy(randomNumbers)
    elif difficulty == "h":
        playhard(randomNumbers)


