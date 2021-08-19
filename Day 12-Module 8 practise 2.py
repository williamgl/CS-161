# Author: Gan Li
# Date: 8/15/21 4:06 下午
# Description: https://greenteapress.com/thinkpython2/html/thinkpython2012.html
from collections import Counter

N = Counter('nyankosensee')

eng_to_cn = {
    'one': '一',
    'two': '二',
    'three': '三',
    'four': '四',
    'five': '五',
    'six': '六',
    'seven': '七',
    'eight': '八',
    'nine': '九',
    'ten': '十',
    'hundred': '百',
    'thousand': '千',
    'ten-thousand': '万',
    'hundred-million': '亿'
}

# num = input('Please type in an integer:')


def inverse_num(number):
    length = len(number)
    inverse_list = []
    for i in range(length):
        inverse_list.append(int(number[length - (i + 1)]))
    return inverse_list


# inverse = inverse_num(num)

for key in eng_to_cn:
    print(key, eng_to_cn[key])
