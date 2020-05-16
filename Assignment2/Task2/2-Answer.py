#!/usr/bin/env python
# coding: utf-8

# In[15]:


#Question-2.1
def length(a):
    return len(a)
l=list(map(str,input().split()))
op=list(map(length,l))
op


# In[17]:


#Question-2.2
def vowel(a):
    if a in ['a','e','i','o','u']:
        return True
    else:
        return False
st=input("Enter a string")
for i in st:
    print(i,":",vowel(i))

