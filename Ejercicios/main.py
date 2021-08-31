import random
import math

def BSSA(k):
    l = 0
    r = 10

    while (l <= r):
        m = math.floor((l + r) / 2)
        if (k == values[m]):
            return m
        elif (k < values[m]):
            r = m - 1
        else:
            l = m + 1
    return -1

values = []
for i in range(1,10):
    values.append(random.randint(1, 10))
values.sort()
print ( values )
print (BSSA(5))