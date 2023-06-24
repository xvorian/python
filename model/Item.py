class Item:
    tax = 13
    all = []
    def __init__(self, name: str, price: float, department: str):
        # Run validation to the received arguments
        assert price >= 0, f"Price {price} should be greater than 0"
        assert len(department) > 0
        assert len(name) > 0

        #Assign to self object
        self.__name = name
        self.__price = price
        self.__department = department

        #Actions to execute
        Item.all.append(self)

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, value):
        self.__name=value

    @property
    def price(self):
        return self.__price

    @property
    def department(self):
        return self.__department

    def price_after_tax(self):
        return round(self.price + (self.price * (self.tax/100)),2)

    def order_total(self, quantity):
        return round(self.price_after_tax()*quantity, 2)


    def __repr__(self):
        # Gives the details of all class and intance members
        return f"{self.__class__.__name__}('{self.name}','{self.price}','{self.department}')"




