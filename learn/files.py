# Python has functions for creating, reading, updating, and deleting files.

#Read from file
myFile = open('sample.json','r+')
text = myFile.read(1000)
print(text)