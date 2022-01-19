#!/usr/bin/env python
# coding: utf-8

# # data types

# In[2]:


num = 25
type(num)


# In[3]:


str1 = "Tracy"
type(str1)


# In[4]:


num = 23.23
type(num)


# In[5]:


tr = True
type(tr)


# In[6]:


#list
items = []
type(items)


# In[9]:


items = []
items.append(50)
print(items)
items.append(46)
print(items)
items.append(49)
print(items)
items.pop(1)
print(items)
#inserting an element
items.insert(0, 53)
print(items)
items.insert(1, 45)
print(items)
#removing an element
items.remove(50)
print(items)
len(items)
sum(items)


# In[13]:


#sets
set2 = set()
type(set2)


# In[16]:


set2 = set()
set2.add(0)
print(set2)
set2.add(1)
print(set2)
#removing an element
set2.remove(0)
print(set2)
len(set2)

