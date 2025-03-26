#!/usr/bin/env python
# coding: utf-8

# In[11]:


class car():
    def __init__(self,brand,model,year,color):
        self.brand= brand
        self.model= model
        self.year=year
        self.color=color
car1=car("bmw","44c","2023","blue")
car1.brand
car1.color      


# In[15]:


class Person():
    def __init__(self,name,age):
        self.name=name
        self.age=age
person1=Person("kavya",23)
person1.name


# In[17]:


class book():
    def __init__(self,name,author,price):
        self.name=name
        self.author=author
        self.price=price
book1=book("400days","chethan bhagath",450)
book2=book("ramayan","amish triparti",800)
book2.name


# In[19]:


class mobile():
    def __init__(self,brand,model,price,color):
        self.brand= brand
        self.model= model
        self.price=price
        self.color=color
mobile1=mobile("oppo","t4",8000,"black")
mobile2=mobile("vivo","f6",5500,"green")
mobile2.model


# In[22]:


class laptop():
    def __init__(self,brand, ram_size, processor,color):
        self.brand= brand
        self.ram_size= ram_size
        self.processor=processor
        self.color=color
laptop1=laptop("lenovo","80gb","intel","black")
laptop1.processor


# In[24]:


class movie():
    def __init__(self,title, genre,rating):
        self.title=title
        self.genre=genre
        self.rating = rating
movie1=movie("rrr","fiction",4.5)
movie2=movie("hridayam","fiction",5)
movie2.title


# In[ ]:




