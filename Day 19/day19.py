from collections import defaultdict

def Parse(data):
    scanners = []
    for scanner in data:
        beacons = []
        for line in scanner.split("\n"):
            if "--" not in line:
                beacons.append(tuple([int(c) for c in line.split(",")]))
        scanners.append(beacons)
    return scanners

def RotatePoint(p, rotation):
    x, y, z = p

    if rotation == 0:
        return (x, y, z)
    if rotation == 1:
        return (x, -z, y)
    if rotation == 2:
        return (x, -y, -z)
    if rotation == 3:
        return (x, z, -y)
    if rotation == 4:
        return (-x, -y, z)
    if rotation == 5:
        return (-x, -z, -y)
    if rotation == 6:
        return (-x, y, -z)
    if rotation == 7:
        return (-x, z, y)
    if rotation == 8:
        return (y, x, -z)
    if rotation == 9:
        return (y, -x, z)
    if rotation == 10:
        return (y, z, x)
    if rotation == 11:
        return (y, -z, -x)
    if rotation == 12:
        return (-y, x, z)
    if rotation == 13:
        return (-y, -x, -z)
    if rotation == 14:
        return (-y, -z, x)
    if rotation == 15:
        return (-y, z, -x)
    if rotation == 16:
        return (z, x, y)
    if rotation == 17:
        return (z, -x, -y)
    if rotation == 18:
        return (z, -y, x)
    if rotation == 19:
        return (z, y, -x)
    if rotation == 20:
        return (-z, x, -y)
    if rotation == 21:
        return (-z, -x, y)
    if rotation == 22:
        return (-z, y, x)
    if rotation == 23:
        return (-z, -y, -x)

def AddPoints(p1, p2):
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    return (x1 + x2, y1 + y2, z1 + z2)

def SubPoints(p1, p2):
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    return (x1 - x2, y1 - y2, z1 - z2)

def InvertPoint(p):
    x, y, z = p
    return (-x, -y, -z)

def ManhattanDistance(p1, p2):
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    return abs(x1 - x2) + abs(y1 - y2) + abs(z1 - z2)

def main():
    data = open("day19.txt").read().strip().split("\n\n")
    scanners = Parse(data)
    ocean = set(scanners.pop(0))
    scannerCoords = [(0, 0, 0)]

    while scanners:
        testScanner = scanners.pop(0)
        match = False
        for rotation in range(24):
            offsets = defaultdict(int)
            for beacon in ocean:
                rotatedPoints = set()
                for point in testScanner:
                    rotatedPoint = RotatePoint(point, rotation)
                    x1, y1, z1 = beacon
                    x2, y2, z2 = rotatedPoint
                    offset = SubPoints(rotatedPoint, beacon)
                    offsets[offset] += 1
            for offset, ct in offsets.items():
                if ct >= 12:
                    match = True
                    scanner = InvertPoint(offset)
                    scannerCoords.append(scanner)
                    for point in testScanner:
                        point = RotatePoint(point, rotation)
                        ocean.add(AddPoints(point, scanner))
            
        if not match:
            scanners.append(testScanner)

    print(len(ocean))

    scannerDistances = set()
    while scannerCoords:
        p1 = scannerCoords.pop()
        for p2 in scannerCoords:
            scannerDistances.add(ManhattanDistance(p1, p2))

    print(max(scannerDistances))

main()
