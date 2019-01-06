import math

for i, j in [(x, math.log10(x)) for x in range(1,101)]:
    print(i, j)