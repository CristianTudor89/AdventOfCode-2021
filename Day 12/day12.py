pathCount = 0

def TraversePart1(graph, visited, node):
    global pathCount

    neighbours = graph[node]

    for neighbour in neighbours:
        if neighbour == 'start':
            continue

        if neighbour == 'end':
            pathCount += 1
            continue

        if neighbour.islower() and neighbour in visited:
            continue
        
        newVisited = visited.copy()
        newVisited.append(neighbour)

        TraversePart1(graph, newVisited, neighbour)

def TraversePart2(graph, visited, node, smallCaveRepeatCount):
    global pathCount

    neighbours = graph[node]

    for neighbour in neighbours:
        if neighbour == 'start':
            continue

        if neighbour == 'end':
            pathCount += 1
            continue

        smallCaveRepeatCountCopy = smallCaveRepeatCount

        if neighbour.islower() and neighbour in visited:
            if smallCaveRepeatCount == 1:
                continue
            else:
                smallCaveRepeatCountCopy = 1
        
        newVisited = visited.copy()
        newVisited.append(neighbour)

        TraversePart2(graph, newVisited, neighbour, smallCaveRepeatCountCopy)

def Solution():
    global pathCount

    with open('day12.txt') as f:
        lines = f.readlines()
        
    graph = {}

    for line in lines:
        tokens = line.rstrip("\n").split('-')
        for i in range(2):
            if tokens[i] not in graph:
                graph[tokens[i]] = []

        graph[tokens[0]].append(tokens[1])
        graph[tokens[1]].append(tokens[0])

    # Part 1
    visited = ['start']
    TraversePart1(graph, visited, 'start')

    print(pathCount)
    pathCount = 0

    # Part 2
    smallCaveRepeatCount = 0
    TraversePart2(graph, visited, 'start', smallCaveRepeatCount)

    print(pathCount)

def main():
    Solution()
main()
