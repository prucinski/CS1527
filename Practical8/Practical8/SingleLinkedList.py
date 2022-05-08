
# Copyright 2013, Michael H.  Goldwasser
#
# Developed for use with the book:
#
#    Data Structures and Algorithms in Python
#    Michael T.  Goodrich, Roberto Tamassia, and Michael H.  Goldwasser
#    John Wiley & Sons, 2013
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
class Empty(Exception):
    pass

class LinkedList:
  """Queue implementation using circularly linked list for storage."""
  
  #---------------------------------------------------------------------------------
  # nested Node class
  class Node:
        """Lightweight, nonpublic class for storing a singly linked node."""
        __slots__ = '_element', '_next'         # streamline memory usage

        def __init__(self, element, next = None):
          self._element = element
          self._next = next
        def get_element(self):
            return self._element
        def get_next(self):
            return self._next
        def set_next(self, new_next):
            self._next = new_next
        def set_current(self, new_current):
            self._element = new_current
      # end of _Node class
      #---------------------------------------------------------------------------------

  def __init__(self, head=None):
      self._head = head
      self._size = 0

  def insert_head(self, elem):
      new_node = self.Node(elem)
      new_node.set_next(self._head)
      self._head = new_node
      self._size +=1

  def get_size(self):
      return self._size

  def print_list(self):
      current = self._head
      listasarray = []
      while current:
          listasarray.append(current.get_element())
          current = current.get_next()
      print(listasarray)
      def return_node(self, nodeIndex):
          return listasarray[nodeIndex]

  def kth_to_last(self, k):
      current = self._head
      nodeIndex = 0
      listasarray =[]
      while current:
          nodeIndex+=1
          if nodeIndex >= k:
              listasarray.append(current.get_element())   
          current = current.get_next()
      print(listasarray)

  def delete_middle(self, node):
      
      self._size -=1
      node.set_current(current.get_next()) 
      node.set_next(temp.get_next())
      


  
  def search(self, data):
      current = self._head
      found = False
      while current and found is False:
          if current.get_element() == data:
              found == True
          else:
              current = current.get_next()
      if current is None:
          raise ValueError("Data is not in the list")
      return current

  def delete(self, data):
      current = self._head
      previous = None
      found = False
      while current and found is False:
          if current.get_element() == data:
              found = True
          else:
              previous = current
              current = current.get_next()
      if current is None:
          raise ValueError("Data not in list")
      if previous is None:
          self._head = current.get_next()
      else:
          previous.set_next(current.get_next())
          self._size -=1

  def delete_duplicates(self):
      current = self._head
      previous = None
      items = []
      while current:
          if current.get_element() in items:
               previous.set_next(current.get_next())        #deleting the node by removing the pointer
               current = current.get_next()
               self._size -=1
          else:
              items.append(current.get_element())
              previous = current
              current = current.get_next()

