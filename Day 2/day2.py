def Part1():
    with open('day2.txt') as f:
        lines = f.readlines()
    x = 0
    y = 0

    for line in lines:
        tokens = line.split(' ')
        if tokens[0] == 'forward':
            x += int(tokens[1])
        elif tokens[0] == 'down':
            y += int(tokens[1])
        elif tokens[0] == 'up':
            y -= int(tokens[1])

    print(x * y)

def Part2():
    with open('day2.txt') as f:
        lines = f.readlines()
    x = 0
    y = 0
    aim = 0

    for line in lines:
        tokens = line.split(' ')
        if tokens[0] == 'forward':
            x += int(tokens[1])
            y += aim * int(tokens[1])
        elif tokens[0] == 'down':
            aim += int(tokens[1])
        elif tokens[0] == 'up':
            aim -= int(tokens[1])

    print(x * y)

def main():
    # Part1()
    Part2()
main()

