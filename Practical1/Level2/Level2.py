import numpy
import random
#2
def returnYear():
    names = ["Monkey", "Rooster", "Dog", "Pig", "Rat", "Ox", "Tiger", "Hare", "Dragon", "Snake", "Horse", "Sheep"]
    print("Give a valid year: ")  #indexes above represent the remainder, thus allowing for a neater code
    year = int(input())
    if year <= 0:
        returnYear()
    else:
        remainder = year%12
        print("The year " + str(year) +" is the year of the " + names[remainder])

#returnYear();

#3
def isLeap():
    print("Give a year to be checked: ")
    year = int(input())
    if year%400 ==0:
        return True
    if year%100 ==0:
        return False
    if year%4 ==0:
        return True
    else:
       return False 



#print("Year = " + str(isLeap()))#

#4
def temperatureTable():

    celcius = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    fahrenheit = []


    for i in range(len(celcius)):
    
    
        fahrenheit.append(9/5*celcius[i] + 32);
   
    

    table = numpy.empty((len(celcius)+1, 2), dtype="<U10")
    table[0] = ("Celcius", "Fahrenheit")


    for i in range(len(celcius)):
        table[i+1] = (celcius[i], fahrenheit[i])
    return table


#print(temperatureTable())

#5
#print("Give word to check for being a palidrome:")
#word = input()

def isPalindrome(word):
    word1 = []
    word2 = []
    i=1
    for x in word:
        word1.append(x)
        
    for x in word:
        word2.append(word1[len(word1) - i])
        i+=1
        
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            
            return False
    return True

        
        
    print(word1, word2)       

#print("This word palindrome status is: ",isPalindrome(word))

#6

#print("Give number to be checked for being a prime number: ")
#number = int(input())

def isPrime(a):
    if a == 1:
        return False
    divisibles = [x  for x in range (2, number)]
    for x in divisibles:
        if a%x == 0:
            return False
    return True
#print("number ", number, "is prime: ", isPrime(number))

#7
#password = input("Input password: ")

def isGoodPassword(passw):
    Numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    passLetters =[]
    oneNumber = False;
    oneUppercase = False;
    oneLowercase = False;
    longEnough = False;
    for x in passw:
        passLetters.append(x)
    if len(passLetters) >= 8:
        longEnough = True;
    print(passLetters)
    for i in range(len(passLetters)):
        
        if (passLetters[i] in Numbers) and oneNumber ==False:
            oneNumber = True
            
        if (passLetters[i].isupper()) and oneUppercase ==False:
            oneUppercase = True
            
        if (passLetters[i].islower()) and oneLowercase ==False:   
            oneLowercase = True
            
    if oneNumber and oneUppercase and oneLowercase and longEnough:
       return True
    print (oneNumber, oneUppercase, oneLowercase, longEnough)
    return False
    

#print("Password", password, "is a ", isGoodPassword(password), " password")

#8

def generateNumbers():
    numbers = [x for x in range(1,50)]
    drawn = []
    i=0
    while i <5:
        chosenNo = random.choice(numbers)
        numbers.remove(chosenNo)
        drawn.append(chosenNo)
        i+=1
    drawn.sort()
    print("Drawn numbers are: ",drawn)


    
#generateNumbers()

#9
def f(x,l=[]):
    for i in range(x):
        l.append(i*i)
        print(l)

print("1",f(2))
print("2",f(3,[3,2,1]))
print("3",f(3))
