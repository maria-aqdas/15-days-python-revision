# Q1. CREATE A CLASS
# A class is a blueprint for creating objects.
# Here, Student is an empty class.

class Student:
    pass
# Creating two objects from the Student class
student1 = Student()
student2 = Student()
print("Q1: Class and Objects")   
print(type(student1))
print(type(student2))   
print("-" * 50)

# Q2. STUDENT ATTRIBUTES
# __init__() is called automatically when an object is created.
# self.name, self.age and self.field are instance attributes.

class StudentInfo:
    def __init__(self, name, age, field):
        self.name = name
        self.age = age
        self.field = field
# Creating two StudentInfo objects
student1 = StudentInfo("Maria", 16, "Data Science")
student2 = StudentInfo("Ali", 17, "Computer Science")
print("Q2: Student Attributes")
print("Student 1:")
print("Name:", student1.name)
print("Age:", student1.age)
print("Field:", student1.field)
print()
print("Student 2:")
print("Name:", student2.name)
print("Age:", student2.age)
print("Field:", student2.field)
print("-" * 50)

# Q3. STUDENT INTRODUCTION
# A function inside a class is called a method.
# introduce() is a method of the StudentIntro class.

class StudentIntro:
    def __init__(self, name, field):
        self.name = name
        self.field = field
    def introduce(self):
        print("Hi, my name is", self.name)
        print("I am studying", self.field)
# Creating an object
student = StudentIntro("Maria", "Data Science")
print("Q3: Student Introduction")
student.introduce()
print("-" * 50)

# Q4. CALCULATOR CLASS
# This class contains four methods:
# add()
# subtract()
# multiply()
# divide()

class Calculator:
    def add(self, a, b):
        return a + b
    def subtract(self, a, b):
        return a - b
    def multiply(self, a, b):
        return a * b
    def divide(self, a, b):
        # Prevent division by zero
        if b == 0:
            return "Cannot divide by zero"
        return a / b
# Creating Calculator object
calc = Calculator()
print("Q4: Calculator")
print("Addition:", calc.add(10, 5))
print("Subtraction:", calc.subtract(10, 5))
print("Multiplication:", calc.multiply(10, 5))
print("Division:", calc.divide(10, 5))
print("-" * 50)

# Q5. RECTANGLE CLASS
# The Rectangle class has two attributes:
# length
# width
# It also has two methods:
# area()
# perimeter()

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
    def perimeter(self):
        return 2 * (self.length + self.width)
# Creating Rectangle object
rectangle = Rectangle(10, 5)
print("Q5: Rectangle")
print("Length:", rectangle.length)
print("Width:", rectangle.width)
print("Area:", rectangle.area())
print("Perimeter:", rectangle.perimeter())
print("-" * 50)

# Q6. BANK ACCOUNT
# This class represents a simple bank account.
# Attributes:
# account_holder
# balance
# Methods:
# deposit()
# withdraw()
# check_balance()

class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
    # Add money to the account
    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance")
    def check_balance(self):
        print("Current Balance:", self.balance)
# Creating BankAccount object
account = BankAccount("Maria", 10000)
print("Q6: Bank Account")
account.check_balance()
account.deposit(5000)
account.withdraw(3000)
account.check_balance()
print("-" * 50)

# Q7. STUDENT MARKS AND GRADE
# This class stores student's name and marks.
# calculate_grade() determines the grade based on marks.

class StudentGrade:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def calculate_grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 80:
            return "B"
        elif self.marks >= 70:
            return "C"
        elif self.marks >= 60:
            return "D"
        else:
            return "F"
# Creating a student object
student = StudentGrade("Maria", 92)
print("Q7: Student Grade")
print("Name:", student.name)
print("Marks:", student.marks)
print("Grade:", student.calculate_grade())
print("-" * 50)

# Q8. MULTIPLE STUDENTS
# Here we create multiple Student objects
# and store them inside a list.
# Then we find the student with the highest marks.

class StudentMarks:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks
# Creating a list of Student objects
students = [
    StudentMarks("Maria", 16, 92),
    StudentMarks("Ali", 17, 85),
    StudentMarks("Sara", 16, 95),
    StudentMarks("Ahmed", 17, 78),
    StudentMarks("Ayesha", 16, 88)
]
print("Q8: Multiple Students")
# Assume the first student has the highest marks
highest = students[0]
# Compare every student with the current highest
for student in students:
    if student.marks > highest.marks:
        highest = student
