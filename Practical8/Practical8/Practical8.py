import SingleLinkedList as sll


#exercise1
myList = sll.LinkedList()

myList.insert_head(1)
myList.insert_head(2)
myList.insert_head(3)
myList.insert_head(1)
myList.insert_head(2)
myList.insert_head(3)
myList.insert_head(4)
myList.insert_head(1)
myList.insert_head(2)
myList.insert_head(3)
myList.insert_head(1)
myList.insert_head(2)
myList.insert_head(3)
myList.insert_head(4)
print("-----------")
print(myList.get_size())
myList.print_list()
myList.kth_to_last(4)
myList.kth_to_last(0)

myList.delete_duplicates()
print("---------")
print(myList.get_size())
myList.print_list()
print("---------")
myList.print_list()
#myList.delete_middle(myList.print_list().return_node(4))  ??
myList.print_list()