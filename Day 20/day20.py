import sys

def CopyMatrix(matrix):
    newRows = []
    for i in range(len(matrix)):
        newRows.append(matrix[i].copy())
    return newRows

def Solution():
    with open('day20.txt') as f:
        lines = f.readlines()

    algorithm = lines[0][:-1]

    inputImage = [['.'] * 500 for i in range(500)]

    posX = 200
    posY = 200

    # Part 1
    # step = 2

    step = 50

    for i in range(2, len(lines)):
        for j in range(len(lines[i]) - 1):
            inputImage[posX][posY] = lines[i][j]
            posY += 1
        posY = 200
        posX += 1

    outputImage = CopyMatrix(inputImage)
    posX = 200
    posY = 200
    rows = len(lines) - 2 
    cols = len(lines[2]) - 1
    offset = posX - 1
    
    for k in range(0, step):
        for i in range(posX - offset, posX + offset + rows):
            for j in range(posY - offset, posY + offset + cols):
                binaryStr = ''
                for k in range(i - 1, i + 2):
                    for l in range(j - 1, j + 2):
                        if inputImage[k][l] == '#':
                            binaryStr += '1'
                        else:
                            binaryStr += '0'
                binaryNumber = int(binaryStr, 2)
                
                outputImage[i][j] = algorithm[binaryNumber]

        inputImage = CopyMatrix(outputImage)
    
    count = 0
    for i in range(posX - 150, posX + rows + 151):
        for j in range(posY - 150, posY + cols + 151):
            if inputImage[i][j] == '#':
                count += 1

    print(count)

def main():
    Solution()
main()
