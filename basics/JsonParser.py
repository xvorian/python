import json

with open('../data/sample.json','r') as file:
    raw_file = json.load(file)

menu = raw_file.get('menu')
popup = menu.get('popup')
menuitems = popup.get('menuitem')

for menuitem in menuitems:
    print(f"key 'value' is {menuitem['value']}, with key 'onclick' {menuitem['onclick']}")
