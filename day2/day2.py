import re

def part_2():
    answer = 0
    input = open("input1.txt", "r").readlines()

    for game in input:
        gameId = int(re.findall("Game ([0-9]*):", game)[0])
        amountRed = re.findall("(\d+)(?=\s*red)", game)
        amountGreen = re.findall("(\d+)(?=\s*green)", game)
        amountBlue = re.findall("(\d+)(?=\s*blue)", game)
        
        minRed = 0
        minGreen = 0
        minBlue = 0

        for x in amountRed:
            x = int(x)
            if x > minRed:
                minRed = x

        for x in amountGreen:
            x = int(x)
            if x > minGreen:
                minGreen = x

        for x in amountBlue:
            x = int(x)
            if x > minBlue:
                minBlue = x

        answer += (minRed * minGreen * minBlue)

        
    print(f"answer: {answer}")

def part_1():
    answer = 0
    red = 12
    green = 13
    blue = 14
    input = open("input1.txt", "r").readlines()

    for game in input:
        isValid = True
        gameId = int(re.findall("Game ([0-9]*):", game)[0])
        amountRed = re.findall("(\d+)(?=\s*red)", game)
        amountGreen = re.findall("(\d+)(?=\s*green)", game)
        amountBlue = re.findall("(\d+)(?=\s*blue)", game)

        for x in amountRed:
            x = int(x)
            if x > red:
                isValid = False

        for x in amountGreen:
            x = int(x)
            if x > green:
                isValid = False

        for x in amountBlue:
            x = int(x)
            if x > blue:
                isValid = False

        if isValid:
            answer += gameId

        
    print(f"answer: {answer}")







part_2()