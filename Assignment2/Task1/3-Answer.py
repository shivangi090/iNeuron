#!/usr/bin/env python
# coding: utf-8

# In[11]:


#Question3
def longestWord(n):
    d={w:len(w) for w in n}
    l=[]
    m=max(d.values())
    for key,value in d.items():
        if value==m:
            l.append(key)
    return l
l=list(map(str,input().split()))
print(longestWord(l))


