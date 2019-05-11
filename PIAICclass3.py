#!/usr/bin/env python
# coding: utf-8

# In[1]:


num =  2
num  +=100
num


# In[2]:


num =  3
num*=2
num


# In[3]:


num =  10
num-=2
num


# In[4]:


num = 12*2/4
num


# In[5]:


num = (12*2)/12
num


# In[13]:


name = "Ammar"
age = input("Enter ur age : ")
print ("My name is " + name + " and my age is "+ age)


# In[11]:


name = "Ammar"
age = 21
print ("My name is " + name + " and my age is "+ str(age))


# In[15]:


name = "Ammar"
age =  21
print ("my name is {} and my age is {}".format (name,age))


# In[17]:


name = "Ammar"
age =  21
print ("my name is {1} and my age is {0}".format (name,age))


# In[23]:


a = 10
b = 20 
if(a<b):
    print("hello")
    print("a chota h")
    print("lekin b bra h")
    if (b>a):
        print ("hello")
print("now i am out of if body")


# In[24]:


a = 10
b = 20 
if(a>b):
    print("hello")
    print("a chota h")
    print("lekin b bra h")
print("now i am out of if body")

if (b>a):
    print("hello")


# In[34]:


num = input(" enter the num ")
if (int(num)%2==0):
    print(" even ")
else:
        print(" odd ")


# In[35]:


num = input(" enter the num ")
if (int(num)%2!=0):
    print(" odd ")
else:
        print(" even ")


# In[ ]:




