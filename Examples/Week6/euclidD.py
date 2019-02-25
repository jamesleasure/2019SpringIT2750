import math

def euclidD(point1, point2):
    sum = 0
    for index in range(len(point1)):
        diff = (point1[index]-point2[index]) ** 2
        sum = sum + diff
        
    euclidDistance = math.sqrt(sum)
    return euclidDistance

print(euclidD([34, 78], [189, 211]))
print(euclidD([100023, 101022], [100024, 101023]))
print(euclidD([13,14,15], [12,13,14]))
