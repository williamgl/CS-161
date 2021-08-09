# Author: Gan Li
# Date: 8/8/21 4:56 下午
# Description: classes and objects
class Employee:
    """Represents an employee"""

    def __init__(self, name, hourly_wage):
        self._name = name
        self._wage = hourly_wage

    def get_wage(self):
        return self._wage

    def set_wage(self, new_wage):
        self._wage = new_wage

    def get_name(self):
        return self._name

    def change_name(self, new_name):
        self._name = new_name

    def cal_pay(self, hours):
        return self._wage * hours


gan = Employee('Gan Li', 25.76)

hours = int(input('How many hours did you work for current pay period?'))
print(gan.cal_pay(hours))
