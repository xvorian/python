import json
import os

file = None
towrite = ""

# get all files in directory
fileList = os.listdir("../data")

# iterate through all files in directory
for file in fileList:

# check if it is file or directory ###
    if os.path.isfile("../data/" + file):
        with open("../data/" + file, "r") as file:
            for line in file.readlines():
                towrite = towrite + line
                print(line, end="")
    print("\n-------------------------------------------------------------")

### write to file while reading from source file
# with open("../data/sample_copy.txt", "w") as file:
#     file.write(towrite)

# with open("../data/sample.json", "r") as json_file:
#     data = json.load(json_file)
#     print(data.get("menu"))
