#!/usr/bin/env python
# coding: utf-8

# In[1]:


a=10
b=20
c=a+b
print(c)


# In[3]:


a=8
b=3
c=a+b
d=a-b
e=a*b
f=a/b
g=a%b
print(c)
print(d)
print(e)
print(f)
print(g)


# In[4]:


a=8
b=3
c=a+b
d=a-b
e=a*b
f=a/b
g=a%b
print("addition is:",c)
print("substraction is:",d)
print("multiplication is:",e)
print("Divide is:",f)
print("remainder is:",g)


# In[5]:


a=10
type(a)


# In[6]:


a=10.5
type(a)


# In[7]:


a="10.5"
type(a)


# In[8]:


a=10
float(a)


# In[9]:


a=10.5
int(a)


# In[10]:


a="10.5"
int(float(a))


# In[11]:


a=input("enter the value of a")
b=input("enter the value of b")
c=a+b
print(c)


# In[12]:


a=int(input("enter the value of a"))
b=int(input("enter the value of b"))
c=a+b
print(c)


# In[1]:


a=int(input("enter the value of a"))
b=int(input("enter the value of b"))
c=a+b
d=a-b
e=a*b
f=a/b
g=a%b
print("Additon is:",c)
print("substraction:",d)
print("multiplication is:",e)
print("divide is:",f)
print("remainder is:",g)


# In[6]:


a=int(input("enter the value of a"))
b=int(input("enter the value of b"))
if(a>b):
    print("a is larger than b")
else:
    print("b is larger than a")
    


# In[10]:


a=int(input("enter the value of a"))
b=int(input("enter the value of b"))
if(a>b):
    print("a is larger than b")
elif(a==b):
    print("a and b equal")
else:
    print("b is larger than a")
    


# In[13]:


a=int(input("enter the value of a"))
if(a%2==0):
    print("a is even no")
else:
    print("a is odd no")
    
    


# In[17]:


year=int(input("enter year"))
if(year%4==0):
    print("year is leap year")
else:
    print("year is nort a leap year")
    


# In[ ]:




