def Solution():
    with open('day10.txt') as f:
        lines = f.readlines()

    closingChars = [')', ']', '}', '>']

    rev_matches = {
        ')': '(',
        ']': '[',
        '}': '{',
        '>': '<'
    }

    count = {
        ')': 0,
        ']': 0,
        '}': 0,
        '>': 0
    }

    points = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137
    }

    # Part 1
    linesToRemove = []

    for line in lines:
        chars = []
        for c in line:
            if c in closingChars:
                lastElem = chars[len(chars) - 1]
                if rev_matches[c] == lastElem:
                    chars.pop()
                else:
                    count[c] += 1
                    linesToRemove.append(line)
                    break
            else:
                chars.append(c)

    sum = 0
    for key, value in count.items():
        sum += points[key] * value

    print(sum)

    # Part 2
    for lineToRemove in linesToRemove:
        lines.remove(lineToRemove)

    matches = {
        '(': ')',
        '[': ']',
        '{': '}',
        '<': '>'
    }

    new_points = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4
    }

    scores = []

    for line in lines:
        chars = []
        score = 0
        for i in range(len(line) - 2, -1, -1):
            if len(chars) >= 1 and line[i] in matches and matches[line[i]] == chars[len(chars) - 1]:
                chars.pop()
            else:
                chars.append(line[i])

        for c in chars:
            score = score * 5 + new_points[matches[c]]
        scores.append(score)

    scores.sort()

    print(scores[int(len(scores) / 2)])

def main():
    Solution()
main()
