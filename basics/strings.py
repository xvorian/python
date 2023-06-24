# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods
first_name ="Amjad"
last_name='Hanif'
name = first_name+' '+last_name

### -------------------------------------------- ####
# String Methods
s = 'Hello'
print(s.capitalize()+' '+name)

### -------------------------------------------- ####
#Concatenate
print('Hello, my name is '+first_name+' '+last_name)

### -------------------------------------------- ####
# String Formatting
# Argument by position
print('Hello, my name is {f} {l}'.format(f=first_name, l=last_name))

#F-String formating
print(f'Hello, My name is {first_name} {last_name}')

### -------------------------------------------- ####
