from model.store.Item import Item
from model.store.Phone import Phone

item = Item("Dell", 1099.99, "Laptop")

phone = Phone("iPhone 14", 1899.99, "Phone", True)

# totalprice = round(item1.total_price(13), 2)
print(f'Total price for {item.name} after tax would be {item.price_after_tax()}')
print (f'Total for 3 laptops is {item.order_total(3)}')

print(item.__dict__) # see the values/attributes of the instance in a dictionary format.
print(phone.__dict__) # see the values/attributes of the instance in a dictionary format.
print(f'Total Price for Phone order {phone.order_total(5)}')
print(f'{phone.__repr__()} {Phone.all}')
print(f'{item.__repr__()} {Item.all}')
