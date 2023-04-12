# If/ Else conditions are used to decide to do something based on something being true or false
x = 5
y = 10
z = 2
b = 5

# Comparison Operators (==, !=, >, <, >=, <=) - Used to compare values

if x > y:
    print(f'{x} is greater than {y}')
else:
    print(f'{y} is greater than {x}')

if x > y:
    print(f'{x} is greater than {y}')
elif y < x:
    print(f'{y} is greater than {x}')
else:
    print(f'{y} is equal to {x}')
# Logical operators (and, or, not) - Used to combine conditional statements
if x > z and x < y:
    print(f'{x} is greater than {z} and less than {y}')

if not(x==y):
    print('x is not equal to y')

# Membership Operators (in, not in) - Membership operators are used to test if a sequence is presented in an object
numbers = [1, 2, 65, 3, 5, 67, 4, 3, 5, 6, 4, 2, 4, 5, 87, 3]
if x in numbers:
    print(x in numbers)

if x not in numbers:
    print(x not in numbers)

# Identity Operators (is, is not) - Compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:
if x is b:
    print('both are equal')