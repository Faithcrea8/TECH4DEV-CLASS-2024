#!/usr/bin/env python
# coding: utf-8

# Question No 12

# In[2]:


def smallestLargest():
    try:
        count = int(input("How many numbers do you want to enter? "))

        while count <= 0:
            print("Please enter a valid number greater than 0.")
            count = int(input("How many numbers do you want to enter? "))

        numbers = []

        for i in range(1, count + 1):
            while True:
                try:
                    num = int(input(f"Number {i}: "))
                    numbers.append(num)
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid numeric value.")

        if numbers:
            smallest = min(numbers)
            largest = max(numbers)
            print(f"Smallest = {smallest}")
            print(f"Largest = {largest}")
        else:
            print("No numbers entered.")

    except ValueError:
        print("Invalid input. Please enter valid numeric values.")

smallestLargest()


# In[ ]:





# Question Number 13

# In[6]:


def printAverage():
    total = 0
    count = 0

    while True:
        num = float(input("Type a number: "))

        if num < 0:
            if count > 0:
                average = total / count
                print(f"Average was {average}")
            else:
                print("")
            break

        total += num
        count += 1

# Example usage:
printAverage()


# In[ ]:





# Question Number 14

# In[7]:


def numUnique(num1, num2, num3):
    unique_numbers = set([num1, num2, num3])
    return len(unique_numbers)

# Example
result1 = numUnique(18, 3, 4)
print(result1)

result2 = numUnique(6, 7, 6)
print(result2)  


# In[ ]:





# Question Number 15

# In[10]:


import random

def rolldice():
    return random.randint(1, 6)

def getaseven():
    tries = 0

    while True:
        dice1 = rolldice()
        dice2 = rolldice()

        total = dice1 + dice2
        print(f"{dice1} + {dice2} = {total}")

        tries += 1

        if total == 7:
            print(f"You won after {tries} tries!")
            break

#Example
getaseven()


# In[ ]:





# In[ ]:




