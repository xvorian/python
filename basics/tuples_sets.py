# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
tuples_numbers = (1, 2, 65, 3, 5, 67, 4, 3, 5, 6, 4, 2, 4, 5, 87, 3)
tuples_numbers2 = tuple((43, 67, 67, 4, 3, 2, 56, 67, 87, 56, 3, 23, 45, 67, 89))

# empty list
tuples_my_list = ()

# list with mixed data types
mix_list = (1, "Hello", 3.4)

tuples_fruits = ("apple", "banana", "cherry", "apple", "cherry")

#print tuples
print(tuples_numbers)
print(tuples_numbers2)
print(type(tuples_fruits))



# A Set is a collection which is unordered and unindexed. No duplicate members.
set_numbers = {1, 2, 65, 3, 5, 67, 4, 3, 5, 6, 4, 2, 4, 5, 87, 3}
# set_numbers2 = set{43, 67, 67, 4, 3, 2, 56, 67, 87, 56, 3, 23, 45, 67, 89}
set_my_list = {}

# list with mixed data types
set_mix_list = {1, "Hello", 3.4}
set_fruits = {"apple", "banana", "graphs", "apple", "cherry"}


# check if in set
print('Apple' in set_fruits)

print(set_numbers)
print(set_fruits)
print(type(set_fruits))
set_fruits.add('watermalon')
print(set_fruits)

