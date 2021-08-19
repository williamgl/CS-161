# Author: Gan Li
# Date: 8/16/21 5:21 下午
# Description:
def some_squares(n):
    square = {}
    for i in range(1, n + 1):
        square[i] = i ** 2
    return square


def main():
    n = int(input('input a positive integer:'))
    print(some_squares(n))


if __name__ == "__main__":
    main()
