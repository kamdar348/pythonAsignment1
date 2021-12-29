#!/usr/bin/env python
# coding: utf-8

# In[8]:


#1. write a python program to print the following string in  specific format(see the out put),
# Twinkle, twinkle, little star,
#           How I wonder what you are!
#                   Up above world so high,
#                    Like a diamond in the sky,
# Twinkle, twinkle, little star,
#           How I wonder what you are

print("Twinkle, twinkle, little star,");
print("          How I wonder what you are!");
print("                  Up above world so high,");
print("                   Like a diamond in the sky,");
print("Twinkle, twinkle, little star,");
print("          How I wonder what you are!");


# In[7]:


#2. Write a python program to get the python version you are using
import sys
print("Python version")
print (sys.version)
print("Version info.")
print (sys.version_info)


# In[6]:


#3. write a python program to display current date and time
import datetime
now = datetime.datetime.now()
print("current date and time is:");
print(now.strftime("%Y-%m-%d  %H,%M,%S"));


# In[5]:


#  4. Write a Python program which accepts the radius of a circle from the user and compute the area.
from math import pi
r = float(input ("Input the radius of the circle : "))
print ("The area of the circle with radius " + str(r) + " is: " + str(pi * r**2))


# In[3]:


# 5. Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them.
fname = input("Input your First Name : ")
lname = input("Input your Last Name : ")
print ("Hello  " + lname + " " + fname)


# In[2]:


#6. write a python program which takes two input from user and print them in addotion
sum1 = int(input("Enter number 1:"));
sum2 = int(input("Enter number 2:"));
result = sum1 + sum2;
print (sum1, "+" ,sum2, "=", result,);


# In[ ]:




