#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 11:55:48 2019

@author: Jenny
"""
# Requires Exceptions.py
from Exceptions import *

class StackNode:
    
    """Creates a separate class StackNode for values that will be added
    to the Stack class
    """
    
    def __init__(self, data, minimum):
        
        self.data = data
        self.next = None
        self.minimum = minimum
        
    def __lt__(self, other):
        
        return self.data < other
    
    def __gt__(self, other):
        
        return self.data > other
        
class Stack:
    
    def __init__(self):
        
        self.top = None
        self.size = 0
        # stores current minimum value in the stack at the time that the 
        # current node is added
        self.min = None
        
    def __len__(self):
        
        return self.size
        
    def pop(self):
        
        """Deletes item at top of the stack and returns value deleted"""
        
        if self.top is None:
            raise EmptyStackError
            
        item = self.top.data
        self.top = self.top.next
        self.size -= 1
        return item
        
    def push(self, item):
        
        """Pushes and item to the top of the stack"""
        
        if self.top is None:
            stack_node = StackNode(item, item)
            self.min = item
        
        # determines whether a new minimum value will be stored in the current
        # node or the old minimum will carry over
        if item < self.min:
            self.min = item
            
        stack_node = StackNode(item, self.min)
        stack_node.next = self.top
        self.top = stack_node
        self.size += 1
        
    def peek(self):
        
        """Returns the value currently at the top of the stack"""
        
        if self.top is None:
            raise EmptyStackError
            
        return self.top.data
    
    def is_empty(self):
        
        return self.top is None
    
    def print_stack(self):
        
        """Prints all values currently in the stack"""
        
        stack = ""
        current = self.top
        while current is not None:
            stack += str(current.data) + " "
            current = current.next
            
        print(stack)
    
    def print_with_mins(self):
        
        """Prints each value in the stack as well as the minimum value at 
        the time that node was added to the stack"""
        
        current = self.top
        while current is not None:
            print(current.data, current.minimum)
            current = current.next
            
    def minimum(self):
        
        return self.top.minimum
            

# Driver code
n = Stack()
print(n.is_empty())
n.push(3)
n.push(4)
n.push(9)
n.push(1)
n.push(8)
n.push(0)
print(n.is_empty())
n.print_with_mins()
print(n.minimum())
n.pop()
print(n.minimum())