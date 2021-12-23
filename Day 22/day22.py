import sys
import copy

def Part1():
    
    with open('day22.txt') as f:
        lines = f.readlines()

    dict = {}

    for i in range(-50, 51):
        for j in range(-50, 51):
            for k in range(-50, 51):
                dict[(i, j, k)] = 0

    for line in lines:
        tokens = line.split()
        on = (tokens[0] == 'on')
        coords = tokens[1].split(',')
        xrange = []
        yrange = []
        zrange = []
        for coord in coords:
            if coord.startswith('x='):
                xcoords = coord[2:].split('..')
                xrange = [int(xcoords[0]), int(xcoords[1])]
            elif coord.startswith('y='):
                ycoords = coord[2:].split('..')
                yrange = [int(ycoords[0]), int(ycoords[1])]
            elif coord.startswith('z='):
                zcoords = coord[2:].split('..')
                zrange = [int(zcoords[0]), int(zcoords[1])]

        if xrange[0] < -50:
            xrange[0] = -50

        if xrange[1] > 50:
            xrange[1] = 50

        if yrange[0] < -50:
            yrange[0] = -50

        if yrange[1] > 50:
            yrange[1] = 50

        if zrange[0] < -50:
            zrange[0] = -50

        if zrange[1] > 50:
            zrange[1] = 50

        for i in range(xrange[0], xrange[1] + 1):
            for j in range(yrange[0], yrange[1] + 1):
                for k in range(zrange[0], zrange[1] + 1):
                    if on == True:
                        dict[(i, j, k)] = 1
                    else:
                        dict[(i, j, k)] = 0
    count = 0
    
    for i in range(-50, 51):
        for j in range(-50, 51):
            for k in range(-50, 51):
                if dict[(i, j, k)] == 1:
                    count += 1

    print(count)

def Intersects(cuboid1, cuboid2):
    cuboid1Left = cuboid1[0][0]
    cuboid1Right = cuboid1[0][1]
    cuboid1Bottom = cuboid1[1][0]
    cuboid1Top = cuboid1[1][1]
    cuboid1Back = cuboid1[2][0]
    cuboid1Front = cuboid1[2][1]

    cuboid2Left = cuboid2[0][0]
    cuboid2Right = cuboid2[0][1]
    cuboid2Bottom = cuboid2[1][0]
    cuboid2Top = cuboid2[1][1]
    cuboid2Back = cuboid2[2][0]
    cuboid2Front = cuboid2[2][1]
    
    intersectsOnX = (cuboid2Left >= cuboid1Left and cuboid2Left <= cuboid1Right) or (cuboid2Left < cuboid1Left and cuboid2Right >= cuboid1Left)
    intersectsOnY = (cuboid2Bottom >= cuboid1Bottom and cuboid2Bottom <= cuboid1Top) or (cuboid2Bottom < cuboid1Bottom and cuboid2Top >= cuboid1Bottom)
    intersectsOnZ = (cuboid2Back >= cuboid1Back and cuboid2Back <= cuboid1Front) or (cuboid2Back < cuboid1Back and cuboid2Front >= cuboid1Back)

    return intersectsOnX and intersectsOnY and intersectsOnZ

def GetNewCuboids(existingCuboid, currentCuboid):
    newCuboids = []

    for i in range(3):
        if existingCuboid[i][0] < currentCuboid[i][0]:
            cuboidToAdd = copy.deepcopy(existingCuboid)
            cuboidToAdd[i][1] = currentCuboid[i][0] - 1
            existingCuboid[i][0] = currentCuboid[i][0]
            newCuboids.append(cuboidToAdd)
        
        if existingCuboid[i][1] > currentCuboid[i][1]:
            cuboidToAdd = copy.deepcopy(existingCuboid)
            cuboidToAdd[i][0] = currentCuboid[i][1] + 1
            existingCuboid[i][1] = currentCuboid[i][1]
            newCuboids.append(cuboidToAdd)

    return newCuboids

def UpdateCuboids(cuboids, currentCuboid):
    newCuboids = []

    for cuboid in cuboids:
        if Intersects(cuboid, currentCuboid):
            newCuboids1 = GetNewCuboids(cuboid, currentCuboid)
            for newCuboid in newCuboids1:
                newCuboids.append(newCuboid)
        else:
            newCuboids.append(cuboid)
    
    if currentCuboid[3] == True:
        newCuboids.append(currentCuboid)

    return newCuboids

def Part2():
    with open('day22.txt') as f:
        lines = f.readlines()

    cuboids = []

    for line in lines:
        tokens = line.split()
        on = (tokens[0] == 'on')
        coords = tokens[1].split(',')
        xrange = ()
        yrange = ()
        zrange = ()
        for coord in coords:
            if coord.startswith('x='):
                xcoords = coord[2:].split('..')
                xrange = [int(xcoords[0]), int(xcoords[1])]
            elif coord.startswith('y='):
                ycoords = coord[2:].split('..')
                yrange = [int(ycoords[0]), int(ycoords[1])]
            elif coord.startswith('z='):
                zcoords = coord[2:].split('..')
                zrange = [int(zcoords[0]), int(zcoords[1])]

        cuboids.append([xrange, yrange, zrange, on])

    newCuboids = []
    newCuboids.append(cuboids[0])

    for i in range(1, len(cuboids)):
        newCuboids = UpdateCuboids(newCuboids, cuboids[i])

    count = 0
    for cuboid in newCuboids:
        count += (cuboid[0][1] - cuboid[0][0] + 1) * (cuboid[1][1] - cuboid[1][0] + 1) * (cuboid[2][1] - cuboid[2][0] + 1)

    print(count)

def main():
    Part1()
    Part2()
main()
