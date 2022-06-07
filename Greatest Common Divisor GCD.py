#!/usr/bin/env python
# coding: utf-8

# In[4]:


def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)
print(gcd(24,60))

#CodeByVaishnaviUdayNehe


# In[ ]:




