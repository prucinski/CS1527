import sys
import myLeakyStack as m

#exercise1
def header():
    try:
        file = open("test.py", "r")
        a = 0
        while a < 10:
            for lines in file:
                print(lines)
                a+=1
                break
        file.close()
    except IOError:
        print("something went wrong")

def tail():
    try:
        array = [None] * 10
        file = open("test.py", "r")
        stack = m.MyLeakyStack(10,11)
        for lines in file:
            stack.push(lines)
        
        for i in range(len(stack)):
            array[i] = stack.pop()
        array = reversed(array)
        for item in array:
            print(item)

            

        file.close()
    except IOError:
        print("something went wrong")

#tail()

def removeComments():
    try:
        name0 = input("Please input the name of the old file: ")
        file = open(name0, "r")
        name1 = input("Please input the name of the new file: ")
        fileResult = open(name1, "a")
        stringLine = ""
        for lines in file:
            
            for characters in lines:
                if characters != '#':
                    stringLine += characters
                    continue
                
                
                break
        fileResult.write(stringLine)       
        file.close()           
        fileResult.close()


    except IOError:
        print("something went wrong")

#removeComments()


def searchVowels():
    name0 = input("Please input the name of the file to search a word with the vowels a e i o u in order: ")
    file = open(name0, "r")
    foundWords = []
    for lines in file:

