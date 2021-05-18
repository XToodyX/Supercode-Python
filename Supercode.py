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
        PYinput = ""
        x_white = 0
        x_black = 0
        notvalid = True

        while notvalid:
            PYinput = input(">").lower()
            if PYinput == "help":
                print(colorinfo)
                PYinput = ""
                continue
            # Check if the input is valid
            try:
                for value in PYinput:
                    if 1 <= int(value) <= 6:
                        notvalid = False
                        continue
                    else:
                        notvalid = True
                        break
            except ValueError:
                print("Please enter 4 numbers from 1-6")

        ListPYinput = list(PYinput)
        PYinput = [int(x) for x in PYinput]
        # Check count of black in the input
        for index, number in enumerate(solNumbers):
            if int(ListPYinput[index]) == number:
                x_black += 1

        # PYinput is List of integers
        # Check count of white in the input
        randomNumbers = set(solNumbers)

        # Check count of white in the input
        for x in randomNumbers:
            counter = PYinput.count(x)
            if not counter > solNumbers.count(x):
                x_white += counter
        x_white -= x_black
        # Make sure that x_white isn't negative
        if x_white < 0:
            x_white = 0
        print(f"{rounds + 1}. You have {x_black}x Black ones and {x_white}x White ones")

        if x_black == 4:
            print("Congratulations you won :-)")
            quit(0)

def playeasy(solNumbers):
    # Player has 8 attempts to find
    # the correct color sequence
    print("To get help write help")
    for rounds in range(8):
        PYinput = ""
        x_white = 0
        x_black = 0
        while len(set(PYinput) & {"1","2","3","4","5","6"}) != 4:
            PYinput = input(">").lower()
            if PYinput == "help":
                print(colorinfo)
                PYinput = ""
                continue

        ListPYinput = list(PYinput)
        PYinput = map(int, PYinput)

        # Check count of black in the input
        for index, number in enumerate(solNumbers):

            if int(ListPYinput[index]) == number:
                x_black += 1

        # Check count of white in the input
        x_white = len(set(solNumbers) & set(PYinput)) - x_black
        # Make sure that x_white isn't negative
        if x_white < 0:
            x_white = 0

        print(f"{rounds+1}. You have {x_black}x Black ones and {x_white}x White ones")

        if x_black == 4:
            print("Congratulations you won :-)")
            quit(0)

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


