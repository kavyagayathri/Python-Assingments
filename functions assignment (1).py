#!/usr/bin/env python
# coding: utf-8

# In[1]:


def sum(a,b):
    return a+b
sum(2,3)


# In[2]:


def mul(a,b):
    return a*b
mul(2,3)


# In[5]:


def div(a,b):
    if a ==0 or b==0:
        print("cannot be divided by zero")
    return a/b
div(8,4)


# In[7]:


def add_all(a,b,c,d,e):
    return a+b+c+d+e
add_all(2,3,4,4,5)


# In[12]:


def sub(a,b):
    return a-b
sub(6,3)


# In[14]:


def modulus(a,b):
    return a%b
modulus(10,3)


# In[15]:


def square(n):
    return n*n
square(9)


# In[16]:


def cube(n):
    return n*n*n
cube(8)


# In[18]:


def maximum(a,b,c):
    if a > b and a> c:
        print("a is greater")
    if b > a and b> c:
        print("b is greater")
    if c> a and  c>b:
        print("c is greater")
maximum(2,3,4)


# In[19]:


def minimum(a,b,c):
    if a< b and a< c:
        print("a is minimum")
    if b < a and b< c:
        print("b is minimum")
    if c< a and  c<b:
        print("c is minimum")
minimum(2,3,4)


# In[20]:


def avg(a,b,c):
    return a+b+c/3
avg(2,3,4)


# In[3]:


def power(b):
    return b**2
power(90)


# In[13]:


def add_all(*a):
    sum=0
    for i in a:
        sum+=i
    return sum
    


# In[14]:


add_all(1,2,3,4,5,6)


# In[3]:


def find_mini(*args):
    return min(args)
find_mini(23,45,67)          


# In[4]:


def find_max(*args):
    return max(args)
find_max(90,67,89,77)


# In[7]:


def avg(*args):
    for i in args:
        return sum(args)/len(args)


# In[8]:


avg(23,45,66,77,86,46,78)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




