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

def ScoreFinder(list1, list2, stringy):
    x = 0
    for i in list1:
        if i == stringy:
            PrintOutput(stringy)
            PrintOutput(list2[x])
        x += 1

def Union(list1, list2):
    list3 = list1 + list2
    PrintOutput(list3)
