# Author: Gan Li
# Date: 7/30/21 5:11 下午
# Description: Module 1 testing
import math
print("Hello CS 161")
print(math.pi)

x = 6
y = 52
z = 0

y = y + 8
z = z + 15

y = y + 3 * 7
z = z + 3 * 12

y = y + 8
z = z + 15

while z >= 60:
    if z >= 60:
        y = y + 1
        z = z - 60

while y >= 60:
    if y >= 60:
        x = x + 1
        y = y - 60

print(x, ":", y, ":", z)


def countdown(n):
    if n <= 0:
        print('Blastoff!')
    else:
        print(n)
        countdown(n-1)
