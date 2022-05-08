import sys;
#Exercise1
def minmax(sequence,min = sys.maxsize, max = -sys.maxsize, a = 0):
    
    
    if(a == len(sequence)):
        print("Sequence " + str(sequence))
        print("The maximum is " + str(max) + " and the minimum is " + str(min))
        return(min, max);
        
   
    if(sequence[a] < min):
        min = sequence[a]
    if(sequence[a] > max):
        max = sequence[a]
    a+=1;
    return minmax(sequence, min, max, a)

#minmax([-12,2,-3,4,5])

#Exercise2
def productofintegers(m, n, product = 0):
    
    if n ==0:
        return product
    product += m
    n-=1;
    return productofintegers(m, n, product)

#print(productofintegers(4, 5))

#Exercise3

#Exercise4
def palindrome(word, i =0):
    listWord = list(word);
    if i > len(listWord) - i - 1:
        return ''.join(listWord)
    temp = listWord[i];
    listWord[i] = listWord[len(listWord) - i - 1]
    listWord[len(listWord) - i - 1] = temp;
    i+=1;
    return palindrome(listWord, i)
    
    



print(palindrome('pots&pans'))

#Exercise5
def isPalindrome(word):
    if palindrome(word) == word:
        return True;
    else:
        return False;

print(isPalindrome("racecar"))
print(isPalindrome("racercar"))

