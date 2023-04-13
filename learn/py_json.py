# JSON is commonly used with data APIS. Here how we can parse JSON into a Python dictionary
import json

userJSON = '{"first_name":"Amjad","last_name": "Hanif","age": 45,"active": "True"}'

user = json.loads(userJSON)
print(user)