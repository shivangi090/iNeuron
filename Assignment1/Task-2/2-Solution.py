#!/usr/bin/env python
# coding: utf-8

# In[6]:


#Question-2
for i in range(5):
    for j in range(i+1):
        print("*",end=" ")
    print()
for i in range(4):
    for j in range(4-i):
        print("*",end=" ")
    print()

