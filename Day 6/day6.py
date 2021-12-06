def Part1():
    with open('day6.txt') as f:
        line = f.readline()

    lanternfish = [int(i) for i in line.split(',')]

    for i in range(80):
        count = 0
        for j in range(len(lanternfish)):
            if lanternfish[j] >= 1:
                lanternfish[j] -= 1
            else:
                lanternfish[j] = 6
                count += 1
        for j in range(count):
            lanternfish.append(8)

    print(len(lanternfish))

def Part2():
    with open('day6.txt') as f:
        line = f.readline()

    lanternfish = [int(i) for i in line.split(',')]

    count = [0] * 9
    for i in range(len(lanternfish)):
        count[lanternfish[i]] += 1

    for i in range(256):
        buffer = count[0]
        for j in range(8):
            count[j] = count[j + 1]
        count[6] += buffer
        count[8] = buffer
    
    sum = 0
    for i in range(len(count)):
        sum += count[i]

    print(sum)
        
def main():
    # Part1()
    Part2()
main()
