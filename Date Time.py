#!/usr/bin/env python
# coding: utf-8

# In[1]:


from datetime import time

t = time(14, 42, 5, 566)
print(t)


# In[2]:


print("hour =", t.hour)
print("minute =", t.minute)
print("second =", t.second)
print("microsecond =", t.microsecond)


# In[7]:


dt = datetime(2019, 1, 28, 23, 55, 59, 1023)


# In[10]:


print("year=", dt.year)
print("month=", dt.month)
print("day=", dt.day)
print("hour =", dt.hour)
print("minute =", dt.minute)
print("second =", dt.second)
print("microsecond =", dt.microsecond)


# In[11]:


# Printing current year, month and day
from datetime import date

# Date object of today's date
today = date.today()

print("Current year:", today.year)
print("Current month:", today.month)
print("Current day:", today.day)


# In[12]:


# Extract the name of the day from a DateTime object
from datetime import datetime

day = datetime(2017, 1, 28)
# This is the code to return the full day name
day.strftime('%A') 
'Saturday'


# In[ ]:




