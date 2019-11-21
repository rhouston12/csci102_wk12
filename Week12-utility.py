#Rhett Houston
#CSCI 102 Section C
#Week 12 Part A

def PrintOutput(word):
    print('OUTPUT', word)

def LoadFile(filename):
    with open(filename) as file1:
        file1 = file1.read()
        PrintOutput(file1)

def UpdateString(string1, string2, n):
    string1.replace(string1, string2, n)
    PrintOutput(string1)

def FindWordCount(list1, stringx):
    PrintOutput(list1.count(stringx))

    
