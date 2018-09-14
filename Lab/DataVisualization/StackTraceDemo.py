# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 16:24:22 2018

@author: Nita
"""

def func1(msg):
    print(msg)
    print("Calling func2")
    func2()
    
def func2():
    print("Calling func3")
    func3()
    
def func3():
    raise Exception("Raising exception in func3")
    
func1("Calling func1")

