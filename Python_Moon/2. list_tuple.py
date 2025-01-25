
# Advanced Python: Lists and Tuples

"""
Author: Kalim Amzad Chy
Email: kalim.amzad.chy@gmail.com

This Python script is designed to provide an in-depth understanding of Python lists and tuples.
We will explore:
1. Lists - Creation, accessing elements, operations, and methods.
2. Tuples - Characteristics, usage, and differences from lists.
3. Advanced applications including 1D and 2D lists, and lists with mixed data types.

Each section includes detailed explanations, examples, and challenging assignments.
"""

# Section 1: Python Lists
# -----------------------
# Lists in Python are ordered, mutable (changeable), and allow duplicate elements.

# Example 1: Creating Lists
simple_list = [8, 2, 9, 4, 5]
mixed_list = [1, "Hello", 3.14, True]
temp_list = []  # Empty list
empty_list = list()

# 2D List (List of Lists)
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Accessing Elements
# You can access elements by their index, which starts at 0.
first_element = simple_list[2]  # Outputs 9
second_row_first_col = matrix[1][2]  # Outputs 4
list_range = simple_list[1:4] # Outputs [2, 9, 4]
# List stepping, also known as slicing with a step

# list[start:end:step] (syntax) 

# list_stepping = simple_list[1:7:2]


list_stepping = simple_list[::2]
# print(first_element)
# print(second_row_first_col)
# print("List Stepping: ", list_stepping)
# print("List Range: ", list_range)

# List Operations
# Adding elements
# print("Before Apprend Operation: ", simple_list)
simple_list.append(6)  # Adds 6 to the end
# print("After Append operation: ", simple_list)

simple_list.insert(2, 6)  # Inserts 0 at the beginning
# print("After Insert operation: ", simple_list)

# Removing elements
simple_list.remove(6)  # Removes the first occurrence of 6
# print("After Remove operation: ", simple_list)
popped_element = simple_list.pop()  # Removes and returns the last element
# print("Popped element:", popped_element)
# print("After Pop operation: ", simple_list)

# List Methods
# Join lists
combined_list = simple_list + mixed_list
# print("Combined List: ", combined_list)

# Sort lists
simple_list.sort()  # Sorts the list in place
# print("Sorted List: ", simple_list)

# Copy a list
duplicate_list = simple_list

duplicate_list.append(7)
# print("simple_list id", id(simple_list), "duplicate_list id: ", id(duplicate_list))
# print("Duplicate List: ", duplicate_list)
# print("Simple List: ", simple_list)

list_copy = simple_list.copy()
list_copy.append(8)
# print("simple_list id", id(simple_list), "list_copy id: ", id(list_copy))
# print("List Copy: ", list_copy)
# print("Simple List: ", simple_list)

# Get the number of elements
list_length = len(simple_list)

# Assignment 1: Create a 2D list representing a 3x3 matrix and perform operations like accessing, modifying, and iterating through it.
# Write your code below:

my_new_list = [ [100,200,300] , [400,500,600] , [700,800,900]]

first_row_third_col = my_new_list[0][2]
print("First Row Third Col" , first_row_third_col)
my_new_list[2][0] = 750
print("After modify list : " , my_new_list)

for row in my_new_list:
    for col in row:
        print(col)
    print()

# Section 2: Python Tuples
# ------------------------
# Tuples are ordered collections like lists but are immutable (cannot be changed after creation).

# Example 2: Creating and Using Tuples
simple_tuple = (1, 2, 3, 4, 5)
mixed_tuple = (1, "Hello", 3.14, True)
temp_tuple = ()  # Empty tuple
empty_tuple = tuple()


# simple_tuple[2] = 76768  # This will raise TypeError as tuples are immutable
print(simple_tuple)

# Accessing elements
first_tuple_element = simple_tuple[0]

# Tuples are immutable
# Trying to change an element like below will raise a TypeError
# simple_tuple[0] = 0

# Tuples can be used as keys in dictionaries because of their immutability
tuple_dict = {simple_tuple: "My Tuple"}

# Assignment 2: Create a tuple with mixed data types and demonstrate its potential use cases in data structures like dictionaries.
# Write your code below:

new_mixed_tuple = ("C201077" , "Irfan Chowdhury" , 3.55 , False)
new_tuple_dict = {new_mixed_tuple: "Student Info "}
print(new_tuple_dict[new_mixed_tuple])


# Section 3: Advanced Applications
# --------------------------------
# Dealing with more complex list and tuple structures for real-world applications.

# Example 3: Advanced List Operations
# Filtering with list comprehensions
# even_numbers = [x for x in simple_list if x % 2 == 0]

# for x in simple_list:
#     if x%2==0:
#         print("Even: ", x)

# even_numbers = [x for x in simple_list if x % 2 ==0]
# print(even_numbers)

# fruits = ["Apple", "Banana", "Orange", "Grapes", "Pineapple", "Mango", "Strawberry", "Watermelon", "Blueberry", "Cherry"]
# new_fruits = []

# new_fruits = [fruit for fruit in fruits if 'a' in fruit ]
# print(new_fruits)




# Nested list comprehensions for 2D list transformations
incremented_matrix = [[cell + 1 for cell in row] for row in matrix]

# Assignment 3: Create a list of tuples, where each tuple contains a student's name and their grade. Sort this list by grades.
# Write your code below:

students_information = [
    ("John Kabir" , 3.45),
    ("Hasan Kabir" , 2.89),
    ("Milton Kabir" , 3.88),
    ("Jashim Kabir" , 3.49),
    ("Newton Sheli" , 4.00)
]


print("Before sorting : " , students_information)
# sorted():  Doesn't modify the original list
sorted_students_information = sorted(students_information , key=lambda  student:student[1])  
print("After sorting : " , sorted_students_information)

# sort() : Modify the original list
students_information.sort(key= lambda student:student[1])
print("Modify the original list: " , students_information)


# Congratulations on completing the advanced section on Python lists and tuples!
# Review the assignments, try to solve them, and check your understanding of these versatile data structures.
