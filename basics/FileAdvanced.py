import os

# directory location
print(os.getcwd())

# change directory
os.chdir("../data")
print(os.getcwd())

# list all the files in the current directory
print(os.listdir())

# create a new directory
os.mkdir("data_backup")
print(os.listdir())

#Copy files from current directory to new directory
# for file in os.listdir():
