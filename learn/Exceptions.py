def div(n, d):
    if(d==0):
        raise Exception("something went wrong")

try:
    result= 12/0
    name = result + "200"
except (TypeError, ZeroDivisionError):
    print("not adding propery")
    result= 12/1
print(result)

try:
    print(int("text"))
except ValueError:
    print("text")

div(3,4)
div(1,0)


