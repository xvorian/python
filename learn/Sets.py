numbers = [1,2,3,4,3,6,7,5,6,7,5,3]
cities = ["Toronto","Montreal","Quebec","Halifax","Toronto"]

uniqueNumbers = set()
uniqueCities = set()

for num in numbers:
    uniqueNumbers.add(num)

for city in cities:
    uniqueCities.add(city)

print(uniqueNumbers)
print(uniqueCities)

