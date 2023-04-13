class Item:
    tax = 13
    def __init__(self, name: str, price: float, department: str):
        # Run validation to the received arguments
        assert price >= 0, f"Price {price} should be greater than 0"
        assert len(department) > 0
        assert len(name) > 0

        #Assign to self object
        self.name = name
        self.price = price
        self.department = department

    def price_after_tax(self):
        return round(self.price + (self.price * (self.tax/100)),2)

    def order_total(self, quantity):
        return round(self.price_after_tax()*quantity, 2)


item1 = Item("Dell", 1099.99, "Laptop")
item2 = Item("HP", 899.99, "Desktop")

# totalprice = round(item1.total_price(13), 2)
print(f'Total price for {item1.name} after tax would be {round(item1.price_after_tax(), 2)}')
print (f'Total for 3 laptops is {item1.order_total(3)}')

print(item1.__dict__) # see the values/attributes of the instance in a dictionary format.
