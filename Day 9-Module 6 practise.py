# Author: Gan Li
# Date: 8/13/21 10:22 上午
# Description: String and List
def cum_sum(li):
    new_list = li
    for i in range(1, len(li)):
        new_list[i] = new_list[i-1] + li[i]
    return new_list


def main():
    t = []
    for i in range(10):
        t.append(i + 1)
    print(cum_sum(t))


if __name__ == "__main__":
    main()
