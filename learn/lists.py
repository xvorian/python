# A List is a collection which is ordered and changeable. Allows duplicate members.
# Create list
numbers = [1, 2, 65, 3, 5, 67, 4, 3, 5, 6, 4, 2, 4, 5, 87, 3]
numbers2 = list((43, 67, 67, 4, 3, 2, 56, 67, 87, 56, 3, 23, 45, 67, 89))

# empty list
my_list = []

# list with mixed data types
mix_list = [1, "Hello", 3.4]

fruits = ["apple", "banana", "cherry", "apple", "cherry"]


# print list
print(numbers)
print(numbers2)

# list functions
print(fruits[1].capitalize())
print(fruits)
print(len(fruits))

# Append to list
fruits.append('Mangos')
print(len(fruits))
print(fruits)

#insert at certain position
fruits.insert(1,'berries')
print(fruits)
