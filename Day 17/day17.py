def Part1():
    targetAreaX = [85, 145]
    targetAreaY = [-108, -163]

    pos = [0, 0]
    velocityX = 0

    for i in range(20, 0, -1):
        if (i * (i + 1) // 2 <= targetAreaX[1]):
            velocityX = i
            break

    found = False
    for j in range(1000, 0, -1):
        if found:
            break

        maxYPos = 0
        velocityY = j
        currentVelocityX = velocityX
        currentVelocityY = velocityY
        initialPos = pos[:]

        while (True):
            pos[0] += currentVelocityX
            if (pos[0] > targetAreaX[1]):
                break

            if currentVelocityX >= 1:
                currentVelocityX -= 1

            if currentVelocityX == 0:
                if pos[1] < targetAreaY[1]:
                    break

            pos[1] += currentVelocityY
            currentVelocityY -= 1

            if pos[1] > maxYPos:
                maxYPos = pos[1]

            if pos[0] >= targetAreaX[0] and pos[0] <= targetAreaX[1] and pos[1] <= targetAreaY[0] and pos[1] >= targetAreaY[1]:
                print(maxYPos)
                found = True
                break
        
        pos = initialPos

def Part2():
    targetAreaX = [85, 145]
    targetAreaY = [-108, -163]

    pos = [0, 0]
    velocityX = 0

    count = 0

    for i in range(145, 0, -1):
        velocityX = i

        for j in range(1000, -1000, -1):
            velocityY = j
            currentVelocityX = velocityX
            currentVelocityY = velocityY
            initialPos = pos[:]

            while (True):
                pos[0] += currentVelocityX
                if (pos[0] > targetAreaX[1]):
                    break

                if currentVelocityX >= 1:
                    currentVelocityX -= 1

                if currentVelocityX == 0:
                    if pos[1] < targetAreaY[1]:
                        break

                pos[1] += currentVelocityY
                currentVelocityY -= 1

                if pos[0] >= targetAreaX[0] and pos[0] <= targetAreaX[1] and pos[1] <= targetAreaY[0] and pos[1] >= targetAreaY[1]:
                    count += 1
                    break
            
            pos = initialPos

    print(count)
        
def main():
    Part1()
    Part2()
main()
