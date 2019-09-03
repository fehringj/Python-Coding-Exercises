#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 11:42:32 2019

@author: Jenny
"""

def oneAway(string1, string2):
    
    """Determines whether string1 is one function away (replace, insert, or 
    delete) from string2
    pre: input two strings
    post: returns True if string1 is one function away from string2
    """
    
    if len(string1) == len(string2):
        return one_replace(string1, string2)
    elif len(string1) + 1 == len(string2):
        return one_insert(string1, string2)
    # insert is equivalent to delete but the roles of the two strings are 
    # reversed, so the same function can be used as for insert, but with 
    # the strings in reverse order
    elif len(string1) - 1 == len(string2):
        return one_insert(string2, string1)
    
def one_replace(first, second):
    
    """Account for whether string1 would be equivalent to string2 if
    one character were replaced with another
    pre: input is two strings
    post: return True if string1 is equivalent to string2 when one letter is
    replaced
    """
    
    different_letter = False
    for i in range(0, len(first)):
        if first[i] != second[i]:
            if different_letter:
                return False
            different_letter = True
    return True
    
def one_insert(first, second):
    
    """Determines whether an item can be inserted or deleted into either 
    string and the strings would then be equivalent
    pre: takes two strings
    post: returns True when strings are equivalent with one insertion/deletion
    """
    
    index1 = 0
    index2 = 0
    
    while index2 < len(second) and index1 < len(first):
        if first[index1] != second[index2]:
            if index1 != index2:
                return False
            index2 += 1
        else:
            index1 += 1
            index2 += 1
    return True