# Name: Betero Tiikana
# Course: CS205 Discreet Math

# Import Library
from sys import argv

# File Reader function
def fileReader(data):
    with open(data, 'r') as file:
        fileData = file.read()
        print(fileData)

if len(argv) < 2:
    print('The command line is missing the file name parameter, try again!')
else:
    fileName = argv[1]
    fileReader(fileName)