#!/usr/bin/env python
# coding: utf-8

# In[14]:


#Question-1.2
def filter_long_words(l,n):
    o=[]
    d={w:len(w) for w in l}
    for key,value in d.items():
        if value>n:
            o.append(key)
    return o
l=list(map(str,input().split()))
n=int(input("Enter a number"))
op=filter_long_words(l,n)
op

