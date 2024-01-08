#!/usr/bin/env python
# coding: utf-8

# No 1 question

# In[1]:


iterations =[1,2,3,4,5,6,7,8]
for i in iterations:
    if i==iterations[0] or i==iterations[-1]:
        print("+ - - - - +")
    elif i % 2==0:
        print("\\\t/")
    else:
        print("/\t\\")
    #there is always a \ before a special character since its not part of the code


# In[ ]:





# No 2 Question

# In[1]:


num=range(0,5)
for i in num:
       print("**********")   
   
    
    


# 

# Question No 3

# In[2]:


i=1
for i in range(1,7):
    print(i)


    


# In[37]:


for i in range(1,7):
    print(i*2)


    


# In[ ]:





# In[39]:


for i in range(1,7):
    print(i*2)


# In[7]:


k=30
for i in range(1,7):
    if i==1:
        print(k)
    else:
        k=k-10
        print(k)
        
        


    


# In[9]:


k=-7
for i in range(1,7):
    if i==1:
        print(k)
    else:
        k=k+4
        print(k)
        
        


    


# In[ ]:





# In[6]:


k=4
for i in range(1,7):
    if i==1:
        print(k)
    else:
        k=k+15
        print(k)
        
        


    


# In[ ]:





# In[10]:


k=97
for i in range(1,7):
    if i==1:
        print(k)
    else:
        k=k-3
        print(k)
        
        


    


# In[11]:


k=-4
for i in range(1,7):
    if i==1:
        print(k)
    else:
        k=k+18
        print(k)
        
        


    


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# 

# 

# Question No 4

# In[2]:


# n represents the num er of desired occurence and printing of i
# j represents the actual number in the occurrence
n = int(input("Enter number of rows: "))

for i in range(1,n+1):
    for j in range(1, i+1):
        print(i, end="")
    print()


# In[ ]:





# Question No 5

# In[47]:


def pay (salary: float, hours_worked: int) -> float:
    normal_hours = 8
    overtime_rate = 1.5

    if hours_worked <= normal_hours:
        return (salary) * (hours_worked)
    else:
        normal_pay =(salary) * (normal_hours)
        overtime_pay = (salary) * overtime_rate * (hours_worked - normal_hours)
        total_pay = normal_pay + overtime_pay
        return total_pay

# stated sample excercise
result1 = pay(5.50, 6)
result2 = pay(4.00, 11)

print (result1)
print (result2)


# In[ ]:





# Question No 7

# In[48]:


import math

def area(radius):
    return math.pi * radius**2

#example:
result = area(2.0)
print(result)


# In[ ]:





# Question No 7

# In[55]:


low = 1
high = 1001
sum = 0
for i in range(low,high):
    sum += i
 
    print("sum = " , sum)


# In[57]:


# modified version of the above codes to acccept inputs within specified range
low = int(input("low? "))
high = int(input("high? "))
sum_result = 0

for i in range(low, high):
    sum_result += i

print("sum = ", sum_result)


# In[ ]:





# Question No 8

# In[59]:


sum_result = 0

while True:
    user_input = input("Enter a number (type 0 to stop): ")

    try:
        number = int(user_input)
        sum_result += number
    except ValueError:
        print("Invalid input. Please enter a valid number.")

    if number == 0:
        break

print("Sum of the numbers entered:", sum_result)


# In[ ]:





# Question No 9

# In[60]:


sum_result = 0

while True:
    user_input = input("Enter a number (type 0 to stop): ")

    try:
        number = int(user_input)
        sum_result += number
    except ValueError:
        print("Invalid input. Please enter a valid number.")

    if number == -1:
        break

print("Sum of the numbers entered:", sum_result)


# In[ ]:





# Question No 10

# In[61]:


def repl(word, repetitions):
    if repetitions <= 0:
        return ""
    else:
        return word * repetitions

# Example usage:
result = repl("hello", 3)
print(result)  # Output: "hellohellohello"

result_zero_reps = repl("world", 0)
print(result_zero_reps)  # Output: ""


# QUestion No 11

# In[76]:


def printRange(start, end):
    result = ""

    if start < end:
        # Increasing sequence
        result = " ".join(str(num) for num in range(start, end + 1))
    elif start > end:
        # Decreasing sequence
        result = " ".join(str(num) for num in range(start, end - 1, -1))
    else:
        # Same number
        result = str(start)

    print(result)

# Example usage:
printRange(2, 7)
# Output: 2 3 4 5 6 7

printRange(19, 11)
# Output: 19 18 17 16 15 14 13 12 11

printRange(5, 5)
# Output: 5


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




