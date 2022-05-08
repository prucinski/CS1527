#---------------readme--------------------
#Author: 51985961
#This app is pretty straightforward to run. When launched, it prompts you to input your decision as to what you want to do.
#1 - Parses an expression into a binary tree and returns a formatted result. It will detect any mistakes within the expression. The
#expression must be of the form (X?Y), where X, Y = {(, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9} and ? = { +, -, *, /}.
#2 -As in 1, but also visualizes the tree using an inorder traversal. The user is then prompted whether they want to save the tree or not.
#
#3 - Loads a tree from a file, the name of which is specified by the user. WARNING - the file must be in the same directory as the programme.
#4 - Exits the program.
#Anything else - unrecognised input, will loop back again to the menu.
#
#There was some inspiration taken from the code repository for the Goodrich book - however, no fragment was directly taken from it. I only
#used it when I got stuck and needed some inspiration how to adjust my Tree data structure implementation.


import pickle
import unittest

#a simple exception class defining exceptions in parsing the expression. It will print where the error occured and and what the issue is.
class ParseError(Exception):
    def __init__(self, errorPosition, expectedOperands):
        self.errorPosition = errorPosition
        self.expectedOperands = expectedOperands
    def __str__(self):
        return "Error at position " + str(self.errorPosition) + ": expected one of the following: " + " or ".join(self.expectedOperands)


#This exception class SHOULD NEVER be reached (outside of one case) because of the way the programme operates. However, it is here in case anyone somehow managed to break the programme completely.
class WeirdError(Exception):
    pass

#A class defining a binary tree. Inside of it there is a class defining a node.
class BinaryTree():
    
    
    class Node():
        def __init__(self, value, left_child, right_child, position):
            self._position = position               #position is just a pointer - in this way, the tree can access a node's children
            self._value = value
            self._left_child = left_child           #left and right child here point to positions of a node
            self._right_child = right_child
        
        def getposition(self):
            return self._position

        def getvalue(self):         #standard setters and getters, I found them rather useful despite not being a common programming practice in python. They are used throughout the code.
            return self._value

        def setvalue(self, newv):
            self._value = newv

        def get_left_pos(self):
            return self._left_child

        def setleft(self, newo):
            self._left_child = newo

        def get_right_pos(self):
            return self._right_child
        def setright(self, newo):
            self._right_child = newo

        def __str__(self):              #This method is currently 'dead code'. However, it proved very useful during debugging and so I decided to leave it in in case anyone needed to edit the code.
            return str("This node has a value of " + str(self.getvalue())  + ", it's left child's position is " + str(self.get_left_pos()) + ", and it's right child's position is " + str(get_right_pos()))
            

    def __init__(self):
        #The tree stores all nodes as an array. This makes this tree more of a heap. Regardless, this was very convenient for this problem.
        self._all_nodes = []

    #a method that will create a node and add it to the tree (by default, it will be a node with no children and no value). It also returns the node so that we can operate on it.
    def insert_node(self, operand = None, lchild = None, rchild = None):
        #position will be the pointer - using position, node will point to next node through left child or right child. We will never be deleting any
        #nodes so this is a safe way of giving each node a position.
        position = len(self._all_nodes)                                   
        new_node = self.Node(operand, lchild, rchild, position)               #initialising the node
        self._all_nodes.append(new_node)
        return new_node

    
    def print_node_description(self):
        for items in self._all_nodes:
            print(items)

    #This method returns a node when provided a position.
    def find_node(self, position):
        if position != None:
            return self._all_nodes[int(position) ]

    #These two methods return the left child of a node X. The position of node X is the input of these functions.
    def find_left(self, position):
        parentNode = self.find_node(position)
        if self.find_node(parentNode.get_left_pos()):
            leftChild = self.find_node(parentNode.get_left_pos()).getvalue()
        else:
            leftChild = None
        return leftChild

    def find_right(self, position):
        parentNode = self.find_node(position)
        if self.find_node(parentNode.get_right_pos()):
            rightChild = self.find_node(parentNode.get_right_pos()).getvalue()
        else:
            rightChild = None
        return rightChild

    #This method returns the evaluated expression.
    def evaluate_expression(self, position = 0):
        node = self.find_node(position)      #start position - root node
        left = self.find_left(position)
        right = self.find_right(position)
        if left == None and right == None:
            return int(node.getvalue())
        if node.getvalue() == "+":
            return self.evaluate_expression(node.get_left_pos()) + self.evaluate_expression(node.get_right_pos())
        elif node.getvalue() == "-":
            return self.evaluate_expression(node.get_left_pos()) - self.evaluate_expression(node.get_right_pos())
        elif node.getvalue() == "*":
            return self.evaluate_expression(node.get_left_pos()) * self.evaluate_expression(node.get_right_pos())
        elif node.getvalue() == "/":
            return self.evaluate_expression(node.get_left_pos()) / self.evaluate_expression(node.get_right_pos())
        else:
            raise WeirdError("This error should be impossible to reach. Something went wrong in evaluation of the expression.")

    #This method just neatly prints the result of the function above.
    def evaluate_expression_print(self):
        print("The result of this expression evaluates to: ", self.evaluate_expression())

    #This method performs an inorder traversal of a binary tree to print a visualization of the tree to the user.
    def inorder_traversal(self, position = 0, calls = 0):
        calls+=2                            #the purpose of this variable is just to count how many spaces need to be printed for each line of the tree
        node = self.find_node(position)
        left = self.find_left(position)
        right = self.find_right(position)
        if left:
            self.inorder_traversal(node.get_left_pos(), calls)
        print(" " * calls, node.getvalue())
        if right:
            self.inorder_traversal(node.get_right_pos(), calls)


