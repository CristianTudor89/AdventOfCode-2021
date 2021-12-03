def listToString(ints): 
    return ''.join([str(int) for int in ints])

def Part1():
    with open('day3.txt') as f:
        lines = f.readlines()

    size = len(lines[0]) - 1

    gamma = [None] * size
    epsilon = [None] * size

    for i in range(size):
        count_0 = 0
        count_1 = 0
        for line in lines:
            if line[i] == '0':
                count_0 += 1
            else:
                count_1 += 1

        if count_0 > count_1:
            gamma[i] = 0
            epsilon[i] = 1
        else:
            gamma[i] = 1
            epsilon[i] = 0

    gammaStr = listToString(gamma)
    epsilonStr = listToString(epsilon)

    gammaNr = int(gammaStr, 2)
    epsilonNr = int(epsilonStr, 2)

    print(gammaNr * epsilonNr)
        
def Part2():
    with open('day3.txt') as f:
        lines = f.readlines()

    size = len(lines[0]) - 1

    oxygenRatings = lines.copy()
    scrubberRatings = lines.copy()

    for i in range(size):
        if (len(oxygenRatings) == 1 and len(scrubberRatings) == 1):
            break;

        count_0 = 0
        count_1 = 0
        for line in oxygenRatings:
            if line[i] == '0':
                count_0 += 1
            else:
                count_1 += 1

        oxygenCopy = oxygenRatings.copy()

        if (len(oxygenRatings) > 1): 
            if count_0 > count_1:
                for line in oxygenCopy:
                    if (line[i] == '1'):
                        oxygenRatings.remove(line)
            else:
                for line in oxygenCopy:
                    if (line[i] == '0'):
                        oxygenRatings.remove(line)

        count_0 = 0
        count_1 = 0
        for line in scrubberRatings:
            if line[i] == '0':
                count_0 += 1
            else:
                count_1 += 1

        scrubberCopy = scrubberRatings.copy()

        if (len(scrubberRatings) > 1):
            if count_1 >= count_0:
                for line in scrubberCopy:
                    if (line[i] == '1'):
                        scrubberRatings.remove(line)
            else:
                for line in scrubberCopy:
                    if (line[i] == '0'):
                        scrubberRatings.remove(line)

    gammaStr = listToString(oxygenRatings[0])
    epsilonStr = listToString(scrubberRatings[0])

    gammaNr = int(gammaStr, 2)
    epsilonNr = int(epsilonStr, 2)

    print(gammaNr * epsilonNr)

def main():
    # Part1()
    Part2()
main()
