# Author: Gan Li
# Date: 8/14/21 11:24 上午
# Description: Module 8 practise
"""
def histogram(string):
    dictionary = dict()
    for character in string:
        if character not in dictionary:
            dictionary[character] = 1
        else:
            dictionary[character] += 1
    return dictionary
"""


def histogram(string):
    dictionary = dict()
    for character in string:
        dictionary[character] = dictionary.get(character, 0) + 1
    return dictionary


# def main():
sentence = input('Please type in your sentence:')
hist = histogram(sentence)
# print(hist)
# for c in sorted(hist):
#     print(c, hist[c])


# if __name__ == "__main__":
#    main()


def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse


print(invert_dict(hist))
