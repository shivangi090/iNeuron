#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Question-1.1
def func(a,b):
    return a*b
def myreduce(func,numbers):
    r=numbers[0]
    for i in numbers[1:]:
        r=func(r,i)
    return(r)
numbers=list(map(int,input().split()))
r=myreduce(func,numbers)
print(r)


# In[2]:


#Question-1.2
def func(a,b):
    return a if a>b else b
def myfilter(func,numbers):
    r=numbers[0]
    for i in numbers[1:]:
        r=func(r,i)
    return r
numbers=list(map(int,input().split()))
r=myfilter(func,numbers)
print(r)

