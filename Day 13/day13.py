class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

def Solution():
    with open('day13.txt') as f:
        lines = f.readlines()

    points = []
    splitPoints = []

    for line in lines:
        if line == '\n':
            continue

        point = line[:-1].split(',')
        if len(point) == 2:
            points.append(Point(int(point[1]), int(point[0])))
        else:
            tokens = line[:-1].split()
            vals = tokens[2].split('=')
            if (vals[0] == 'x'):
                splitPoints.append(Point(0, int(vals[1])))
            else:
                splitPoints.append(Point(int(vals[1]), 0))

    new_points = points.copy()

    for splitPoint in splitPoints:
        pointsToRemove = []

        if splitPoint.x == 0:
            for point in points:
                if point.y > splitPoint.y:
                    diff = point.y - splitPoint.y
                    new_point = Point(point.x, splitPoint.y - diff)
                    if not new_point in new_points:
                        new_points.append(new_point)
                    pointsToRemove.append(point)
        elif splitPoint.y == 0:
            for point in points:
                if point.x > splitPoint.x:
                    diff = point.x - splitPoint.x
                    new_point = Point(splitPoint.x - diff, point.y)
                    if not new_point in new_points:
                        new_points.append(new_point)
                    pointsToRemove.append(point)

        for point in pointsToRemove:
            new_points.remove(point)

        # Part 1
        # print(len(new_points))
        # break

        # Part 2
        points = new_points.copy()

    # Part 2
    maxX = 0
    maxY = 0

    for point in points:
        if point.x > maxX:
            maxX = point.x
        if point.y > maxY:
            maxY = point.y

    matrix = [[''] * (maxY + 1) for i in range(maxX + 1)]

    for i in range(maxX + 1):
        for j in range(maxY + 1):
            if (Point(i, j) in points):
                matrix[i][j] = '1'
            else:
                matrix[i][j] = ' '

    for i in range(maxX + 1):
        print(*matrix[i])

def main():
    Solution()
main()
