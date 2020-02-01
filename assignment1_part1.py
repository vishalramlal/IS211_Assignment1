#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Assignment 1 Part 1


class ListDivideException(Exception):
    pass

OK = []

def listDivide(numbers, divide = 2):
    for i in numbers:
        if i%divide==0:
            OK.append(i)
            if OK < 0:
                raise ListDivideException()
            else:
                return len(OK)

            
    
def testListDivide(listDivide):
    listDivide([1,2,3,4,5])
    listDivide([2,4,6,8,10])        
    listDivide([30,54,63,98,100], divide=10)
    listDivide([])
    listDivide([1,2,3,4,5], 1)
    
testListDivide

