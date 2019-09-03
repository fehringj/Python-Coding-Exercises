#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 13:42:23 2019

@author: Jenny
"""

def checkPermutation(string1, string2):
    
    """Determines whether string1 is a permutation of string2, lengths are 
    first compared, then a list comprised of unique values for each letter
    determines whether both strings share the same letters
    pre: input is two strings
    post: returns whether or not the strings are permutations of each other
    """
    
    if equalLengths(string1, string2):
   
        listOfNumbers = generateList(string1)
        
        for i in string2:
            number = ord(i)
            listOfNumbers[number] += 1
            if listOfNumbers[number] == 1:
                print("This is not a permutation. One letter or more differs.")
                return
            else:
                pass
        print("This is a permutation.")
    else:
        print("This is not a permutation. Lengths do not match.")
        
def generateList(arg1):
    
    """Generates a list for each letter in ASCII character set, then stores
    number of times that letter appears in a given string
    pre: input is a string
    post: return list with a value stored for each character in the string
    """
    
    numbersList = [0] * 128
    for i in arg1:
        number = ord(i)
        numbersList[number] += 1
    
    return numbersList
        
def equalLengths(arg1, arg2):
    
    """Determines if two strings are of equal lengths
    pre: input is two strings
    post: returns True if both strings are equal length
    """
    
    count1 = len(arg1)
    count2 = len(arg2)
    
    if count1 != count2: return False
    else: return True
    