def Solution():
    with open('day14.txt') as f:
        lines = f.readlines()

    template = lines[0][:-1]
    dict = {}

    for i in range(2, len(lines)):
        pair = lines[i][:-1].split(' -> ')
        dict[pair[0]] = pair[1]

    polymer = template[:]

    for i in range(18):
        values = []
        for j in range(len(polymer) - 1):
            key = polymer[j : j + 2]
            value = dict[key]
            if j == len(polymer) - 2:
                values.append(polymer[j] + value + polymer[j + 1])
            else:
                values.append(polymer[j] + value)

        polymer = ''
        for value in values:
            polymer += value

        frequencies = {}
        for i in polymer:
            if i in frequencies:
                frequencies[i] += 1
            else:
                frequencies[i] = 1

        maxVal = max(frequencies.values())
        minVal = min(frequencies.values())

        print(maxVal, minVal, maxVal - minVal)
    
    # frequencies = {}
    # for i in polymer:
    #     if i in frequencies:
    #         frequencies[i] += 1
    #     else:
    #         frequencies[i] = 1
    
    # maxVal = max(frequencies.values())
    # minVal = min(frequencies.values())

    # print(maxVal - minVal)

def main():
    Solution()
main()
