# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
list_fruits = ["apple", "banana", "cherry", "apple", "cherry"]
set_fruits = {"apple", "banana", "graphs", "apple", "cherry"}
tuples_fruits = ("apple", "banana", "cherry", "apple", "cherry")


for fruit in list_fruits:
    if fruit == 'apple':
        print('found name but still continue')
        continue
    print(f'Name: {fruit}')

# loop through range

for i in range(len(list_fruits)):
    print(f'Name: {list_fruits[i]}')

for j in range(0,10):
    print(f'for value is: {j}')
# While loops execute a set of statements as long as a condition is true.
count=0
while count < 10:
    print(f'while value is: {count}')
    count+=1