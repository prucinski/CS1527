#  Author: CS1527 Course Team
#  Date: 14 February 2021
#  Assessment 1:  20% of your overall mark for the course
# You need to modify the code below to make it run correctly.
# 1) The class is incomplete and is missing methods.
# 2) You will need to add methods to make this a circular array.
# 3) You will also need to complete the init method.
# 4) Lastly, add a method to create a menu so the user can modify maxlen.
# 5) With the menu you should have two options: one to change maxlen,
# 6) and the other to rerun the script to see the output with the change.

class Full(Exception):
    pass


class Empty(Exception):
    pass

class MyLeakyStack():
    #The structure of this code is pretty much copied from what I have created for the circular queue for practical with stacks and queues, which in turn was based on 
    #the structure provided by the tutorial. Then, after having imported that, I modified the circular queue to be a circular stack. After that, the "leaky" property was implemented.
    
    def __init__(self, maxlen, capacity):
        self._stackSize = maxlen   #maximum capacity of array (size of stack)
        self._capacity = capacity
        self._currentElements = 0;
        self._storage = [None]*capacity #storage room
        self._frontStackIndex = 0
        self._backStackIndex = 0        #frontStackIndex = top of the stack    
        
    def push(self, e):          #add to the top of the stack
        
        self._storage[self._frontStackIndex % self._capacity ] = e;
        self._currentElements +=1
        if (self._currentElements > self._stackSize):
            print("stack is full, removing ", self._storage[self._backStackIndex % self._capacity])
            self._storage[self._backStackIndex % self._capacity] = None
            self._currentElements -=1;
            self._backStackIndex +=1
            
        self._frontStackIndex +=1

    def pop(self):              #remove from the top of the stack
        
        temp = self._storage[(self._frontStackIndex -1) % self._capacity]
        if self._storage[(self._frontStackIndex - 1) % self._capacity] == None:
            raise Empty('The queue is empty')
        self._frontStackIndex -=1
        self._storage[self._frontStackIndex % self._capacity] = None
        self._currentElements -=1
        return temp

    def peek(self):          #returns the top element of the stack without removing it
        return self._storage[(self._frontStackIndex -1) % self._capacity]
        
        
    
    def is_empty(self):     #returns True if there are no elements in the stack
        return len(list(filter(None, self._storage))) == 0

    def __len__(self):      #returns the number of elements
        return len(list(filter(None, self._storage)))

    def show(self):         #prints the entire array of the stack
        print(self._storage)
    
    def set_length(self, newlength):
        self._storage = [None]*self._capacity  #resetting the stack to avoid glitches when setting a new length
        self._stackSize  = int(newlength)
        self._currentElements = 0;
        self._frontStackIndex = 0
        self._backStackIndex = 0 
   
        


    def menu(self):
        """ Either end or change the maxlen of the inner array """
        decision = input("Would you like to change the stack size of the leaky stack? WARNING: this operation will reset the stack (Y/N) ")
        if decision == "Y":
            newlength = input("Please provide the new stack size: ")
            S.set_length(newlength)
            S.run()
            
        elif decision == "N":
            return
        else:
            print("Unrecognised value. Please try again.")
            S.menu()




    ####### don't edit between here and the comment below ########
    def run(self):
        for i in range(12):
            try:
                S.push(i)
                print("after push "+str(i), S._storage)
            except Exception as e:
                print(e, "\n after push "+str(i), S._storage)

        for i in range(6):
            try:
                a=S.pop()
                print("after pop "+str(a), S._storage)
            except Exception as e:
                print(e, S._storage)

        for i in range(5):
            try:
               S.push(i+100)
               print("after push " + str(i+100), S._storage)
            except Exception as e:
               print(e, S._storage)
        ###### don't edit the above lines - add anything below as you wish
        
        S.menu()

#### don't add anything below here
if __name__ == '__main__':
    S = MyLeakyStack(5, 10)   # stack size should be 5 and the capacity of the array should be 10
    S.run()                   # start the application
    
