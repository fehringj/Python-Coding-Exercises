#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 12:50:25 2019

@author: Jenny
"""
# Requires Exceptions.py
from Exceptions import *

class Animal:
    
    """Creates a separate class Animal that stores name and time of entry
    to the shelter as individual nodes"""
    
    def __init__(self, name, timestamp):
        
        self.name = name
        self.next = None
        self.timestamp = timestamp
        
    def __lt__(self, other):
        
        return self.timestamp < other
    
    def __gt__(self, other):
        
        return self.timestamp > other
    
    def __ge__(self, other):
        
        return self.timestamp > other or self.timestamp == other
        
class AnimalQueue:
    
    """Class that creates a queue from nodes of from the AnimalQueue class"""
    
    def __init__(self):
        
        self.size = 0
        self.first = None
        self.last = None
        
    def __len__(self):
        
        return self.size
    
    def add(self, animal, time):
        
        """Add a node to the queue
        pre: input animal name and time of arrival at the shelter in 
        24 hour format
        post: node added to next available space in the queue"""
        
        queue_node = Animal(animal, time)
        if self.last is not None:
            self.last.next = queue_node
            self.size += 1
        
        self.last = queue_node
        
        if self.first is None:
            self.first = queue_node
            self.size += 1
            
    def is_empty(self):
        
        """Function to determine if queue is empty
        post: returns True if queue is empty"""
        
        return self.first is None
    
    def dequeue(self):
        
        """Return first value added to the queue"""
        
        return self.first.name
    
    def remove(self):
        
        """Removes first value added to the queue"""
        
        if self.first is None:
            raise NoSuchElement
            
        node = self.first.timestamp
        self.first = self.first.next
        if self.first is None:
            self.last = None
        self.size -= 1
            
        return node
    
    def peek_name(self):
        
        """Returns the name of the first animal added to the queue/brought to
        the shelter"""
        
        if self.first is None:
            raise EmptyQueueError
            
        return self.first.name
    
    def peek_time(self):
        
        """Returns the time that the first animal arrived at the shelter/first
        time added to the queue"""
        
        if self.first is None:
            raise EmptyQueueError
            
        return self.first.timestamp
    
    # In an unordered queue this will return the highest priority animal
    # i.e. the animal that came in earliest
    def priority_animal(self):
        
        """Function to determine if first priority animal is not at the head
        of the queue
        post: returns name and time of first animal at shelter, but not 
        necessarily first animal in queue"""
        
        current = self.first
        minimum = self.first
        
        while current is not None:
            if current.timestamp < minimum.timestamp:
                minimum = current
            current = current.next
            
        item = minimum.name, minimum.timestamp
        
        return item

def print_all_animals(cats, dogs):
    
    """Merges queue of cats and queue of dogs into one list ordered by priority
    based on time of arrival at shelter
    post: prints names of cats and dogs in order of arrival time"""
    
    cat = cats.first
    dog = dogs.first
    
    for i in range(len(cats) + len(dogs)):
        if cat is not None and cat.timestamp < dog.timestamp:
            print(cat.name, cat.timestamp)
            cat = cat.next
        elif dog is not None:
            print(dog.name, dog.timestamp)
            dog = dog.next
            
def print_queue(queue):
    
    """Prints one of the queues
    post: prints the name and time of arrival for each animal in queue"""
    
    queue_first = queue.first
    
    while queue_first is not None:
        print(queue_first.name, queue_first.timestamp)
        queue_first = queue_first.next
            
def dequeue_any(cats, dogs):
    
    """Dequeues the highest priority animal of both queues
    post: returns the first animal to arrive at shelter of the dogs and the 
    cats"""
    
    cat = cats.first
    dog = dogs.first
    
    if cat is not None and cat.timestamp < dog.timestamp:
        print(cat.name)
    elif dog is not None:
        print(dog.name)
    else:
        print("No animals are currently in the queue.")
      
        
    
# Driver code

cats = AnimalQueue()
dogs = AnimalQueue()


cats.add("Lilo", 5.45)
cats.add("Kim", 7.53)
cats.add("Wendy", 13.21)
cats.add("Max", 17.09)
print(cats.priority_animal())
print_queue(cats)
cats.dequeue()

dogs.add("Fido", 6.32)
dogs.add("Tim", 10.12)
dogs.add("Spot", 14.55)
dogs.add("Liam", 15.00)
dogs.add("Lady", 21.13)
dogs.dequeue()
print_queue(dogs)

print_all_animals(cats, dogs)
dequeue_any(cats, dogs)