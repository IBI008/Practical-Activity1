#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Print the price
sales_price = 24500
print(total_price)


# In[2]:


# total_price not define, it suppose to be sales_price
# using a wrong name is the cause of the error
# The error can be interpreted as NameError

# Solution to print the price
sales_price = 24500
print(sales_price)


# In[3]:


# Print a text string verbatim
print "My name is James Bond"


# In[4]:


# There is an error because there is a missing parentheses at the front of print.
# there is no bracket before and after the string
# The error can be interpreted as SyntaxError

# Solution to print a text string verbatim
print("My name is James Bond")


# In[8]:


# Determine if x is greater than 10
x = 11
if x > 10:
print('X is greater than 10')
else:
    print('x is not greater than 10')


# In[6]:


# There is missing indentation before the first print
# The cause of the error was the failure to observe four gap before typing print in line 4
# The error can be interpreted as IndentationError

# Solution to Determine if x is greater than 10
x = 11
if x > 10:
    print('x is greater than 10')
else:
    print('x is not greater than 10')


# In[9]:


# Create the variable list_a
list_a = [1,2,3,4,'Ayaan', 'Hirsi']

list_a[11]


# In[10]:


# The reason for the error was that the list index is not up to 11, total index is 6
# The cause of the error was the unability to get the list index correctly
# The error message can be interpreted as IndexError

# Solution to Create the variable list_a
list_a = [1,2,3,4,'Ayaan', 'Hirsi']

list_a
print('list_a')


# In[ ]:




