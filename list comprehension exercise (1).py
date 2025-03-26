#!/usr/bin/env python
# coding: utf-8

# In[3]:


a=[i*i for i in range(1,11)]
a


# In[4]:


b=[i for i in range(1,21) if i%2==0]
b


# In[5]:


c=[i for i in range(1,11)]
c


# In[8]:


d=[i*i*i for i in range(1,11)]
d


# In[10]:


l=["Hello", "World", "Python"]
e=[i.upper() for i in l]
e


# In[11]:


s="Python is fun"
f = [i for i in s]
f


# In[12]:


l=[0, 10, 20, 30, 40]
d=[i*9/5+32 for i in l]
d


# In[13]:


l=["dog", "elephant", "cat", "rabbit"]
d=[i for i in l if len(i)>3]
d


# In[14]:


o=[i for i in range(1,51) if i%3==0 and i%5==0]
o


# In[16]:


l=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
s=[i for i in l if i%2!=0]
s


# In[21]:


s="hello world"
f=[i for i in s if i in "aeiouAEIOU"]
f


# In[22]:


l=["Hello", "WORLD", "Python", "LiSt"]
e=[i.lower() for i in l]
e


# In[23]:


r=[i for i in range(1,51) if i%2==0]
r


# In[25]:


p=[5, 12, 17, 9, 3, 21, 30]
g= [ i for i in p if i>=10]
g


# In[30]:


f=[i for i in range(1,21) if i%3==0]
f


# In[31]:


g=[i*i for i in range(1,11) if i%2==0]
g


# In[32]:


l= ["apple", "banana", "cherry", "date"]
h=[i[0] for i in l]
h


# In[ ]:




