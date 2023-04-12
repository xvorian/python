# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
# Read more about dictionaries at https://docs.python.org/3/tutorial/datastructures.html#dictionaries
person = {
    'first_name': 'Amjad',
    'last_name': 'Hanif',
    'age': 45,
    'active': True
}

person2 = {
    'first_name': 'Shumaila',
    'last_name': 'Amjad',
    'age': 42,
    'active': True
}

family = [person,person2]

print(family)

person_via_constructor=dict(name='John Doe',age=30,active=False)

print(person, type(person))
print(person_via_constructor)

print(person_via_constructor['age'])
print(person_via_constructor.get('name'))

# add key value
person_via_constructor['phone']='123.321.3214'

print(person_via_constructor)

# get dictionary keys
print(person_via_constructor.keys())

via_constructor = person_via_constructor.copy()
via_constructor['city']='Toronto'

print(person_via_constructor)
print(via_constructor)


# Remove item
del(via_constructor['city'])
person_via_constructor.pop('phone')
