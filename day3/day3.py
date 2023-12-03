import re

def part_2():
    input = []
    answer = 0
    with open('input1.txt', 'r') as file:
        input = file.readlines()

    def get_gear_ratio(point):
        numbers = []
        print(point)
        for rowIndex in range(point["y"] - 1, point["y"] + 2):
            row = input[rowIndex]
            matches = re.finditer("[0-9]+", row)

            for match in matches:
                #print(match)
                for x in range(point["x"] - 1, point["x"] + 2):
                    if match.start() == x or match.end() - 1 == x:
                        print(f"found on x: {x} - y: {rowIndex}")
                        print(f"start: {match.start()} - end: {match.end() - 1}")
                        print("----------")
                        numbers.append(match.group())
                        break


        print(numbers)
        if len(numbers) != 2:
            return 0
        print("______________________________")
        return int(numbers[0]) * int(numbers[1])
    
    x = 0
    y = 0
    for row in input:
        x = 0
        for col in row:
            if col == "*":
                answer += get_gear_ratio({"x": x, "y": y})
            x += 1
        y += 1
    print(f"Answer: {answer}")


def part_1():
    input = []
    answer = 0
    with open('input1.txt', 'r') as file:
        input = file.readlines()

    def is_valid(points):
        for point in points:
            for x in range(point["x"] - 1, point["x"] + 2):
                for y in range(point["y"] - 1, point["y"] + 2):
                    print(f"{x} - {y}")
                    if 0 <= y < len(input):
                        if 0 <= x < len(input[y]) - 1:
                            if not input[y][x].isnumeric() and input[y][x] != "." and input[y][x] != "/n":
                                print(f"found {input[y][x]}")
                                return True

        return False

    x = 0
    y = 0
    for row in input:
        x = 0
        foundNumber = False
        tempNumber = ''
        tempPoints = []
        for col in row:
            if col.isnumeric():
                tempNumber += col
                foundNumber = True
                tempPoints.append({"x": x, "y": y})

            elif foundNumber:
                print(tempNumber)
                print(tempPoints)
                if is_valid(tempPoints):
                    answer += int(tempNumber)
                
                foundNumber = False
                tempNumber = ''
                tempPoints = []
                print("-----------------------")
            x +=1
        y += 1

    print(answer)


part_2()