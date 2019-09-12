#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 10:13:17 2019

@author: Jenny
"""
# Requires Stack.py
from Stack import *

new_stack = Stack()
old_stack = Stack()

class MyQueue:
    
    """Implementation of a queue that is comprised of two stacks"""
    
    def size(self):
        
        return len(new_stack) + len(old_stack)
    
    def add(self, value):
        
        """Add elements to new_stack, which contains newest elements at the
        top of the stack
        pre: input value to add
        post: return True when completed"""
        
        new_stack.push(value)
        
    def move_stacks(self):
        
        """Moves values from the new_stack to old_stack so that older values
        are now on the top of the old_stack
        post: new_stack is empty and old_stack has all values stored newest on
        bottom to oldest on top"""
        
        if old_stack.is_empty():
            while not new_stack.is_empty():
                old_stack.push(new_stack.pop())
                
    def queue_peek(self):
        
        """Returns oldest item add to the stacks"""
        
        self.move_stacks()
        return old_stack.peek()
    
    def remove(self):
        
        """Removes oldest value from the stacks and returns that value"""

        self.move_stacks()
        return old_stack.pop()


m = MyQueue()
m.add(2)
m.add(1)
m.add(3)
m.add(4)
m.add(5)
m.add(6)

new_stack.print_stack()
print(new_stack.peek())
print(m.queue_peek())
old_stack.print_stack()
print(m.size())
print(m.remove())
old_stack.print_stack()