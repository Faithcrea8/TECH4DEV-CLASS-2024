#!/usr/bin/env python
# coding: utf-8

# Question 1 solution

# In[6]:


def find_maximum_num(lst):
    maximum_value = lst[0]  # Assume the first element is the maximum

    for num in lst:
        if num > maximum_value:
            maximum_value = num

    return maximum_value

# Example:
given_list = [2, 4, 7, 4, 23, 5, 1, 4, 8, 9]
maximum_value = find_maximum_num(given_list)

print(f"The maximum value in the list is: {maximum_value}")


# In[ ]:





# Question 2 solution

# In[7]:


def calculate_average(lst):
    total = sum(lst)
    average = total / len(lst)
    return average

# Example usage:
given_list = [4, 7, 1, 5, 11, 53, 12, 46, 84, 23]
average_value = calculate_average(given_list)

print(f"The average value of the list is: {average_value}")


# In[ ]:





# Question 3 solution

# In[9]:


def print_reverse_order(lst):
    reversed_list = list(reversed(lst))
    print("Original list:", lst)
    print("Reversed list:", reversed_list)

# Example
given_list = [2, 6, 7, 45, 23, 53, 14, 45, 89, 5]
print_reverse_order(given_list)  # here lst = given_list


# In[ ]:





# Question 4 solution

# In[10]:


def compare_lists(list1, list2):
    if len(list1) != len(list2):
        print("False (lists are not the same length)")
        return

    result = all(list1[i] < list2[i] for i in range(len(list1)))
    print(result)

# Example
list_a = [2, 6, 7, 4, 23, 53, 14, 45, 89, 5]
list_b = [3, 8, 9, 5, 24, 54, 15, 46, 90, 6]

compare_lists(list_a, list_b)


# In[ ]:





# Question 5 solution

# In[11]:


def swap_elements(lst, index1, index2):
    if 0 <= index1 < len(lst) and 0 <= index2 < len(lst):
        lst[index1], lst[index2] = lst[index2], lst[index1]
        print(f"List after swapping elements at indexes {index1} and {index2}: {lst}")
    else:
        print("Invalid indices. Please provide valid indices within the range of the list.")

# Example
my_list = [2, 6, 7, 4, 23, 53, 14, 45, 89, 5]
swap_elements(my_list, 2, 5)


# In[ ]:





# Question 6 solution

# In[13]:


def last_index_of_value(lst, value):
    try:
        last_index = len(lst) - 1 - lst[::-1].index(value)
        print(f"The last index of {value} is: {last_index}")
    except ValueError:
        print(f"{value} not found in the list. The last index is -1.")

# Example usage:
my_list = [74, 85, 102, 99, 101, 85, 56]
value_to_find = 85

last_index_of_value(my_list, value_to_find)
def combine_lists(list1, list2):
    combined_list = list1 + list2
    print("Combined List:", combined_list)

# Example usage:
list_a = [2, 6, 7, 4, 23]
list_b = [53, 14, 45, 89, 5]

combine_lists(list_a, list_b)


# In[ ]:





# Question 7 solution

# In[16]:


def last_index_of_value(lst, value):
    last_index = len(lst) - 1 - lst[::-1].index(value) if value in lst  else -1
    print(f"The last index of {value} is: {last_index}")

# Example usage:
my_list = [74, 85, 102, 99, 101, 85, 56]
value_to_find = 85

last_index_of_value(my_list, value_to_find)


# In[ ]:





# Question 8 solution

# In[17]:


def calculate_range(lst):
    min_value = min(lst)
    max_value = max(lst)
    value_range = max_value - min_value + 1

    print(f"The range of values in the list is: {value_range}")

# Example usage:
my_list = [36, 12, 25, 19, 46, 31, 22]
calculate_range(my_list)


# In[ ]:





# Question 9 solution

# In[18]:


def count_elements_between(lst, min_value, max_value):
    count = 0  # Initialize a counter to 0

    # Loop through each number in the list
    for num in lst:
        # Check if the number is between the minimum and maximum values
        if min_value <= num <= max_value:
            count += 1  # If yes, increment the counter

    # Print the final count
    print(f"The count of elements between {min_value} and {max_value} is: {count}")

# Example usage:
my_list = [14, 1, 22, 17, 36, 7, -43, 5]
min_value = 4
max_value = 17

count_elements_between(my_list, min_value, max_value)


# In[ ]:





# Question 10 solution

# In[19]:


def is_sorted(lst):
    # Check if every element is less than or equal to the next one
    sorted_check = all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1))
    print(sorted_check)

# Example usage:
list1 = [16.1, 12.3, 22.2, 14.4]
list2 = [1.5, 4.3, 7.0, 19.5, 25.1, 46.2]

is_sorted(list1)  # Output: False
is_sorted(list2)  # Output: True


# In[ ]:




