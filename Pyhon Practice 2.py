# LOOP: Loops enable you to execute a block of code multiple times. Python has two primary types of loops:
#  for loops and while loops.

#WHILE LOOP: A while loop repeatedly executes a block of code as long as a specified condition is true. The syntax is:
# while condition:
count=0 
while count<5: 
    print("The count is:", count) 
    count+=1 
print("----------")

# Infinite loop
#while True:
#    print("This is an infinite loop.")



# FOR LOOP: A for loop iterates over a sequence (like a list, tuple, or string) and executes a block of 
# code for each item in the sequence. The syntax is: for variable in sequence:  code block
Name ="Maria Aqdas"
for x in Name:
    print(x)

for i in range(10):
    if(i%2==0):
        print(i, "is even.")

for i in range(1,10):
    if(i%2==1):
        print(i, "is odd.")

for i in range(1,30,3):
    print("Jump in 3: ",i)

for i in range(1,30,5):
    print("Jump in 5: ",i)
else:
    print("Loop is completed.")
print("----------")    

# LOOP CONTROL STATEMENTS: Loop control statements change the execution from its normal sequence.
#  When execution leaves a scope, all automatic objects that were created in that scope are destroyed. 

# Python supports the following control statements:
# 1. break statement: Terminates the loop statement and transfers execution to the statement 
# immediately following the loop.
for i in range(1, 11):
    if i==5:
        break
    print(i)
print("----------")

# 2. continue statement: Causes the loop to skip the remainder of its body and 
# immediately retest its condition prior to reiterating.  
for i in range(1, 11):
    if i==5:
        continue
    print(i)
print("----------")

# 3. Pass statement: The pass statement is a null operation; nothing happens when it executes. 
# The pass statement is useful as a placeholder when a statement is required syntactically,
#  but you do not want any command or code to execute. 
count=0
while count<5:
    if count==3:
        break
    print("The count is:", count)
    count+=1       
print("----------")

while True:
    user_input=input("Enter'exit' to stop the loop: ")
    if user_input=="exit":
        print("Exiting the loop.")
        break
    print("You entered:", user_input)

print("----------")

#Practice:
for i in range(1,11):
    print(i)
print("----------") 

for i in range(1, 31):
    if i%2==0:
        print(i, "is even.")    
print("----------") 

i=1
while(i<=10):
    print(i)
    i+=1
print("----------") 

for i in range(1, 11):
    if i==6:
        break
    print(i)
print("----------") 

for i in range(1, 11):
    if i==5:
        continue
    print(i)  
print("----------") 

#Exercise:
#Q1. Print Numbers
for i in range(1, 50):
    print (i)
print("----------") 

# Q2. Even Numbers  
for i in range(1,100):
    if  i%2==0:
        print(i, "is even.")
print("----------") 

#Q3. Sum of Numbers
num=int(input("Enter a number: "))
print("The sum of numbers from 1 to", num, "is:", sum(range(1, num+1)))
print("----------") 

#Q4. Multiplication Table
num=int(input("Enter a number: "))
for i in range(1, 11):
    print(num, "x", i, "=", num*i)
print("----------") 

# Q5. Count Even and Odd
even_count=0
odd_count=0
for i in range(1,100):
    if i%2==0:
        even_count+=1
    else:
        odd_count+=1
print("Even numbers:", even_count)
print("Odd numbers:", odd_count)
print("----------") 

#Q6. Factorial
num=int(input("Enter a number: "))
factorial=1
for i in range(1, num+1):
    factorial*=i
print("The factorial of", num, "is:", factorial)
print("----------") 