#A class used for testing the data structure.
class TestBinaryTree(unittest.TestCase):

    def test_expressionParsing(self):
        self.assertEqual(parse_expression("(4+5)").evaluate_expression(), 9)
        self.assertEqual(parse_expression("((9+5)*5)").evaluate_expression(), 70)
        self.assertEqual(parse_expression("(((6/3)*(9+5))*5)").evaluate_expression(), 140)
        self.assertEqual(parse_expression("(5/2)").evaluate_expression(), 2.5)
        
#THIS PART IS GLITCHY IN VISUAL STUDIO (and perhaps in other IDEs as well) as it throws the exception first and halts the execution of the programme. Using in cmd guarantees working just fine.
#Using a Regex can make us check if the message matches the expected one. I used "\" to sygnalise special characters within the regular expression.
#The documentation found at https://docs.python.org/3/library/unittest.html#assert-methods was a lifesaver.

    def test_expressionParsingExceptions(self): 
        with self.assertRaisesRegex(ParseError,  "Error at position 4: expected one of the following: \)"):
          parse_expression("(4+5")

        with self.assertRaisesRegex(ParseError,  "Error at position 5: expected one of the following: \)"):
          parse_expression("(4*3*2)")

        with self.assertRaisesRegex(ParseError,  "Error at position 6: expected one of the following: \+ or \- or \* or \/"):
          parse_expression("(4*(2))")

        with self.assertRaisesRegex(WeirdError,  "Error processing left bracket. Check if the brackets are mismatched"):
          parse_expression("(4*(3+2)*(2+1))")

        with self.assertRaisesRegex(ParseError,  "Error at position 6: expected one of the following: the expression should end here. Check if there are brackets missing."):
          parse_expression("(2*4)*(3+2)")

        with self.assertRaisesRegex(ParseError,  "Error at position 12: expected one of the following: \)"):
          parse_expression("((2+3)*(4*5)")

        with self.assertRaisesRegex(ParseError,  "Error at position 6: expected one of the following: the expression should end here. Check if there are brackets missing."):
          parse_expression("(2+5)*(4/(2+2)))")

        with self.assertRaisesRegex(ParseError,  "Error at position 18: expected one of the following: \+ or \- or \* or \/"):
          parse_expression("(((2+3)*(4*5))+(1(2+3))))")
    #def test_exceptions(self):
     #   pass





#This menu captures user input to decide what action within the programme will be taken. 
def menu():
    
    print("What would you like to do?")
    decision = input("Parse an expression - 1. Parse an expression and visualise the tree - 2. Load a tree from memory - 3. Test the programme using test cases - 4. Exit - 5.  \n")

    if decision == "1":
        expression = input("Please provide an expression to be parsed \n")
        print("Parsing expression...")
        tree = parse_expression(expression)
        tree.evaluate_expression_print()
        menu()
        

    elif decision == "2":
        expression = input("Please provide an expression to be parsed \n")
        print("Parsing expression... Visualising the tree...")
        tree = parse_expression(expression)
        tree.evaluate_expression_print()
        tree.inorder_traversal()
        decision2 = input("Would you like to save the tree visualization? (Y/N)\n")
        if decision2 == "Y":
            pickleTree(tree)
        menu()

    elif decision == "3":
        
        tree = unpickleTree()
        decision2 = input("Would you like to parse the expression within the tree? (Y/N)\n")
        if decision2 == "Y":
            tree.evaluate_expression_print()
        decision3 = input("Would you like to visualize the tree? (Y/N)\n")
        if decision3 == "Y":
            tree.inorder_traversal()
        menu()

    elif decision == "4":
        print("Testing...")
        unittest.main()
        

    elif decision == "5":
        print("Exiting...")
        return 0

    else:
        print("Error in inputs. Please provide just the number (e. g. 2 )")
        menu()

