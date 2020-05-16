#!/usr/bin/env python
# coding: utf-8

# In[6]:


#Question-2.1
a=list(input().upper())
print(a)


# In[5]:


#Question-2.2
l=[(i*chr(a)) for a in range(120,123) for i in range(1,5)]
l


# In[7]:


#Question2.3
l=[(i*chr(a)) for i in range(1,5) for a in range(120,123)]
l


# In[8]:


#Question-2.4
s=[2,3,4]
matrix = [[[j] for j in range(s[a],s[a]+3)] for a in range(3)]
print(matrix)


# In[9]:


#Question-2-5
s=[2,3,4,5]
matrix = [[j for j in range(s[a],s[a]+4)] for a in range(4)] 
print(matrix)


# In[10]:


#Question-2.6
matrix=[(j,i) for j in range(1,4) for i in range(1,4)]
matrix






