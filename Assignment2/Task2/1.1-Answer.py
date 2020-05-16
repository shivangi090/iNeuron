#!/usr/bin/env python
# coding: utf-8

# In[12]:


#Question-1.1
from math import sqrt
class sides_triangle:
    def __init__(self):
        self.a=float(input("Enter the first side"))
        self.b=float(input("Enter the first side"))
        self.c=float(input("Enter the first side"))
class area_triangle(sides_triangle):
    def __init__(self):
        sides_triangle.__init__(self)
    def cal_area(self):
        s=(self.a+self.b+self.c)/2
        arr=(s*(s-self.a)*(s-self.b)*(s-self.c))**0.5
        return arr
        
        
a=area_triangle()
print(a.cal_area())

