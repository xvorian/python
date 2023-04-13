from model.store.Item import Item

class Phone(Item):
    def __init__(self, name: str, price: float, department: str, isBroken: bool):
        super().__init__(name, price, department)
        self.__isBroken = isBroken

    @property
    def isBoken(self):
        return self.__isBroken

    @isBoken.setter
    def isBroken(self, value):
        self.__isBroken=value