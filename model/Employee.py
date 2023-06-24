import datetime

from enum import Enum
from msilib.schema import Property


class Role(Enum):
    SOFTWARE_ENGINEER = "Software Engineer"
    QA_ENGINEER = "QA Engineer"
    DEVELOPER = "Developer"
    TESTER = "Tester"
    MANAGER = "Manager"
    CEO = "CEO"
    DESIGN = "Design Engineer"
    OTHER = "Other"


class Employee:

    def __init__(self, name: str, role: Role, salary: float):
        self.name = name
        self.role = role
        self.__salary = salary
        self.__bonus = self.__calculate_bonus()

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        self.__salary = value

    def __calculate_bonus(self):
        if self.role == Role.QA_ENGINEER:
            return self.__salary * 4
        elif self.role == Role.DEVELOPER:
            return self.__salary * 5
        elif self.role == Role.TESTER:
            return self.__salary * 6
        elif self.role == Role.MANAGER:
            return self.__salary * 7
        elif self.role == Role.CEO:
            return self.__salary * 10
        elif self.role == Role.DESIGN:
            return self.__salary * 3
        elif self.role == Role.OTHER:
            return self.__salary * 2
        elif self.role == Role.SOFTWARE_ENGINEER:
            return self.__salary * 5

    def __str__(self) -> str:
        return f"Name: {self.name}, Role: {self.role.value} Salary: {self.__salary}, Bonus: {self.__bonus}"

    def greeting(self):
        return f"Hello, {self.name} your Role is {self.role.value}"

    def work(self):
        return f"{self.name} is working as {self.role.value}"

    @staticmethod
    def calculate_rrsp(salary, rate):
        result = 0
        try:
            result = salary / (rate / 100)
        except ZeroDivisionError:
            print("Division by zero")
        return result

    def calculate_bonus(self):
        return format(self.__salary * 1.10, '.2f')


############### END of Employee Class ###################

############### START of Software Engineer Class ###################
class SoftwareEngineer(Employee):
    def debug(self):
        print(f"{self.name} is a Debugging as {self.role.value}")


############### END of Software Engineer Class ###################

############### START of QA Engineer Class ###################
class QAEngineer(Employee):
    alias = Role.QA_ENGINEER

    def work(self):
        return f"{self.name} is working as QA Engineer"


class Designer(Employee):
    def work(self):
        return f"{self.name} is working as Designer"


############### END of Software Engineer Class ###################

############# End Class Definition #############

se1 = SoftwareEngineer("John", Role.SOFTWARE_ENGINEER, 22000)
qe1 = QAEngineer("Jane", Role.QA_ENGINEER, 10000)
d1 = Designer("Micheal", Role.DESIGN, 12000)

employees = [se1, qe1, d1]
for employee in employees:
    print(employee)
print("________________________________")

# print(se1)
# print(se1.work())
# se1.debug()
# print("________________________________")
# print(qe1)
# print(qe1.work())
# print("________________________________")
