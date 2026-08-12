# Tuples: A tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets.
fruits=("apple", "banana", "cherry")
print(fruits)
print("------------")

# creating tuples in different ways
# 1. Using parentheses 
colors = ("red", "green", "blue")
numbers = (1, 2, 3, 4, 5)
mixed_tuple = ("apple", 1, True, 3.14)
nested_tuple = (1, 2, ("a", "b", "c"), 3)
print("------------")

# without parentheses
fruits2 = "apple", "banana", "cherry"
print(fruits2)

# creating a tuple with one item
single_item_tuple = ("apple",)  
print(single_item_tuple)

# creating a tuple without parentheses
single_item_tuple2 = "apple",
print(single_item_tuple2)

#Using the tuple() constructor
tuple_from_list = tuple(["apple", "banana", "cherry"])
print(tuple_from_list)

# Accessing Tuple Items: You can access tuple items by referring to the index number, inside square brackets.
print(fruits[0])  # Output: apple
print(fruits[1])  # Output: banana
print(fruits[2])  # Output: cherry

# Negative indexing: Negative indexing means beginning from the end, -1 refers to the last item, -2 refers to the second last item etc.
print(fruits[-1])  # Output: cherry
print(fruits[-2])  # Output: banana


#TUPLE METHODS
# 1. count(): Returns the number of times a specified value occurs in a tuple.
print(fruits.count("apple"))  # Output: 1

# 2. index(): Searches the tuple for a specified value and returns the position of where it was found.
print(fruits.index("banana"))  # Output: 1

# 3. len(): Returns the number of items in a tuple.
print(len(fruits))  # Output: 3

# 4. max(): Returns the largest item in a tuple.
numbers = (1, 2, 3, 4, 5)
print(max(numbers))  # Output: 5

# 5. min(): Returns the smallest item in a tuple.
print(min(numbers))  # Output: 1

# 6. sum(): Returns the sum of all items in a tuple.
print(sum(numbers))  # Output: 15

# 7. sorted(): Returns a new sorted list from the items in a tuple.
print(sorted(fruits))  # Output: ['apple', 'banana', 'cherry']  

# 8. any(): Returns True if any item in the tuple is true. If the tuple is empty, return False.
bool_tuple = (False, False, True)
print(any(bool_tuple))  # Output: True

# 9. all(): Returns True if all items in the tuple are true. If the tuple is empty, return True.
bool_tuple2 = (True, True, True)
print(all(bool_tuple2))  # Output: True

# 10. reversed(): Returns a reversed iterator of the tuple.
reversed_tuple = tuple(reversed(fruits))
print(reversed_tuple)  # Output: ('cherry', 'banana', 'apple')

# 11. zip(): Combines two or more tuples into a single tuple of tuples.
tuple1 = (1, 2, 3)  
tuple2 = ('a', 'b', 'c')
zipped_tuple = tuple(zip(tuple1, tuple2))
print(zipped_tuple)  # Output: ((1, 'a'), (2, 'b'), (3, 'c'))

# 12. unpacking: You can unpack a tuple into variables.
fruit1, fruit2, fruit3 = fruits
print(fruit1)  # Output: apple
print(fruit2)  # Output: banana
print(fruit3)  # Output: cherry

# 13. slicing: You can slice a tuple to get a subset of its items.
print(fruits[0:2])  # Output: ('apple', 'banana')

# 14. concatenation: You can concatenate two or more tuples using the + operator.
tuple_a = (1, 2, 3)
tuple_b = (4, 5, 6)
concatenated_tuple = tuple_a + tuple_b
print(concatenated_tuple)  # Output: (1, 2, 3, 4, 5, 6)

# 15. repetition: You can repeat a tuple using the * operator.
repeated_tuple = tuple_a * 2
print(repeated_tuple)  # Output: (1, 2, 3, 1, 2, 3)

# 16. membership: You can check if an item exists in a tuple using the in keyword.
print("apple" in fruits)  # Output: True
print("grape" in fruits)  # Output: False

# 17. immutability: Tuples are immutable, meaning you cannot change their items after creation. However, you can create a new tuple by concatenating or slicing existing tuples.
new_fruits = fruits + ("grape",)
print(new_fruits)  # Output: ('apple', 'banana', 'cherry', 'grape')

# 18. converting to list: You can convert a tuple to a list using the list() constructor.
fruits_list = list(fruits)
print(fruits_list)  # Output: ['apple', 'banana', 'cherry']

# 19. converting to set: You can convert a tuple to a set using the set() constructor.
fruits_set = set(fruits)
print(fruits_set)  # Output: {'banana', 'cherry', 'apple'}

# 20. converting to dictionary: You can convert a tuple of key-value pairs to a dictionary using the dict() constructor.
key_value_tuple = (("name", "Alice"), ("age", 30), ("city", "New York"))
fruits_dict = dict(key_value_tuple)

print(fruits_dict)  # Output: {'name': 'Alice', 'age': 30, 'city': 'New York'}

# 21. nested tuples: You can create tuples within tuples, which are called nested tuples.
nested_tuple_example = (1, 2, (3, 4), (5, 6))
print(nested_tuple_example)  # Output: (1, 2, (3, 4), (5, 6))

# 22. tuple comprehension: Unlike lists and sets, tuples do not support comprehension syntax directly. However, you can create a tuple from a generator expression.
tuple_from_generator = tuple(x * 2 for x in range(5))
print(tuple_from_generator)  # Output: (0, 2, 4, 6, 8)

# 23. tuple with mixed data types: Tuples can contain elements of different data types, including integers, strings, floats, and even other tuples.
mixed_data_tuple = (1, "apple", 3.14, (2, 3))
print(mixed_data_tuple)  # Output: (1, 'apple', 3.14, (2, 3))   

# 24. tuple with boolean values: Tuples can also contain boolean values (True or False).
boolean_tuple = (True, False, True)
print(boolean_tuple)  # Output: (True, False, True)

# 25. tuple with None values: Tuples can contain None values, which represent the absence of a value.
none_tuple = (None, 1, "apple")
print(none_tuple)  # Output: (None, 1, 'apple')

# 26. tuple with complex numbers: Tuples can also contain complex numbers, which have a real and imaginary part.
complex_tuple = (1 + 2j, 3 + 4j)
print(complex_tuple)  # Output: ((1+2j), (3+4j))

# 27. tuple with frozenset: Tuples can contain frozensets, which are immutable sets.
frozenset_tuple = (frozenset([1, 2, 3]), frozenset([4, 5, 6]))
print(frozenset_tuple)  # Output: (frozenset({1, 2, 3}), frozenset({4, 5, 6}))
print("------------")
