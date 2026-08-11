# List: A list in python is a collection of items in ordered, changeable, and allows duplicate values. Lists are written with square brackets.
my_list = [1, 2, 3, 4, 5]
print(my_list)
print("---------------")

# Lists one of the most verstile data struture in python and are used to store multiple items in single variable.
# string of items in a list are separated by commas and enclosed within square brackets.
#list of strings
my_list = ["apple", "banana", "cherry"] 
print(my_list)
print("---------------")

#list of integers
my_list = [1, 5, 7, 9, 3]
print(my_list)
print("---------------")

#list of mixed data types
my_list = ["abc", 34, True, 40, "male"]
print(my_list)
print("---------------")

#Nested list: A list can also contain other lists, this is called nested list.
my_list = ["mouse", [8, 4, 6], ['a']]
print(my_list)

#Accessing list items: You can access the list items by referring to the index number.
my_list = ["apple", "banana", "cherry"]
print(my_list[0])  # Output: apple
print(my_list[1])  # Output: banana

#Accessing nested list items: You can access the items of a nested list by referring to the index number of the list, followed by the index number of the item inside that list.
my_list = ["mouse", [8, 4, 6], ['a']]
print(my_list[0])      # Output: mouse
print(my_list[1])      # Output: [8, 4, 6]  
print(my_list[2])      # Output: ['a']

# Negative indexing: Negative indexing means beginning from the end, -1 refers to the last item, -2 refers to the second last item etc.
my_list = ["apple", "banana", "cherry"]
print(my_list[-1])  # Output: cherry
print(my_list[-2])  # Output: banana

# Range of indexes: You can specify a range of indexes by specifying where to start and where to end the range.
my_list = ["apple", "banana", "cherry", "date", "elderberry"]
print(my_list[2:5])  # Output: ['cherry', 'date', 'elderberry']

# List length: To determine how many items a list has, use the len() function.
my_list = ["apple", "banana", "cherry"]
print(len(my_list))  # Output: 3

# List Sorting: Lists have a built-in sort() method that sorts the list ascending by default.
my_list = [3, 1, 4, 2, 5]
my_list.sort()
print(my_list)  # Output: [1, 2, 3, 4, 5]

# List Reverse: The reverse() method reverses the current sorting order of the elements.
my_list = [3, 1, 4, 2, 5]
my_list.reverse()
print(my_list)  # Output: [5, 2, 4, 1, 3]

# List Copy: You cannot copy a list simply by typing list2 = list1, because list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2. There are ways to make a copy, one way is to use the built-in List method copy().
my_list = ["apple", "banana", "cherry"]
list2 = my_list.copy()
print(list2)  # Output: ['apple', 'banana', 'cherry']

# List Join: There are several ways to join, or concatenate, two or more lists in Python. One of the easiest ways are by using the + operator.
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)  # Output: ['a', 'b', 'c', 1, 2, 3]

# List Comprehension: List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
# Example: Create a new list with the values doubled from an existing list.
my_list = [1, 2, 3, 4, 5]
new_list = [x * 2 for x in my_list]
print(new_list)  # Output: [2, 4, 6, 8, 10]

# List Methods: Python has a set of built-in methods that you can use on lists. Some of the most commonly used list methods are:
# append(): Adds an element at the end of the list.  
my_list = ["apple", "banana", "cherry"]
my_list.append("orange")
print(my_list)  # Output: ['apple', 'banana', 'cherry', 'orange']

# clear(): Removes all the elements from the list.
my_list.clear()

# copy(): Returns a copy of the list.
# count(): Returns the number of elements with the specified value.
# extend(): Add the elements of a list (or any iterable), to the end of the current list.
# index(): Returns the index of the first element with the specified value.
# insert(): Adds an element at the specified position.
# pop(): Removes the element at the specified position.
# remove(): Removes the first item with the specified value.
# reverse(): Reverses the order of the list.
# sort(): Sorts the list.

#List Slicing: List slicing is a way to extract a portion of a list by specifying a start and end index. The syntax for list slicing is list[start:end], where start is the index of the first element to include, and end is the index of the first element to exclude.
my_list = ["apple", "banana", "cherry", "date", "elderberry"]
# Slicing from index 1 to 3 (excluding index 3) 
sliced_list = my_list[1:3]
print(sliced_list)  # Output: ['banana', 'cherry']

# Slicing from the beginning to index 3 (excluding index 3)
sliced_list = my_list[:3]
print(sliced_list)  # Output: ['apple', 'banana', 'cherry']

# Slicing from index 2 to the end of the list
sliced_list = my_list[2:]
print(sliced_list)  # Output: ['cherry', 'date', 'elderberry']

# Slicing with negative indexes
sliced_list = my_list[-3:-1]
print(sliced_list)  # Output: ['cherry', 'date']

#Slicing with step: You can also specify a step value in list slicing, which determines the interval between elements to include in the slice. The syntax for this is list[start:end:step].
my_list = ["apple", "banana", "cherry", "date", "elderberry"]
# Slicing with a step of 2
# This will include every second element from index 0 to index 4 (excluding index 4)
sliced_list = my_list[0:4:2]
print(sliced_list)  # Output: ['apple', 'cherry']   

# Modifying list items: You can modify the value of a specific item in a list by referring to its index number and assigning a new value.
my_list = ["apple", "banana", "cherry"] 
my_list[1] = "blueberry"
print(my_list)  # Output: ['apple', 'blueberry', 'cherry']

# Change a list item by index: You can change the value of a specific item in a list by referring to its index number and assigning a new value.
my_list = ["apple", "banana", "cherry"]
my_list[1] = "blueberry"
print(my_list)  # Output: ['apple', 'blueberry', 'cherry']

# Change a range of list items: You can change the values of a range of items in a list by specifying the start and end index numbers and assigning new values to that range.
my_list = ["apple", "banana", "cherry", "date", "elderberry"]
# Changing the values of items from index 1 to index 3 (excluding index 3)
my_list[1:3] = ["blueberry", "cantaloupe"]  
print(my_list)  # Output: ['apple', 'blueberry', 'cantaloupe', 'elderberry']

# Adding list items: You can add new items to a list by using the append() method, which adds an item to the end of the list, or the insert() method, which adds an item at a specified index.
# Adding an item to the end of the list using append()
my_list = ["apple", "banana", "cherry"]
my_list.append("date")
print(my_list)  # Output: ['apple', 'banana', 'cherry', 'date']

# Adding an item at a specific index using insert()
my_list = ["apple", "banana", "cherry"]
my_list.insert(1, "blueberry")  # Insert "blueberry" at index 1
print(my_list)  # Output: ['apple', 'blueberry', 'banana', 'cherry']

# Removing list items: You can remove items from a list by using the remove() method, which removes the first occurrence of a specified value, or the pop() method, which removes an item at a specified index.
# Removing an item by value using remove()
my_list = ["apple", "banana", "cherry", "date"]
my_list.remove("banana")  # Remove "banana" from the list
print(my_list)  # Output: ['apple', 'cherry', 'date']
# Removing an item by index using pop()
my_list = ["apple", "banana", "cherry", "date"]
my_list.pop(1)  # Remove the item at index 1 ("banana")
print(my_list)  # Output: ['apple', 'cherry', 'date']

