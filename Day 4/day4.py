def Solution():
    with open('day4.txt') as f:
        lines = f.readlines()

    numbersStr = lines[0].split(',')
    numbersMap = map(int, numbersStr)
    numbers = list(numbersMap)

    matrices = []
    matrix = []

    for i in range(2, len(lines)):
        if (lines[i] == '\n'):
            continue

        rowStr = lines[i].split()
        rowMap = map(int, rowStr)
        row = list(rowMap)

        matrix.append(row)
        if (len(matrix) == 5):
            matrices.append(matrix)
            matrix = []

    boards = []
    for i in range(len(matrices)):
        board = [[0] * 5 for i in range(5)]
        boards.append(board)

    # Part 2
    indices = [0] * len(matrices)
    # ------------------------------------------
    
    for number in numbers:
        for i in range(len(matrices)):
            for j in range(5):
                for k in range(5):
                    if (matrices[i][j][k] == number):
                        boards[i][j][k] = 1

        for i in range(len(boards)):
            for j in range(5):
                count1 = 0
                for k in range(5):
                    if (boards[i][j][k] == 1):
                        count1 += 1
                
                count2 = 0
                for k in range(5):
                    if (boards[i][k][j] == 1):
                        count2 += 1

                if count1 == 5 or count2 == 5:
                    sum = 0
                    for m in range(5):
                        for l in range(5):
                            if (boards[i][m][l] == 0):
                                sum += matrices[i][m][l]
                    # Part 1
                    # print(sum * number)
                    # return

                    # Part 2
                    indices[i] = 1
                    finished = True
                    for index in indices:
                        if (index == 0):
                            finished = False
                    if finished:
                        print(sum * number)
                        return

def main():
    Solution()
main()
