# Author: Gan Li
# Date: 8/13/21 5:19 下午
# Description: Module 7
def sum_all(*args):
    s = 0
    for arg in args:
        s += arg
    return s


def main():
    print(sum_all(1, 3, 5, 7, 9))


if __name__ == "__main__":
    main()
# https://canvas.oregonstate.edu/courses/1836660/pages/module-7-exercise-solutions?module_item_id=20450322
