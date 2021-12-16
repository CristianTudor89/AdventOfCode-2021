import sys

def GetNewValue(type, values):
    sum = 0
    product = 1
    for value in values:
        sum += value
        product *= value

    if type == 0:
        return sum
    elif type == 1:
        return product
    elif type == 2:
        return min(values)
    elif type == 3:
        return max(values)
    elif type == 5:
        return values[0] > values[1]
    elif type == 6:
        return values[0] == values[1]
    elif type == 7:
        return values[0] < values[1]

def DecodeExpression(binaryStr, versionSum, pos):
    version = int(binaryStr[pos : pos + 3], 2)
    type = int(binaryStr[pos + 3: pos + 6], 2)

    versionSum += version

    if type == 4:
        currentPos = pos + 6
        number = ''
        while currentPos < len(binaryStr):
            number += binaryStr[currentPos + 1 : currentPos + 5]
            if binaryStr[currentPos] == '0':
                currentPos += 5
                break
            else:
                currentPos += 5

        return [versionSum, int(number, 2), currentPos]
        
    else:
        lengthTypeId = binaryStr[pos + 6]

        if lengthTypeId == '0':
            length = int(binaryStr[pos + 7 : pos + 22], 2)
            currentPos = pos + 22
            end = currentPos + length

            values = []
            while (currentPos < end):
                [versionSum, value, newPos] = DecodeExpression(binaryStr, versionSum, currentPos)
                values.append(value)
                currentPos = newPos
            
            newValue = GetNewValue(type, values)

            return [versionSum, newValue, currentPos]
                
        elif lengthTypeId == '1':
            length = int(binaryStr[pos + 7: pos + 18], 2)
            currentPos = pos + 18

            values = []
            for i in range(length):
                [versionSum, value, newPos] = DecodeExpression(binaryStr, versionSum, currentPos)
                values.append(value)
                currentPos = newPos

            newValue = GetNewValue(type, values)

            return [versionSum, newValue, currentPos]

def Solution():
    with open('day16.txt') as f:
        packet = f.read()[:-1]

    hexToBinary = {
        '0': '0000',
        '1': '0001',
        '2': '0010',
        '3': '0011',
        '4': '0100',
        '5': '0101',
        '6': '0110',
        '7': '0111',
        '8': '1000',
        '9': '1001',
        'A': '1010',
        'B': '1011',
        'C': '1100',
        'D': '1101',
        'E': '1110',
        'F': '1111'
    }

    binaryStr = ''
    for i in packet:
        binaryStr += hexToBinary[i]

    [versionSum, value, pos] = DecodeExpression(binaryStr, 0, 0)

    print(versionSum)
    print(value)

def main():
    Solution()
main()
