import json

file = None
towrite = ""
with open("../data/sample.txt", "r") as file:
    for line in file.readlines():
        towrite = towrite + line
        print(line, end="")

with open("../data/sample_copy.txt", "w") as file:
    file.write(towrite)

# with open("../data/sample.json", "r") as json_file:
#     data = json.load(json_file)
#     print(data.get("menu"))
