import itertools
import functools

def GetNewPos(pos, incr):
    return (pos + incr - 1) % 10 + 1

def Part1():
    pos = [8, 3]
    scores = [0, 0]
    i = 1
    j = 0

    while scores[0] < 1000 and scores[1] < 1000:
        pos[j] = GetNewPos(pos[j], i * 3 + 3)
        scores[j] += pos[j]
        if scores[j] >= 1000:
            print(scores[(j + 1) % 2] * (i + 2))
            break

        i += 3
        j = (j + 1) % 2

@functools.lru_cache(maxsize=None)
def Play(pos1, score1, pos2, score2):
    count1 = 0
    count2 = 0

    for i, j, k in itertools.product((1, 2, 3), (1, 2, 3), (1, 2, 3)):
        newPos1 = GetNewPos(pos1, i + j + k)
        newScore1 = score1 + newPos1
        if newScore1 >= 21:
            count1 += 1
        else:
            newCount2, newCount1 = Play(pos2, score2, newPos1, newScore1)
            count1 += newCount1
            count2 += newCount2
    
    return count1, count2

def Part2():
    scores = Play(8, 0, 3, 0)
    print(max(scores[0], scores[1]))

def main():
    Part1()
    Part2()
main()
