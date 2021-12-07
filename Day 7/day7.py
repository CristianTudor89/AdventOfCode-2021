def Solution():
    with open('day7.txt') as f:
        line = f.readline()

    ints = [int(i) for i in line.split(',')]

    min = 1000000000
    for i in range(len(ints)):
        sum = 0
        for val in ints:
            # Part 1
            # sum += abs(val - i)
            # Part 2
            sum += (abs(val - i) * (abs(val - i) + 1)) / 2
        if (sum < min):
            min = sum

    print(min)

def main():
    Solution()
main()
