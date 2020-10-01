import random
import math

n = int(input("Enter n: "))
arr = []
sqr = []
count = 0


def square(x, c):
    root = math.sqrt(x)
    if int(root + 0.5) ** 2 == x:
        sqr.append(x)
        c += 1
    return c


for i in range(n):
    arr.append(int(random.randint(1, 100)))
    count = square(arr[i], count)

print('Squares:', sqr, '\nCount:', count)