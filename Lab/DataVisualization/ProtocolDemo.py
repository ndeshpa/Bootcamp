# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 09:32:01 2018

@author: Nita
"""

class ProtocolDemo:
    def __init__(self, greetings):
        self.__greetings = greetings
    
    def __len__(self):
        return len(self.__greetings)
    
    def __str__(self):
        msg = ""
        for e in self.__greetings:
            msg += e + " "
        return msg
    
           
        
all_greetings=ProtocolDemo(['Hello', 'Ola', 'Hi', 'Howdy'])

print("Number of Elements: " , len(all_greetings))
print("String Representation: " , str(all_greetings))