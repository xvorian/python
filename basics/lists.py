numbers = [1,2,3,4,3,6,7,5,6,7,5,3]
cities = ["Toronto","Montreal","Quebec","Halifax"]

# simple printing
print(numbers)
print(cities)

print(cities[3])

# interation over the lists
for city in cities:
    print(city)

#
#for num in numbers:
#    print(num)


# appending
dubCities =[]
for city in cities:
    dubCities.append(city)
print(dubCities)

# inserting
dubCities.insert(0,"Calgary")
print(dubCities)
dubCities.insert(0,"Burlington")
print(dubCities)

# slicing range
print(dubCities[1:3])

# removing item from list
dubCities.pop(1)
print(dubCities)