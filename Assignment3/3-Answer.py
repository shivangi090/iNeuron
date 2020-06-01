#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
def vander(arr, col, boole):
    if boole==True:
        mat=np.array([x**(col-1-i) for x in arr for i in range(col)]).reshape(len(arr), col)
    else:
        mat=np.array([(x**i) for x in arr for i in range(col)]).reshape(len(arr),col)
    return mat
print('***Increasing***')
print(vander([1,2,3,4,5], 5, True))
print('***decreasing***')
print(vander([1,2,3,4,5], 5, False))

