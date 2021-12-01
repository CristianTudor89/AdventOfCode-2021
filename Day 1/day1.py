def main():
    with open('day1.txt') as f:
        lines = f.readlines()
    
    count = 0

    # Part 1
    value = int(lines[0])
    for i in range(0, len(lines) - 1):
        if int(lines[i + 1]) > int(lines[i]):
            count += 1

    print(count)

    # Part 2
    count = 0
    
    for i in range(0, len(lines) - 3):
        val1 = int(lines[i]) + int(lines[i + 1]) + int(lines[i + 2])
        val2 = int(lines[i + 1]) + int(lines[i + 2]) + int(lines[i + 3])
        if val2 > val1:
            count += 1

    print(count)
main()
