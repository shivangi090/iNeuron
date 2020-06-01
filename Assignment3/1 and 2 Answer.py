#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Question-1
try:
    r=5/0
except Exception as e:
    print(e, "is equal to infinity")
else:
    print(r)


# In[14]:


#Question-2
subjects=["Americans","Indians"]
verbs=["play","watch"]
objects=["Baseball","Cricket"]
for i in subjects:
    for j in verbs:
        for k in objects:
            print(i+" "+j+" "+k)

