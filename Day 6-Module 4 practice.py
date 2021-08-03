# Author: Gan Li
# Date: 8/2/21 8:49 上午
# Description: Chapter 6 and Module 4 practice
"""
def compare(a, b):
    if a > b:
        return 1
    elif a == b:
        return 0
    else:
        return -1


x = float(input('Please type in x:'))
y = float(input('Please type in y:'))
print(compare(x, y))
"""

"""
Ackermann function
def ack(m, n):
    if m > 0 and n > 0:
        return ack(m - 1, ack(m, n - 1))
    elif m > 0 and n == 0:
        return ack(m - 1, 1)
    elif m == 0:
        return n + 1
    else:
        return 'invalid m or n'


m_tem = int(input('m:'))
n_tem = int(input('n:'))
print(ack(m_tem, n_tem))
"""

"""
palindrome
def first(word):
    return word[0]


def last(word):
    return word[-1]


def middle(word):
    return word[1:-1]


def is_palindrome(word):
    length = len(word)
    if length <= 1:
        return True
    elif first(word) == last(word):
        return is_palindrome(middle(word))  # 第一次编程卡死在这里，忘了这个return statement
    else:
        return False


vocabulary = input('The word you want to test:')
print(is_palindrome(vocabulary))
"""

"""
Greatest Common Divisor
def gcd(a, b):
    if a > b:
        r = b
        b = a
        a = r
    else:
        pass
    r = b % a
    if r == 0:
        return a
    else:
        return gcd(r, a)


num_a = int(input('input the first integer:'))
num_b = int(input('input the second integer:'))

print(gcd(num_a, num_b))
"""


