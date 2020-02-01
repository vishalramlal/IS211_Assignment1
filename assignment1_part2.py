#!/usr/bin/env python
# coding: utf-8

# In[12]:


#Assignment 1 Part 2


class Book(object):
    def __init__(self):
        self.author = ""
        self.title = ""
    def display(self):
        binfo = (self.title + ", written by " + self.author)
        return binfo
        
    
abook1 = Book()
abook2 = Book()
abook1.title = "Of Mice and Men"
abook1.author = "John Steinbeck"
abook2.title = "To Kill a Mockingbird"
abook2.author = "Harper Lee"

print(abook1.display())
print(abook2.display())

