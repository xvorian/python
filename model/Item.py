import csv


class Item:
    # class attributes
    tax = 13
    discount_rate = 0.05
    all = []

    def __init__(self, name: str, price: float, department: str):
        # Run validation to the received arguments
        assert len(name) > 0, f"Name {name} should not be empty or zero"
        assert price >= 0, f"Price {price} should be greater than 0"
        assert len(department) > 0, f"Department {department} should not be empty or zero"

        # Assign to self object
        self.__name = name
        self.__price = price
        self.__department = department

        # Actions to execute
        Item.all.append(self)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def price(self):
        return self.__price

    @property
    def department(self):
        return self.__department

    def price_after_tax(self):
        return round(self.price + (self.price * (Item.tax / 100)), 2)

    def price_after_discount(self):
        return round(self.price - (self.price * (self.discount_rate / 100)), 2)

    def order_total(self, quantity):
        return round(self.price_after_tax() * quantity, 2)

    @staticmethod
    def initantiate_from_csv(file):
        with open(file, "r") as filename:
            reader = csv.DictReader(filename)
            items = list(reader)

            # Initiate the items
            for item in items:
                Item(name=item["name"], price=float(item["price"]), department=item["department"])

    def __repr__(self):
        # Gives the details of all class and instance members
        return f"{self.__class__.__name__}('{self.name}','{self.price}','{self.department}')"

    def __str__(self):
        # Gives the details of all class and instance members
        return f"{self.__class__.__name__}('{self.name}','{self.price}','{self.department}')"

    def __eq__(self, other):
        return self.name == other.name and self.price == other.price and self.department == other.department


########### end of class implementation ###########

