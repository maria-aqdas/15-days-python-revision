# ==========================================
# Dictionaries in Python
# ==========================================

# Basic Syntax Concept
# dictionary_name = { key1: value1, key2: value2, ... }


# Method 1: Create dictionary using curly braces
cohort = {
    "course": "Python",
    "instructor": "Rishabh Mishra",
    "level": "Beginner"
}

# Print dictionary and check type
print(cohort)
print(type(cohort))


# Method 2: Using dict() constructor with keyword arguments
person = dict(name="Madhav", age=20, grade="A")

print(person)
print(type(person))


# Method 3: Using list of tuples with dict() constructor
person2 = dict([
    ("name", "Madhav"),
    ("age", 20),
    ("city", "Mathura")
])

print(person2)
print(type(person2))

# ==========================================
# Accessing Dictionary Values
# ==========================================

student = {
    1: "Class 10th",
    "name": "Madhav",
    "grade": "A",
    "city": "Mathura"
}

print(student)
print(type(student))

# Accessing specific values using keys in square brackets
print(student["name"])
print(student["grade"])


# ==========================================
# Dictionary Methods
# ==========================================

student = {
    1: "Class 10th",
    "name": "Madhav",
    "grade": "A",
    "city": "Mathura"
}

# .keys() method -> Returns a list of all keys
print(student.keys())

# .values() method -> Returns a list of all values
print(student.values())

# .items() method -> Returns a list of key-value tuples
print(student.items())

# .get() method -> Accessing value safely
print(student.get("name"))

# .get() with a default value when key is missing (avoids KeyError)
print(student.get("email", "nahi hai"))

# ==========================================
# Adding, Modifying, and Removing Items
# ==========================================

student = {
    "name": "Madhav",
    "grade": "A",
    "city": "Mathura"
}

# 1. Adding a new item using assignment operator
student["email"] = "madhav@example.com"
print(student)

# 2. Modifying/Replacing an item's value
student["grade"] = "A+"
print(student)

# 3. Removing items using `del` keyword
del student["grade"]
print(student)

# 4. Removing items using `.pop()` method (stores the removed value)
var1 = student.pop("email")
print(var1)       # Prints the removed value
print(student)    # Prints dictionary after popping email


# ==========================================
# Dictionary Iteration using for loops
# ==========================================

student = {
    "name": "Madhav",
    "grade": "A",
    "city": "Mathura"
}

# Loop through keys
for keys in student:
    print(keys)

# Loop through values (Method A - bracket syntax)
for value in student:
    print(student[value])

# Loop through values (Method B - using .values())
for value in student.values():
    print(value)

# Loop through both keys and values (using .items())
for keys, value in student.items():
    print(keys, value)


# ==========================================
# Nested Dictionaries
# ==========================================

main_student = {
    "student1": {
        "name": "Madhav",
        "age": 20
    },
    "student2": {
        "name": "Keshav",
        "age": 25,
        "grade": "A"
    }
}

# Printing full nested dictionary
print(main_student)

# Accessing an inner dictionary
print(main_student["student1"])

# Accessing nested values using multiple square brackets
print(main_student["student1"]["name"])
print(main_student["student2"]["name"])
print(main_student["student2"]["grade"])


# ==========================================
# Dictionary Comprehension
# ==========================================

# Syntax: new_dict = { key_expr: value_expr for item in iterable if condition }

# Example 1: Squares of numbers 1 to 5
my_dict = {x: x**2 for x in range(1, 6)}
print(my_dict)

# Example 2: Modified expression (x + x)
my_dict_2 = {x: x + x for x in range(1, 6)}
print(my_dict_2)