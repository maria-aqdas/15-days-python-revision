# STRING: A string is a sequence of characters. In Python, strings are enclosed in either single quotes (' ') or double quotes (" ").
print("Allah Almighty is the most merciful and compassionate.")
print('Allah is my heart and my soul.')
print('''He is the creator of the universe and everything in it. 
He is the one who gives us life and sustains us. ''')  
print("------------------------------")

# FORMATED STRING: A formatted string is a string that contains placeholders for variables or expressions.
# There are 3 types of formatted strings in Python: f-strings, str.format() method, and % formatting.
#  % formatting.
Name= "Maria Aqdas " 
age=20
print("My name is %s and I am %d years old." % (Name, age))
print("------------------------------")

# str.format() method.
Name= "Maria Aqdas" 
age=20  
print("My name is {} and I am {} years old.".format(Name, age))

print("My sister name is {name} and she is {age} years old.".format(name="Alia", age=17))
print("------------------------------")

# f-string format
Name= "Maria Aqdas"
age=20
print(f"My name is {Name} and I am {age} years old.")
print("------------------------------")


# Escape Characters: Escape characters are special characters that are used to represent certain characters in a string.
#  In Python, escape characters are represented by a backslash (\).
print("Hello, I am a \"Python\" programmer.")
print('Hello, I am a \'Python\' programmer.')
print("Hello, I am a \\Python\\ programmer.")
print("Hello, I am a \nPython programmer.")
print("Hello, I am a \tPython programmer.")
print("Hello, I am a \bPython programmer.")
print("Hello, I am a \rPython programmer.")
print("Hello, I am a \fPython programmer.")
print("Hello, I am a \vPython programmer.")
print("------------------------------")

# String Operators: String operators are used to perform operations on strings. 
# In Python, there are several string operators, including concatenation (+), repetition (*), and membership (in).
# Concatenation (+)
str1 = "Hello, "
str2 = "I am a Python programmer."
print(str1 + str2)
print("------------------------------")

# Repetition (*)
str1 = "Hello, "
str2 = "I am a Python programmer. "
print(str1 * 3) 
print("------------------------------")

# Membership (in)
str1 = "Hello, I am a Python programmer."
print("Python" in str1)
print("------------------------------")

# string indexing: String indexing is the process of accessing individual characters in a string using their index. 
str1 = "Hi, I am a student."
print(str1[0])  # Output: H     
print(str1[1])  # Output: i         
print(str1[6])  # Output: a     
print(str1[7])  # Output: m     
print(str1[8])  # Output:      
print(str1[9])  # Output: a     
print(str1[10]) # Output:      
print(str1[11]) # Output: s     
print(str1[12]) # Output: t     
print(str1[13]) # Output: u     
print(str1[14]) # Output: d     
print(str1[15]) # Output: e         
print(str1[18]) # Output: .     
print("------------------------------")

# Positive indexing starts from 0 and goes up to n-1, where n is the length of the string.
number = "123456789"
print(number[0])  # Output: 1
print(number[4])  # Output: 5
print(number[8])  # Output: 9
print("------------------------------")

#Negative indexing starts from -1 and goes down to -n, where n is the length of the string.
str1 = "Hi, I am a Maria."
print(str1[-1])  # Output: a     
print(str1[-8])  # Output: M    
print("------------------------------")

# string slicing: String slicing is the process of extracting a substring from a string using its index.
str1 = "Hi, I am a student."
print(str1[0:5])  # Output: Hi, I
print(str1[7:14]) # Output: a student.
print(str1[0:])   # Output: Hi, I am a student.
print(str1[:6])  # Output: Hi, I am a student.
print("------------------------------")

# Traversing a string: Traversing a string is the process of accessing each character in a string one by one.
str1 = "Hi, I am a student."
for char in str1:
    print(char)
print("------------------------------")

# String Methods: String methods are built-in functions that can be used to perform operations on strings.
str1 = "Hi, I am a student."
print(str1.upper()) 
print(str1.lower())  
print(str1.title()) 
print(str1.capitalize())  
print(str1.strip()) 
print(str1.replace("student", "programmer"))  
print(str1.split())  
print(str1.find("student"))   
print(str1.count("a"))  
print(str1.startswith("Hi"))
print(str1.endswith("student."))
print(str1.isalpha())
print(str1.isdigit())
print("------------------------------")

# String bulid-in functions: String built-in functions are functions that are used to perform operations on strings.
str1 = "Hi, I am a student."  
str2 = "123456789"  
print(len(str1))
print(max(str2))
print(min(str2))
print(sorted(str2))
print(reversed(str2))
print("------------------------------")
