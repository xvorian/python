dic1 = {"numbers": [1, 2, 3, 4, 3, 6, 7, 5, 6, 7, 5, 3],
        "cities": ["Toronto", "Montreal", "Quebec", "Halifax"]}

for city in dic1.get("cities"):
        print (city)

for key in dic1.keys():
        print(dic1.get(key))

for values in dic1.values():
        print(values)

for key,value in dic1.items():
        print(key,value)

print("---------------------------")
for key in dic1:
        for value in dic1.get(key):
                print(value)