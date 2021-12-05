def Solution():
    with open('day5.txt') as f:
        lines = f.readlines()

    rowCount = 0
    colCount = 0

    for line in lines:
        pairs = line.split(' -> ')
        pair1 = [int(i) for i in pairs[0].split(',')]
        pair2 = [int(i) for i in pairs[1].split(',')]

        if pair1[0] > colCount:
            colCount = pair1[0]
        if pair2[0] > colCount:
            colCount = pair2[0]

        if pair1[1] > rowCount:
            rowCount = pair1[1]
        if pair2[1] > rowCount:
            rowCount = pair2[1]

    rowCount += 1
    colCount += 1
    matrix = [[0] * colCount for i in range(rowCount)]

    for line in lines:
        pairs = line.split(' -> ')
        pair1 = [int(i) for i in pairs[0].split(',')]
        pair2 = [int(i) for i in pairs[1].split(',')]

        # Part 1
        # if (pair1[0] != pair2[0]) and (pair1[1] != pair2[1]):
        #     continue

        # Part 2
        if (pair1[0] != pair2[0]) and (pair1[1] != pair2[1]):
            if abs(pair1[0] - pair2[0]) != abs(pair1[1] - pair2[1]):
                continue
        # -------------------------------------------------------------

        if pair1[0] == pair2[0]:
            for i in range(min(pair1[1], pair2[1]), max(pair1[1], pair2[1]) + 1):
                matrix[i][pair1[0]] += 1
        elif pair1[1] == pair2[1]:
            for i in range(min(pair1[0], pair2[0]), max(pair1[0], pair2[0]) + 1):
                matrix[pair1[1]][i] += 1
        # Part 2
        else:
            x = pair1[1]
            y = pair1[0]

            for i in range(abs(pair1[0] - pair2[0]) + 1):
                matrix[x][y] += 1

                if x < pair2[1]:
                    x += 1
                else:
                    x -= 1

                if y < pair2[0]:
                    y += 1
                else:
                    y -= 1

    count = 0
    for i in range(rowCount):
        for j in range(colCount):
            if matrix[i][j] > 1:
                count += 1
    print(count)

def main():
    Solution()
main()
