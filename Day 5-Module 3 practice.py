# Author: Gan Li
# Date: 8/1/21 12:45 下午
# Description:
# Module 3 exercises
import math
"""
num = float(input('Please type in a number:\n'))
print(num > 10)
"""

"""
num = int(input('Please type in a number:'))
numbers = ['one', 'two', 'three', 'four', 'five']
if 1 <= num <= 5:
    print(numbers[num-1])
else:
    print('input not recognized')
"""

"""
高斯求和 Gauss Sum
Gauss_sum = 0
num = int(input('Please type in a positive number:'))
for i in range(1, num + 1):
    Gauss_sum += i
print('The Gauss Sum is:', Gauss_sum)
"""

"""
sentence = input('Please type in a sentence:')
length = len(sentence)
if length % 2 == 0:
    print('even')
else:
    print('odd')
"""

"""
sentence = ''
while True:
    new_sentence = input('Please type in a sentence:')
    if new_sentence == 'quit':
        break
    else:
        pass
    sentence += new_sentence + '\n'
print(sentence)
升级版：
sentence = input('Please type in a sentence:')
while sentence != 'quit':
    print(sentence)
    sentence = input('Please type in a sentence:')
"""


class Solver:

    def demo(self, a, b, c):
        d = b ** 2 - 4 * a * c
        if d > 0:
            disc = math.sqrt(d)
            root1 = (-b + disc) / (2 * a)
            root2 = (-b - disc) / (2 * a)
            return root1, root2
        elif d == 0:
            return -b / (2 * a)
        else:
            return "This equation has no roots"


if __name__ == '__main__':
    solver = Solver()

    while True:
        a = int(input("a: "))
        b = int(input("b: "))
        c = int(input("c: "))
        result = solver.demo(a, b, c)
        print(result)
