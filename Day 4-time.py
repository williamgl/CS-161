# Author: Gan Li
# Date: 7/31/21 11:22 上午
# Description: Chap 5 Exercise 1; This program is only valid until 2099
import time

epoch_year = 1970
epoch_month = 1
epoch_date = 1

month = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
         'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
days_of_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# The imported time is GTM-0 time. I am in Seattle, so I convert it to pacific time.
time_number = time.time() - 3600 * 7

days = int(time_number // (60 ** 2 * 24)) + 1
seconds = int(time_number % (60 ** 2 * 24))
hour = minute = second = 0

year = epoch_year
day = days

while day >= 366 + 365 * 3:
    year = year + 4
    day = day - (366 + 365 * 3)

if day >= 365 * 2 + 366:
    year = year + 3
    day = day - (365 * 2 + 366)
elif day >= 365 * 2:
    year = year + 2
    day = day - 365 * 2
elif day >= 365:
    year = year + 1
    day = day - 365
else:
    pass

for i in range(12):
    if day > days_of_month[i]:
        day = day - days_of_month[i]
    else:
        break

hour = seconds // 3600
seconds = seconds - 3600 * hour
minute = seconds // 60
second = seconds % 60

print('Today is ', day, ' ', month[i], ' ', year, '.', sep='')
print('Now is ', hour, ':', minute, ':', second, '.', sep='')
print('The epoch is 1 Jan 1970.')
print('It has been', days, 'days since the epoch.')
