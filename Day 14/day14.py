def GetNewPolymer(polymer, dict):
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

    return polymer

def Part1():
    with open('day14.txt') as f:
        lines = f.readlines()

    template = lines[0][:-1]
    dict = {}

    for i in range(2, len(lines)):
        pair = lines[i][:-1].split(' -> ')
        dict[pair[0]] = pair[1]

    polymer = template[:]
    
    for i in range(10):
        polymer = GetNewPolymer(polymer, dict)
    
    frequencies = {}
    for i in polymer:
        if i in frequencies:
            frequencies[i] += 1
        else:
            frequencies[i] = 1
    
    maxVal = max(frequencies.values())
    minVal = min(frequencies.values())

    print(maxVal - minVal)

def Part2():
    with open('day14.txt') as f:
        lines = f.readlines()

    template = lines[0][:-1]
    dict = {}

    for i in range(2, len(lines)):
        pair = lines[i][:-1].split(' -> ')
        dict[pair[0]] = pair[1]

    polymer = template[:]

    pairs = {}
    frequencies = {}

    for i in range(len(polymer) - 1):
        key = polymer[i : i + 2]
        if not key in pairs:
            pairs[key] = 1
        else:
            pairs[key] += 1
    
    for i in range(40):
        newPairs = {}

        for key in pairs.keys():
            value = dict[key]

            key1 = key[0] + value
            key2 = value + key[1]

            if not key1 in newPairs:
                newPairs[key1] = pairs[key]
            else:
                newPairs[key1] = newPairs[key1] + pairs[key]

            if not key2 in newPairs:
                newPairs[key2] = pairs[key]
            else:
                newPairs[key2] = newPairs[key2] + pairs[key]

        pairs = newPairs

    for key in pairs.keys():
        for j in key:
            if j in frequencies:
                frequencies[j] += pairs[key]
            else:
                frequencies[j] = pairs[key]

    maxVal = max(frequencies.values())
    minVal = min(frequencies.values())

    print((maxVal - minVal) // 2 + 1)

def main():
    Part1()
    Part2()
main()
