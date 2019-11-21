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

def Intersection(list1, list2):
    x = 0
    list3 = list1 + list2
    list4 = []
    for i in list3:
        if list3.count(list3[x]) > 1:
            list4.append(list3[x])
        x += 1
    PrintOutput(list4)

def NotIn(list1, list2):
    x = 0
    list3 = list1 + list2
    list4 = []
    list5 = []
    for i in list3:
        if list3.count(list3[x]) == 1:
            list4.append(list3[x])
        x += 1
    for i in list4:
        if i in list1:
            list5.append(i)
    PrintOutput(list5)
            
