import heapq

def GetMatrix(lines):
    rows = []
    for line in lines:
        line = line[:-1]
        rows.append([int(i) for i in line])

    return rows

class PriorityQueue:
    def __init__(self):
        self.values = []

    def empty(self):
        return not self.values

    def push(self, value, priority):
        heapq.heappush(self.values, [priority, value])

    def pop(self):
        return heapq.heappop(self.values)[1]

def GetNeighbours(rows, cols, pos):
    dirX = [-1, 0, 1]
    dirY = [-1, 0, 1]
    neighbours = []

    for k in dirX:
        for l in dirY:
            if (k != 0 and l != 0):
                continue

            newPos = [pos[0] + k, pos[1] + l]
            if newPos == pos:
                continue

            if (newPos[0] < 0 or newPos[0] >= rows):
                continue

            if (newPos[1] < 0 or newPos[1] >= cols):
                continue

            neighbours.append(newPos)
    
    return neighbours

def GetCost(matrix, tileWidth, tileHeight, i, j, partTwo):
    if not partTwo:
        return matrix[i][j]

    value = matrix[i % tileWidth][j % tileHeight] + i // tileWidth + j // tileHeight
    if value > 9:
        value = value % 9

    return value

def Dijkstra(matrix, tileWidth, tileHeight, rows, cols, partTwo):
    costMatrix = [[1_000_000] * cols for i in range(rows)]
 
    queue = PriorityQueue()
    queue.push([0, 0], 0)

    costMatrix[0][0] = 0

    while not queue.empty():
        currentNode = queue.pop()
        if currentNode == [rows - 1, cols - 1]:
            print(costMatrix[rows - 1][cols - 1])
            break

        neighbours = GetNeighbours(rows, cols, currentNode)
        for neighbour in neighbours:
            neighbourCost = GetCost(matrix, tileWidth, tileHeight, neighbour[0], neighbour[1], partTwo)
            cost = costMatrix[currentNode[0]][currentNode[1]] + neighbourCost

            if costMatrix[neighbour[0]][neighbour[1]] == 1_000_000 or cost < costMatrix[neighbour[0]][neighbour[1]]:
                costMatrix[neighbour[0]][neighbour[1]] = cost
                queue.push(neighbour, cost)

def Solution(partTwo):
    with open('day15.txt') as f:
        lines = f.readlines()
    
    matrix = GetMatrix(lines)

    tileWidth = rows = len(matrix)
    tileHeight = cols = len(matrix[0])

    if partTwo:
        rows *= 5
        cols *= 5

    Dijkstra(matrix, tileWidth, tileHeight, rows, cols, partTwo)

def main():
    Solution(False)
    Solution(True)
main()
