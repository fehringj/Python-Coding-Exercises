#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 12:39:33 2019

@author: Jenny
"""

def shortest_string(string):
    
    """Generates a compressed string for a given series of letters and outputs
    the shorter string of the two
    ex: aaabbbcccc -> a3b3c4
    pre: input a string
    post: returns either the compressed string or original depending on which 
    is shorter
    """
    
    map_hash = make_hash_table(string)
    print(map_hash)
    compressed_string = compress_string(map_hash)
    return check_length(compressed_string, string)

def _get_hash(key):
    
    """Generates a key for a given input letter based on its position in 
    the ASCII character set
    pre: input is a letter of the supplied phrase
    post: returns a key value for the letter
    """
    
    return ord(key)
        
def make_hash_table(sequence):
    
    """Creates a hash table for the inputed sequence of letters
    pre: input is a string
    post: returns a hash table that indicates how many times each letter 
    appeared in the string
    """
    
    map_hash = [0] * 128    
    for letter in sequence:
        key = _get_hash(letter)
        if map_hash[key] == 0:
            map_hash[key] = list([letter, 1])
        else:
            if map_hash[key][0] == letter:
                map_hash[key][1] += 1
                
    return map_hash

def compress_string(table):
    
    """Generates a compressed string
    pre: input is hash table for the string
    post: returns a compressed version of the string
    """
    
    compressed = ""
    for i in range(0, len(table)-1):
        if type(table[i]) is list:
            compressed += table[i][0] + str(table[i][1])
    return compressed

def check_length(compressed, original):
    
    """Determines whether the original string is shorter than the compressed
    pre: input is the compressed and original strings
    post: returns the shorter string of the two
    """
    
    if len(compressed) < len(original):
        return compressed
    else:
        return original