import datetime
class Employee:
    def __init__(self, f_name: str, l_name: str, age: int, address:str, dob:datetime,phone:str, department:str, manager:str, salary:float,date_of_join:datetime):
        self.__f_name=f_name
        self.__l_name=l_name
        self.__name= self.__f_name+' '+self.__l_name
        self.__age=age
        self.__address=address
        self.__datetime=datetime
        self.__phone=phone
        self.__department=department
        self.__manager=manager
        self.__salary=salary
        self.__date_of_joining=date_of_join

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,value):
        self.__name = value

