import datetime

class Employee:
    num_of_employee =0
    raise_amount = 1.04

    def __init__(self, fName, lName, pay):
        self.fName = fName
        self.lName = lName
        self.pay = pay
        self.email = fName + "." + lName + "@company.com"

        Employee.num_of_employee += 1

    def fullName(self):
        return '{} {}'.format(self.fName, self.lName)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amount(cls,amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls,emp_str):
        first,last,pay = emp_str.split('-')
        return cls(first,last,pay)

    @staticmethod
    def is_work_day(day):
        if day.weekday() == 5 or day.weekday() ==6:
            return False
        return True
############################# END EMPLOYEE OF CLASS #############################
############################# END DEVELOPER OF CLASS #############################
class Developer(Employee):
    pass

############################# END MANAGER OF CLASS #############################
class Manager(Employee):
    pass

############################# END OF CLASES #############################

emp1 = Employee("John", "Doe", 50000)
emp2 = Employee.from_string('Jane-Doe-150000')

print(emp1.email)
print(emp2.email)
print(emp1.fullName())
print(emp1.pay)
print("-----------------")
Employee.set_raise_amount(1.08)
emp1.apply_raise()
print(emp1.pay)
print("-----------------")
emp1.set_raise_amount(1.10)
emp1.apply_raise()
print(emp1.pay)
print("-----------------")
print(emp2.email)

# date format (yyyy,mm,dd)
my_date = datetime.date(2022,12,10)
print(Employee.is_work_day(my_date))