cities = ["Toronto","Montreal","Quebec","Halifax"]

def capitalizeCase(string):
    print(string.capitalize())

def squared(number):
    return number**2

# default parameter value
def greets(name="Guest"):
    return "Hello "+name
print(squared(3))

def printList(list):
    for name in list:
        print(name)

print(greets()) # default
print(greets("Amjad"))
printList(cities)