#This is the main function responsible for parsing the expression. While it perhaps should have been included inside the tree, I started coding with this and so it's outside the tree.
def parse_expression(expression):

    string = [character for character in expression]        #creating an array of characters from the expression provided 
    #removing trailing whitespaces
    while string[-1] ==" ":
        string.pop()

   
    node_stack = []
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    operands = ["+", "-", "*", "/"]
    expected_next = ["("]                                   #this data structure will keep track of what element needs to go next
    expressionTree = BinaryTree()
    currentPosition = 0                                     #keeping track of which character we are on right now (for error capture)

    for character in string:
       
        currentPosition +=1

        if character == "(":       
            
            if character not in expected_next:
                raise ParseError(currentPosition, expected_next)

            expected_next = expected_next + numbers
            newNode = expressionTree.insert_node()
           
            if node_stack:                      #If the stack is empty, then the first item created will be the root
                parent = node_stack.pop()          #New node created like this is by default the left child of the previous node
                if parent.get_left_pos() == None:        #If left child already exists, that means the left child and its children have been processed.
                    parent.setleft(newNode.getposition())         #Now, following the stack, the right node shall be processed.
                elif parent.get_right_pos() == None:
                    parent.setright(newNode.getposition())
                else:
                    raise WeirdError("Error processing left bracket. Check if the brackets are mismatched")
                node_stack.append(parent)
            node_stack.append(newNode)               #inserting an empty node onto the stack every time a new node is created
           

        elif character == ")":    
            
            if len(node_stack) == 0:
                expected_next.clear()
                expected_next = ["the expression should end here. Check if there are brackets missing."]
                raise ParseError(currentPosition, expected_next)
            if character not in expected_next:
                raise ParseError(currentPosition, expected_next)
            
            node_stack.pop()                    #node is complete, can be removed from the stack.
            expected_next.clear()
            expected_next = [")"] + operands
     

        elif character in numbers:

            if len(node_stack) == 0:
                expected_next.clear()
                expected_next = ["the expression should end here. Check if there are brackets missing."]
                raise ParseError(currentPosition, expected_next)
            if character not in expected_next:
                raise ParseError(currentPosition, expected_next)

            newNode = expressionTree.insert_node(character)
            numberNode = node_stack.pop()       
                                                               #If we have a number, then we'll set either the left child of the node [on top of the stack]
            if numberNode.get_left_pos() == None:            # or a right child of the node (if left is already there) to a number
                numberNode.setleft(newNode.getposition())
                expected_next.clear
                expected_next =  operands
            elif numberNode.get_right_pos() == None:
                numberNode.setright(newNode.getposition())
                expected_next.clear
                expected_next = [")"]
            else:
                raise WeirdError("Error in parsing number. You should have gotten an error already.")

            node_stack.append(numberNode)

 

        elif character in operands:

            if len(node_stack) == 0:
                expected_next.clear()
                expected_next = ["the expression should end here. Check if there are brackets missing."]
                raise ParseError(currentPosition, expected_next)
            if character not in expected_next:
                raise ParseError(currentPosition, expected_next)
            
            numberNode = node_stack.pop()           #If there is an expected operand, then the item on top of the stack will have its value set to the operand
            numberNode.setvalue(character)
            node_stack.append(numberNode)

            expected_next.clear
            expected_next = ["("] + numbers

        else:
            expected_next = expected_next + ["--- \nThe provided character within the expression does not belong to an expression."]
            raise ParseError(currentPosition, expected_next)

        #Finally, the loop analysing every character is over. The input has been parsed into a tree. If there is still something left on the stack, it means there was an error.
    if node_stack:
        expected_next = [")"]
        raise ParseError(currentPosition, expected_next)
    return expressionTree


#functions using the pickle package were inspired from https://wiki.python.org/moin/UsingPickle
def pickleTree(expressionTree):
    filename = input("Please provide a file name you would like to use. Do not provide any extension (e.g. '.p') \n")
    pickle.dump(expressionTree, open(filename +".p", "wb"))
    print("Tree has been successfully saved to " + filename + ".p in the directory of the programme")
def unpickleTree():
    filename = input("Please provide the name of a file you would like to open. The file must be in the same directory as this programme.\n Do not provide any extension (e.g. '.p') \n")
    print("Loading the tree...")
    expressionTree = pickle.load(open(filename+".p", "rb"))
    return expressionTree

#----------main-----------
print("Welcome to the expression tree programme.")
menu()