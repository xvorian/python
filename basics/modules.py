# A module is basically a file containing a set of functions to include in your application. There are core python modules, modules you can install using the pip package manager (including Django) as well as custom modules
#Core modules

from camelcase import CamelCase

#User defined modules
import lists
import functions

# Import custom module
from validator import validate_email

# Using modules
print(lists.fruits)

print(functions.divide(3, 4))

c = CamelCase()
print(c.hump('all lower case'))

email ='test@test.com'
invalid_email='test.com'

if validate_email(email):
    print(f'{email} is a valid email')
else:
    print(f'{email} is a Invalid email')

print(validate_email(invalid_email))