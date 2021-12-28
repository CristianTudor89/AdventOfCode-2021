import sys

def Solution():
    with open('day24.txt') as f:
        lines = f.readlines()

    """
    x = (z % 26 + b) != w
    y = (w + c) * x
    z = (z / a) * ((25 * x + 1) + y)

    1) a = 1

        x = (z % 26 + b) != w
        y = (w + c) * x
        z = z * ((25 * x + 1) + y)

        c > 0, w > 0, x = 0 or 1 => y >= 0 => z > 0

        b > 0 when a = 1
        z > 0 => z % 26 > 0 => (z % 26 + b) >= 10
        w = [1, 9] => x = 1

        x = 1
        y = w + c
        z = 26 + y => z = 26 + w + c

    2) a = 26

        x = (z % 26 + b) != w
        y = (w + c) * x
        z = (z / 26) * ((25  * x + 1) + y)

        c > 0, w > 0, x = 0 or 1 => y >= 0 => z > 0

        b < 0 when a = 26

        - x = 0:

            z = (z / 26) * (y + 1)

            y = (w + c) * x => y = 0

            w = [1, 9]
            c = [1, 15]

            z = z / 26

        - x = 1:

            z = (z / 26) * (y + 26)

            y = (w + c) * x = w + c => z = z / 26 * (w + c)

        z = z / 26

        x = 0 => z % 26 + b = w

        w_old + c_old = w_new - b_new
    """

    b_dict = {}
    c_dict = {}

    a = [1, 1, 1, 1, 26, 26, 1, 1, 26, 26, 1, 26, 26, 26]
    b = [10, 11, 14, 13, -6, -14, 14, 13, -8, -15, 10, -11, -13, -4]
    c = [1, 9, 12, 6, 9, 15, 7, 12, 15, 3, 6, 2, 10, 12]

    index = 0
    for i in range(14):
        if a[i] == 1:
            c_dict[index] = i
            index += 1
        elif a[i] == 26:
            b_dict[b[i]] = i

    perm_c = [1, 9, 12, 6, 7, 12, 6]
    perm_b = [-4, -13, -14, -6, -15, -8, -11]

    # Part 1
    w = [0] * 14
    for i in range(7):
        b_index = b_dict[perm_b[i]]
        c_index = c_dict[i]

        if perm_b[i] + perm_c[i] >= 0:
            w[b_index] = 9
            w[c_index] = 9 - (perm_b[i] + perm_c[i])
        else:
            w[c_index] = 9
            w[b_index] = 9 - abs(perm_b[i] + perm_c[i])

        if i == 6:
            numberStr = "".join([str(x) for x in w])
            print(int(numberStr))

    # Part 2
    w = [0] * 14
    for i in range(7):
        b_index = b_dict[perm_b[i]]
        c_index = c_dict[i]

        if perm_b[i] + perm_c[i] >= 0:
            w[b_index] = 1 + perm_b[i] + perm_c[i]
            w[c_index] = 1
        else:
            w[c_index] = 1 + abs(perm_b[i] + perm_c[i])
            w[b_index] = 1

        if i == 6:
            numberStr = "".join([str(x) for x in w])
            print(int(numberStr))
            
def main():
    Solution()
main()
