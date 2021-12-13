def Solution():
    with open('day13.txt') as f:
        lines = f.readlines()

    points = []
    splitPoints = []

    for line in lines:
        point = line[:-1].split(',')
        if len(point) == 2:
            points.append([int(point[1]), int(point[0])])
        elif line == '\n':
            continue
        else:
            vals = line[:-1].split()
            vals1 = vals[2].split('=')
            if (vals1[0] == 'x'):
                splitPoints.append([0, int(vals1[1])])
            else:
                splitPoints.append([int(vals1[1]), 0])

    new_points = points[:]

    for splitPoint in splitPoints:
        pointsToRemove = []

        if splitPoint[0] == 0:
            for point in points:
                if point[1] > splitPoint[1]:
                    diff = point[1] - splitPoint[1]
                    new_point = [point[0], splitPoint[1] - diff]
                    if not new_point in new_points:
                        new_points.append(new_point)
                    pointsToRemove.append(point)
        elif splitPoint[1] == 0:
            for point in points:
                if point[0] > splitPoint[0]:
                    diff = point[0] - splitPoint[0]
                    new_point = [splitPoint[0] - diff, point[1]]
                    if not new_point in new_points:
                        new_points.append(new_point)
                    pointsToRemove.append(point)

        for point in pointsToRemove:
            new_points.remove(point)

        # Part 1
        # print(len(new_points))
        # break

        # Part 2
        points = new_points

    # Part 2
    maxX = 0
    maxY = 0

    for point in points:
        if point[0] > maxX:
            maxX = point[0]
        if point[1] > maxY:
            maxY = point[1]

    matrix = [[''] * (maxY + 1) for i in range(maxX + 1)]

    for i in range(maxX + 1):
        for j in range(maxY + 1):
            if ([i, j] in points):
                matrix[i][j] = '1'
            else:
                matrix[i][j] = ' '

    for i in range(maxX + 1):
        print(*matrix[i])

def main():
    Solution()
main()
