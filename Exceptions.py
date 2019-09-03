#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 12:18:50 2019

@author: Jenny
"""

class Error(Exception):
    """ Base class for other exceptions """
    pass
    
class EmptyStackError(Exception):
    """ Raised when trying to access values from an empty stack """
    pass

class NoSuchElement(Exception):
    """ Raised when requesting an element that does not exist """
    pass