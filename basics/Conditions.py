condition=True
if condition:
    print("Condition is true")

emptyNames = []
names = ["Amjad","Ayan"]

if emptyNames:
    print("result is false")

if names:
    print("This is true")

result = 10
if result > 0 and result<10:
    print("result between 10")
elif result>=10 and result<=100:
    print("result between 10 - 100")
else:
    print("not a valid number")