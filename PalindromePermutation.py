#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 10:27:03 2019

@author: Jenny
"""
        
        
def is_palindrome(phrase):
    
    """ Case-sensitive and punctuation sensitive function that returns 
    whether a given phrase is a permutation of a palindrome 
    pre: takes one string
    post: returns True when the phrase is a palindrome"""
    
    # remove hashtag below to make this function not case-sensitive
    # phrase = phrase.lower
    phrase = phrase.replace(" ", "")
    map_hash = make_hash_table(phrase)
    return check_max_one_odd(map_hash)

def _get_hash(key):
    
    """Returns a key for a given letter based on its value in the 
    ASCII character set"""
    
    return ord(key)
        
def make_hash_table(phrase):
    
    """Makes a hash table for the phrase that tracks the number of times a 
    letter in the ASCII character set appears in the phrase
    pre: takes one string
    post: returns a hash table for the string
    """
    
    # creates a hash table with a 0 at every value in the ASCII character set
    map_hash = [0] * 128    
    for letter in phrase:
        key = _get_hash(letter)
        if map_hash[key] == 0:
            map_hash[key] = list([key, 1])
        else:
            if map_hash[key][0] == key:
                map_hash[key][1] += 1
                
    return map_hash
                    
def check_max_one_odd(table):
    
    """If there is at most one letter that appears only once in the phrase, 
    the phrase is a palindrome
    pre: takes a hash table
    post: returns True if the phrase is a palindrome
    """
    
    found_odd = 0
    
    # checks to see there is at most one value that is not divisible by 2 
    # in the phrase
    for i in range(0, len(table)-1):
        if type(table[i]) is list:
            if table[i][1] % 2 == 1:
                found_odd += 1
    
    if found_odd >= 2:
        return False
    else:
        return True