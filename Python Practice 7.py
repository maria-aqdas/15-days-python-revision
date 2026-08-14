
# 1. Create Function without Parameters  
  
def greetings():  
    print("Welcome to the Python course by Rishabh")  

# Calling/Using the function  
greetings()


# 2. Function to Add Two Numbers
# ==========================================

# a, b are parameters
def add_two_numbers(a, b):
    result = a + b
    print("The sum is:", result)

# 5, 3 are positional arguments
add_two_numbers(5, 3)

# Calling with keyword arguments / changing sequence
add_two_numbers(a=10, b=100)
add_two_numbers(b=50, a=10)


# ==========================================
# Function to Add Three Numbers
# ==========================================

def add_three_numbers(a, b, c):
    result = a + b + c
    print("The sum is:", result)

# Calling with 3 arguments
add_three_numbers(5, 3, 100)


# ==========================================
# 3. Function using Return Statement
# ==========================================

def add_two_num(a, b):
    return a + b
    # Any code written after return statement will not execute

# Calling and storing the returned value
sum_two_num = add_two_num(10, 1)
print(sum_two_num)

# =======================================================
# 4. Temperature Conversion (With Return vs Without Return)
# =======================================================

# Method A: Using Return
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

temp_f = celsius_to_fahrenheit(25)
print(temp_f)
print("With Return:", type(temp_f))  # Returns <class 'float'>
  

# Method B: Without Return (Using Print inside function)
def celsius_to_fahrenheit_print(celsius):
    fahrenheit = (celsius * 9/5) + 32
    print(fahrenheit)

temp_f2 = celsius_to_fahrenheit_print(50)
print("Without Return:", type(temp_f2))  # Returns <class 'NoneType'>

# ==========================================
# 5. Empty Function using `pass`
# ==========================================

def kuch_bhi():
    # Code to be updated later
    pass

print("Hello World")
