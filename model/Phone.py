from model.Item import Item


class Phone(Item):
    def __init__(self, name: str, price: float, department: str, isBroken: bool):
        assert isinstance(isBroken,bool), f"{isBroken} should be boolean"
        super().__init__(name, price, department)
        self.__isBroken = isBroken

    @property
    def isBoken(self):
        return self.__isBroken

    @isBoken.setter
    def isBroken(self, value):
        self.__isBroken = value


Item.initantiate_from_csv("../data/items.csv")
phone1 = Phone("Samsung Galaxy S20 Ultra", 1124.99, "Electronics", False)
phone2 = Phone("Samsung Galaxy S20", 1149.99,"Electronics",True)

phones = [phone1, phone2]
for phone in phones:
    print(phone.price_after_tax())

#print(Item.all)

