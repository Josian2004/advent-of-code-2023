def part_2():
    input = []
    answer = 0
    with open('input.txt', 'r') as file:
        input = file.readlines()

    answer += len(input)

    def calculate(cards, currAnswer):
        tempcards = []
        for card in cards:
            winning = []
            myNumbers = []
            foundSeperator = False
            amountWon = 0

            splitCard = card.split()
            splitCard.pop(0)
            id = int(splitCard[0].removesuffix(":"))
            splitCard.pop(0)

            for number in splitCard:
                if number == "|":
                    foundSeperator = True
                elif foundSeperator:
                    myNumbers.append(number)
                else:
                    winning.append(number)

            for myNumber in myNumbers:
                if myNumber in winning:
                    amountWon += 1

            startIndex = id
            for i in range(startIndex, startIndex + amountWon):
                tempcards.append(input[i])
            

        print(len(tempcards))
        currAnswer += len(tempcards)
        if len(tempcards) > 0:
            calculate(tempcards, currAnswer)
        else:
            print(f"Answer: {currAnswer}")

    calculate(input, answer)


def part_1():
    input = []
    answer = 0
    with open('input.txt', 'r') as file:
        input = file.readlines()

    for card in input:
        winning = []
        myNumbers = []
        foundSeperator = False

        amountWon = 0
        points = 0

        card = card.split()
        card.pop(0)
        card.pop(0)

        for number in card:
            if number == "|":
                foundSeperator = True
            elif foundSeperator:
                myNumbers.append(number)
            else:
                winning.append(number)

        print(f"Winning: {winning}")
        print(f"Mine: {myNumbers}")

        for myNumber in myNumbers:
            if myNumber in winning:
                amountWon += 1

        print(f"Amount Won: {amountWon}")

        for i in range(0, amountWon):
            if points == 0:
                points = 1
            else:
                points = points * 2

        print(f"Points: {points}")

        answer += points

        print("__________________________")

    print(f"Answer: {answer}")


part_2()