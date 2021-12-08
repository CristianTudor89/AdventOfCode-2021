def Solution():
    with open('day8.txt') as f:
        lines = f.readlines()

    # Part 1
    # 1, 4, 7, 8
    segments = [2, 4, 3, 7]
    count = 0

    for line in lines:
        parts = line.split('|')
        digits = parts[1].split()
        for digit in digits:
            for j in segments:
                if len(digit) == j:
                    count += 1
                    break
    print(count)

    # Part 2
    # 1, 4, 7, 8
    segments = [2, 4, 3, 7]
    sum = 0
    for line in lines:
        dict = {}
        parts = line.split('|')
        digits = parts[0].split()
        for digit in digits:
            for j in segments:
                if len(digit) == j:
                    if j == 2:
                        dict[1] = digit
                    elif j == 4:
                        dict[4] = digit
                    elif j == 3:
                        dict[7] = digit
                    else:
                        dict[8] = digit
                    break
        
        for digit in digits:
            if len(digit) == 6:
                if (digit.find(dict[1][0]) == -1 or digit.find(dict[1][1]) == -1):
                    dict[6] = digit
                    break

        for digit in digits:
            if len(digit) == 6:
                if dict[6] == digit:
                    continue

                for j in dict[4]:
                    if digit.find(j) == -1:
                        dict[0] = digit
                        break

        for digit in digits:
            if len(digit) == 6:
                if (dict[6] == digit or dict[0] == digit):
                    continue

                dict[9] = digit
                break
        
        for digit in digits:
            if len(digit) == 5:
                if (digit.find(dict[1][0]) != -1 and digit.find(dict[1][1]) != -1):
                    dict[3] = digit
                    break

        for digit in digits:
            if len(digit) == 5:
                count = 0
                for i in digit:
                    if dict[6].find(i) == -1:
                        count += 1
                if count == 0:
                    dict[5] = digit
                    break

        for digit in digits:
            found = False
            for i in range(10):
                if i != 2 and dict[i] == digit:
                    found = True
            if found == False:
                dict[2] = digit
                break
    
        digits1 = parts[1].split() 
        nr = 0
        for digit1 in digits1:
            str = sorted(digit1)
            for i in range(10):
                str1 = sorted(dict[i])
                if str == str1:
                    nr = nr * 10 + i
            
        sum += nr

    print(sum)
    
def main():
    Solution()
main()
