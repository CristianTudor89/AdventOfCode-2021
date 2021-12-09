def GetMatrix(lines):
    rows = []
    for line in lines:
        line = line[:-1]
        rows.append([int(i) for i in line])

    return rows

def IsLowestPoint(lines, i, j):
    found = True

    if (i < len(lines) - 1) and lines[i][j] >= lines[i + 1][j]:
        found = False
    if (i > 0) and lines[i][j] >= lines[i - 1][j]:
        found = False
    if (j < len(lines[i]) - 1) and lines[i][j] >= lines[i][j + 1]:
        found = False
    if (j > 0) and lines[i][j] >= lines[i][j - 1]:
        found = False
    
    return found

def GetBasinSize(visited, lines, i, j):
    size = 1

    if i < len(lines) - 1 and lines[i + 1][j] != 9 and [i + 1, j] not in visited:
        visited.append([i + 1, j])
        size += GetBasinSize(visited, lines, i + 1, j)

    if i > 0 and lines[i - 1][j] != 9 and [i - 1, j] not in visited:
        visited.append([i - 1, j])
        size += GetBasinSize(visited, lines, i - 1, j)

    if j < len(lines[i]) - 1 and lines[i][j + 1] != 9 and [i, j + 1] not in visited:
        visited.append([i, j + 1])
        size += GetBasinSize(visited, lines, i, j + 1)

    if j > 0 and lines[i][j - 1] != 9 and [i, j - 1] not in visited:
        visited.append([i, j - 1])
        size += GetBasinSize(visited, lines, i, j - 1)

    return size

def Solution():
    with open('day9.txt') as f:
        lines = f.readlines()

    lines = GetMatrix(lines)

    points = []
    basins = []

    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if IsLowestPoint(lines, i, j):
                points.append(lines[i][j])
                visited = [[i, j]]
                basins.append(GetBasinSize(visited, lines, i, j))

    # Part 1
    print(sum(points) + len(points))
    
    # Part 2
    basins.sort()
    prod = 1
    for i in range(len(basins) - 3, len(basins)):
        prod *= basins[i]
    print(prod)

def main():
    Solution()
main()