print("Student with highest marks:")
print("Name:", highest.name)
print("Age:", highest.age)
print("Marks:", highest.marks)
print("-" * 50)

# Q9. SHOPPING CART
# The ShoppingCart class stores items and their prices.
# Methods:
# add_item()
# remove_item()
# show_items()
# calculate_total()

class ShoppingCart:
    def __init__(self):
        # Dictionary will store:
        # item name -> price
        self.items = {}
    # Add an item to the cart
    def add_item(self, name, price):
        self.items[name] = price
    # Remove an item from the cart
    def remove_item(self, name):
        if name in self.items:
            del self.items[name]
        else:
            print("Item not found")
    # Display all items
    def show_items(self):
        if not self.items:
            print("Cart is empty")
            return
        for name, price in self.items.items():
            print(name, ":", price)
    def calculate_total(self):
        return sum(self.items.values())
# Creating ShoppingCart object
cart = ShoppingCart()
print("Q9: Shopping Cart")
# Adding items
cart.add_item("Laptop", 100000)
cart.add_item("Mouse", 2000)
cart.add_item("Keyboard", 5000)
print("Items in cart:")
cart.show_items()
print("Total:", cart.calculate_total())
cart.remove_item("Mouse")
print()
print("After removing Mouse:")
cart.show_items()
print("Total:", cart.calculate_total())
print("-" * 50)

# Q10. STUDENT MANAGEMENT SYSTEM
# This is the final challenge.
# Features:
# 1. Add student
# 2. Show students
# 3. Search student
# 4. Update marks
# 5. Delete student
# 6. Exit
# We will use a list of Student objects.


class StudentManagement:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
# List that will contain all student objects
student_list = []
def add_student():
    name = input("Enter student name: ")
    marks = float(input("Enter marks: "))
    # Create a Student object
    student = StudentManagement(name, marks)
    # Add object to the list
    student_list.append(student)
    print("Student added successfully.")
def show_students():
    # Check if list is empty
    if not student_list:
        print("No students found.")
        return
    print("\nStudents:")
    # Display every student
    for student in student_list:

        print(
            "Name:",
            student.name,
            "| Marks:",
            student.marks
        )
# Function: Search Student
def search_student():
    name = input("Enter student name to search: ")
    # Search through all objects
    for student in student_list:
        if student.name.lower() == name.lower():
            print("Student found!")
            print("Name:", student.name)
            print("Marks:", student.marks)
            return
    print("Student not found.")
# Function: Update Marks
def update_marks():
    name = input("Enter student name: ")
    for student in student_list:
        if student.name.lower() == name.lower():
            new_marks = float(
                input("Enter new marks: ")
            )
            # Update the object's marks
            student.marks = new_marks
            print("Marks updated successfully.")
            return
    print("Student not found.")
# Function: Delete Student
def delete_student():
    name = input("Enter student name to delete: ")
    for student in student_list:
        if student.name.lower() == name.lower():
            student_list.remove(student)
            print("Student deleted successfully.")
            return
    print("Student not found.")
# MAIN MENU
while True:

    print("\n")
    print("=" * 40)
    print("     STUDENT MANAGEMENT SYSTEM")
    print("=" * 40)
    print("1. Add Student")
    print("2. Show Students")
    print("3. Search Student")
    print("4. Update Marks")
    print("5. Delete Student")
    print("6. Exit")
    print("=" * 40)
    choice = input("Enter your choice: ")
    # Option 1: Add Student
    if choice == "1":
        add_student()
    # Option 2: Show Students
    elif choice == "2":
        show_students()
    # Option 3: Search Student
    elif choice == "3":
        search_student()
    # Option 4: Update Marks
    elif choice == "4":
        update_marks()
    # Option 5: Delete Student
    elif choice == "5":
        delete_student()
    # Option 6: Exit
    elif choice == "6":
        print("Program ended.")
        break

    # Invalid Choice
    else:

        print("Invalid choice. Please try again.")
