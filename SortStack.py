#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 11:06:27 2019

@author: Jenny
"""

# Requires Stack.py
from Stack import *

stack1 = Stack()
stack2 = Stack()


def sort_stack():
    
    """Sorts an unsorted stack using another stack
    pre: input is a stack to be sorted
    post: stack is sorted"""
    
    while not stack1.is_empty():
        
        current = stack1.pop()
        
        while not stack2.is_empty() and stack2.peek() > current:
            stack1.push(stack2.pop())
        stack2.push(current)
        
    while not stack1.is_empty():
        stack1.push(stack2.pop())
                

# Driver code
         
stack1.push(4)
stack1.push(5)
stack1.push(2)
stack1.push(8)
stack1.push(1)
stack1.push(9)
stack1.print_stack()
sort_stack()
stack1.print_stack()
stack2.print_stack()