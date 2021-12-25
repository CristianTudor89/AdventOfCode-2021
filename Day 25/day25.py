import sys
import copy

def GetNextPos(matrix, rows, cols, pos):
    nextPos = []

    if matrix[pos[0]][pos[1]] == '>':
        nextPos = [pos[0], pos[1] + 1]
        if nextPos[1] == cols:
            nextPos[1] = 0
    elif matrix[pos[0]][pos[1]] == 'v':
        nextPos = [pos[0] + 1, pos[1]]
        if nextPos[0] == rows:
            nextPos[0] = 0

    if matrix[nextPos[0]][nextPos[1]] == '.':
        return nextPos

    return pos

def Move(matrix, cucumber, rows, cols):
    moved = False
    copyMatrix = copy.deepcopy(matrix)

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == cucumber:
                nextPos = GetNextPos(matrix, rows, cols, [i, j])
                if nextPos != [i, j]:
                    moved = True
                    copyMatrix[nextPos[0]][nextPos[1]] = matrix[i][j]
                    copyMatrix[i][j] = '.'

    return [copyMatrix, moved]

def Solution():
    with open('day25.txt') as f:
        lines = f.readlines()

    matrix = []
    for line in lines:
        row = []
        for c in line[:-1]:
            row.append(c)
        matrix.append(row)

    rows = len(lines)
    cols = len(lines[0][:-1])

    step = 0
    while (True):
        step += 1

        [copyMatrix, moved1] = Move(matrix, '>', rows, cols)

        matrix = copy.deepcopy(copyMatrix)

        [copyMatrix, moved2] = Move(matrix, 'v', rows, cols)

        matrix = copy.deepcopy(copyMatrix)

        if moved1 == False and moved2 == False:
            break

    print(step)

def main():
    Solution()
main()
