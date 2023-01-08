from collections import defaultdict

def line(x0, y0, x1, y1):
    if y0 == y1 :
        return 0, y0

    if x0 == x1:
        return x0, None

    else:
        slope = (y1-y0) / (x1-x0) 
        interact = y0 - slope*x0
        return slope, interact

def maxPoints(points):
    if len(points) == 1:
        return 1
    lines = defaultdict(lambda: set())
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            x0, y0 = points[i]
            x1, y1 = points[j]
            ourline = line(x0, y0, x1, y1)
            lines[ourline].add(i)
            lines[ourline].add(j)
        return max([len(lines[ourline])] for ourline in lines)

points = [[0,0],[4,5],[7,8],[8,9],[5,6],[3,4],[1,1]]
print(maxPoints(points))
