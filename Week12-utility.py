#Rhett Houston
#CSCI 102 Section C
#Week 12 Part A

def PrintOutput(word):
    print('OUTPUT', word)

def LoadFile(filename):
    with open(filename) as file1:
        file1 = file1.read()
        PrintOutput(file1)
