def GetMatrix(lines):
    rows = []
    for line in lines:
        line = line[:-1]
        rows.append([int(i) for i in line])

    return rows

def GetNeighbours(lines, rows, cols, pos):
    dirX = [-1, 0, 1]
    dirY = [-1, 0, 1]
    neighbours = []

    for k in dirX:
        for l in dirY:
            newPos = [pos[0] + k, pos[1] + l]
            if newPos == pos:
                continue

            if (newPos[0] < 0 or newPos[0] >= rows):
                continue

            if (newPos[1] < 0 or newPos[1] >= cols):
                continue

            if (lines[newPos[0]][newPos[1]] == 0):
                continue

            neighbours.append(newPos)
    
    return neighbours

def Step(lines, rows, cols):
    flashCount = 0

    indices = []
    for i in range(rows):
        for j in range(cols):
            if lines[i][j] < 9:
                lines[i][j] += 1
            else:
                lines[i][j] = 0
                indices.append([i, j])
                flashCount += 1

    while (len(indices) > 0):
        newIndices = []
        for i in range(len(indices)):
            neighbours = GetNeighbours(lines, rows, cols, indices[i])
            for neighbour in neighbours:
                if lines[neighbour[0]][neighbour[1]] < 9:
                    lines[neighbour[0]][neighbour[1]] += 1
                else:
                    lines[neighbour[0]][neighbour[1]] = 0
                    newIndices.append([neighbour[0], neighbour[1]])
                    flashCount += 1
        indices = newIndices
    
    return flashCount

def Part1():
    with open('day11.txt') as f:
        lines = f.readlines()

    lines = GetMatrix(lines)
    rows = len(lines)
    cols = len(lines[0])
    flashes = 0
    steps = 100
    
    for step in range(steps):
        flashes += Step(lines, rows, cols)

    print(flashes)

def Part2():
    with open('day11.txt') as f:
        lines = f.readlines()

    lines = GetMatrix(lines)
    rows = len(lines)
    cols = len(lines[0])
    flashes = 0
    step = 0

    while (True):
        step += 1
        flashes += Step(lines, rows, cols)

        found = True
        for i in range(rows):
            for j in range(cols):
                if lines[i][j] != 0:
                    found = False
                    i = rows
                    break
        if found:
            print(step)
            break
        
def main():
    Part1()
    Part2()
main()
