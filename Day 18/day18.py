import sys
import itertools

def Add(number1, number2):
    newNumber = '[' + number1 + ',' + number2 + ']'

    return Reduce(newNumber)

def Reduce(number):
    newNumber = number

    explodePos = GetExplodePos(number, 0)
    if explodePos != -1:
        newNumber = Explode(number, explodePos)

    if newNumber != number:
        return Reduce(newNumber)
    
    splitPos = GetSplitPos(number, 0)
    if splitPos != -1:
        newNumber = Split(number, splitPos)

    if newNumber != number:
        return Reduce(newNumber)
    
    return number

def GetExplodePos(number, pos):
    openBracketCount = 0

    while (pos < len(number)):
        if number[pos] == '[':
            openBracketCount += 1
        elif number[pos] == ']':
            openBracketCount -= 1

        if openBracketCount >= 5 and number[pos + 1].isdigit():
            newPos = pos + 2
            found = True
            foundComma = False

            while (newPos < len(number)):
                if number[newPos] == '[':
                    found = False
                    break

                if number[newPos] == ',':
                    foundComma = True

                if number[newPos].isdigit() and foundComma:
                    break

                newPos += 1

            if found:
                return pos

        pos += 1

    return -1

def GetSplitPos(number, pos):
    while (pos < len(number) - 1):
        if number[pos].isdigit() and number[pos + 1].isdigit():
            return pos
            
        pos += 1

    return -1

def GetNumberToTheLeftPos(number, pos):
    foundDigit = False

    while (pos >= 0):
        if number[pos].isdigit():
            foundDigit = True
        elif foundDigit:
            return pos + 1

        pos -= 1

    return -1

def GetNumberToTheRightPos(number, pos):
    closedBracket = False

    while (pos < len(number)):
        if number[pos] == ']':
            closedBracket = True
        
        if number[pos].isdigit() and closedBracket:
            return pos

        pos += 1

    return -1

def GetFirstNumberFromPos(number, pos):
    startPos = pos
    endPos = startPos

    while number[endPos].isdigit():
        endPos += 1

    return int(number[startPos : endPos])

def GetSecondNumberFromPos(number, pos):
    startPos = number.find(',', pos + 1) + 1
    endPos = startPos

    while number[endPos].isdigit():
        endPos += 1

    return int(number[startPos : endPos])

def GetClosingBracketPos(number, pos):
    while (pos < len(number)):
        if number[pos] == ']':
            return pos
        
        pos += 1

    return -1

def GetPosAfterNumber(number, pos):
    while (pos < len(number) and number[pos].isdigit()):
        pos += 1

    return pos

def Explode(number, explodePos):
    numberToTheLeftPos = GetNumberToTheLeftPos(number, explodePos)
    numberToTheRightPos = GetNumberToTheRightPos(number, explodePos)

    newNumber = number[0 : explodePos]

    if numberToTheLeftPos == -1:
        newNumber += '0,'
    else:
        numberToTheLeft = GetFirstNumberFromPos(number, numberToTheLeftPos)
        sum = GetFirstNumberFromPos(number, explodePos + 1) + numberToTheLeft

        if number[explodePos - 1] == ',':
            newNumber = number[0 : explodePos - 2]
            newNumber += str(sum) + ','
        else:
            newNumber = number[0 : numberToTheLeftPos]
            newNumber += str(sum) + number[numberToTheLeftPos + 1 : explodePos]
            newNumber += '0,'

    closingBracketPos = GetClosingBracketPos(number, explodePos)

    if numberToTheRightPos == -1:
        newNumber += '0' + number[closingBracketPos + 1 : ]
    else:
        numberToTheRight = GetFirstNumberFromPos(number, numberToTheRightPos)
        sum = GetSecondNumberFromPos(number, explodePos + 1) + numberToTheRight

        if number[closingBracketPos + 1] == ',':
            if number[closingBracketPos + 2].isdigit():
                posAfterNumber = GetPosAfterNumber(number, closingBracketPos + 2)
                newNumber += str(sum)
                newNumber += number[posAfterNumber : ]
            else:
                if numberToTheLeftPos == -1:
                    newNumber = number[0 : explodePos] + '0,'
                newNumber += number[closingBracketPos + 2 : numberToTheRightPos]
                newNumber += str(sum) + number[numberToTheRightPos + 1 : ]
        else:
            posAfterNumber = GetPosAfterNumber(number, numberToTheRightPos)
            newNumber += '0' + number[closingBracketPos + 1 : numberToTheRightPos]
            newNumber += str(sum) + number[posAfterNumber : ]

    return newNumber

def Split(number, splitPos):
    newNumber = number[0 : splitPos]
    intVal = int(number[splitPos : splitPos + 2])

    newNumber += '[' + str(intVal // 2) + ','

    if intVal % 2 == 1:
        newNumber += str(intVal // 2 + 1) + ']'
    else:
        newNumber += str(intVal // 2) + ']'

    newNumber += number[splitPos + 2 : ]

    return newNumber

def GetMagnitude(number):
    while (True):
        pair = GetFirstPair(number)
        if pair[0] == -1:
            break
        
        newNumber = number[pair[0] + 1 : pair[1]]
        values = newNumber.split(',')

        result = int(values[0]) * 3 + int(values[1]) * 2

        number = number[0 : pair[0]] + str(result) + number[pair[1] + 1 : ]

    return int(number)

def GetFirstPair(number):
    pos = 0
    while (pos < len(number)):
        if number[pos] == '[':
            found = False
            newPos = pos + 1
            while (newPos < len(number)):
                if number[newPos] == '[':
                    break

                if number[newPos] == ']':
                    found = True
                    break

                newPos += 1
            
            if found:
                return [pos, newPos]
        
        pos += 1
    
    return [-1, -1]

def Part1():
    with open('day18.txt') as f:
        numbers = f.readlines()

    currentNumber = numbers[0][:-1]

    for i in range(1, len(numbers)):
        currentNumber = Add(currentNumber, numbers[i][:-1])

    magnitude = GetMagnitude(currentNumber)

    print(magnitude)

def Part2():
    with open('day18.txt') as f:
        numbers = f.readlines()

    magnitudes = set()
    pairs = list(itertools.permutations(numbers, 2))

    for number1, number2 in pairs:
        sum = Add(number1[:-1], number2[:-1])
        magnitudes.add(GetMagnitude(sum))

    print(max(magnitudes))

def main():
    # Part1()
    Part2()
main()
