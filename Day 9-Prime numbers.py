# Author: Gan Li
# Date: 8/13/21 11:31 上午
# Description: Input a number n < 10000, return the nth prime number
def prime(n, total):
    prime_list = [2, 3]
    for i in range(2, total):
        if check_prime(i, prime_list):
            prime_list.append(i)
    if n <= len(prime_list):
        return prime_list[n - 1]
    else:
        print('There is only ', len(prime_list), ' prime numbers under ',
              total, '.', sep='')


def check_prime(n, li):
    for i in range(len(li)):
        if n % li[i] == 0:
            return False
    return True


if __name__ == "__main__":
    setting = 10000
    change = input('The current setting is to check numbers up to 10000.\n'
                   'Would you wants to change this setting?(Y/N)')
    while change != 'N':
        if change == 'Y':
            setting = int(input('Please type in the new limit:'))
            change = 'N'
        else:
            change = input('Wrong command. Please type in Y/N:')
    num = int(input('Please input the number n:'))
    if num == 11 or 12 or 13:
        print('The ', num, 'th prime number under ', setting, ' is ',
              prime(num, setting), '.', sep='')
    elif num % 10 == 1:
        print('The ', num, 'st prime number under ', setting, ' is ',
              prime(num, setting), '.', sep='')
    elif num % 10 == 2:
        print('The ', num, 'nd prime number under ', setting, ' is ',
              prime(num, setting), '.', sep='')
    elif num % 10 == 3:
        print('The ', num, 'rd prime number under ', setting, ' is ',
              prime(num, setting), '.', sep='')
    else:
        print('The ', num, 'th prime number under ', setting, ' is ',
              prime(num, setting), '.', sep='')
