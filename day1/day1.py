import re

help_2 = [
   "one",
   "two",
   "three",
   "four",
   "five",
   "six",
   "seven",
   "eight",
   "nine",
   "zero"
   ]

help_dict = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
    'zero': '0'
}

inputString = open("inputPart2.txt", "r").read()

def get_number(word, reversed):
    temp = ""
    for c in word:
        for n in help_2:
            x = re.findall(n, temp)
            if len(x) > 0:
                return ''.join(help_dict[ele] for ele in x[0].split())
        if reversed:
            temp = c + temp
        else:
            temp += c
        if c.isnumeric():
            return c
    return None
input = inputString.split()
answer = 0
for i in input:
    calValue = get_number(i, False) + get_number(i[::-1], True)
    answer += int(calValue)
print(answer)