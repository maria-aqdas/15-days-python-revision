# VARIABLE:  A varibale is a container used to store and manage data.
a= 12
print(a) 
 
# DATA TYPE: In which type we store our data
b=10
c="Maria Aqdas"    
d=12.4   
e=True
print(type(b)) 
print(type(c))
print(type(d))
print(type(e))
print("----------")

# INPUT: Taking value from user
name=input("What is your name?")
print("My name is", name)
print(type(name))

# TYPE CASTING: converting one type data into an other type
age=int(input("O, whats your age?"))
print("Sure, My age is",age)
print(type(age))

CGPA=float(input("Can you shae your CGPA?"))
print("Of course, it is", CGPA)
print(type(CGPA))
print("Thats great, Thanks for sharing.")
print("----------")

# ARITHMETIC OPERATORS:  Use to perform Arithmetic operations on data.
Add=(12+8)
print(Add)
Substract=(12-8)
print(Substract)
Multiplication=(12*8)
print(Multiplication)
Devision=(12/8)
print(Devision)
Dobule_Devision=(12//8)
print(Dobule_Devision)
Modulas=(12%8)
print(Modulas)
Power=(12**8)
print(Power)
print("----------")

# COMPARSION OPERATORS:  Used to compare two values and return result in the form of TRUE or FALSE depending on the condition.
var1=50
var2=40
print(var1==var2)
print(var1!=var2)
print(var1<=var2)
print(var1>=var2)
print(var1<var2)
print(var1>var2)
print("----------")

# LOGICAL OPERATORS: They are used to compare multiple expressions and conditions and return result in the form of TRUE or FALSE
print(2>3 and 4<7)
print(2>3 or 4<7)
print(not 4<7)
print("----------")

#if, else, elif, nested if
bill=int(input("Enter your bill:  "))
if(bill<5000):
    print("Your bill is less thsn 5000.")
    choice = input("Do you want to buy anything else? (yes/no): ").lower()
    
    if choice == "yes":
        print("Select anything more.")
    else:
        print("Thanks, Pay your bill on counter.")   
elif(bill==5000):
    print("Your bill is 5000. Please Pay it.")
else:
    option = input("Do you want to pay in installments? (yes/no): ").lower()
    
    if option == "yes":
        no_installment = int(input("No. of installments do you want: "))
        if no_installment > 0:
            pay = bill / no_installment
            print("You pay every month Rs.", pay)
        else:
            print("Installments must be greater than 0.")
    else:
        print("Please pay your full bill at the counter.")

print("----------")    


### PRACTIC QUESTIONS #####

# even or odd
a=12
if(a%2==0):
    print("EVEN")
else:
    print("ODD")
print("----------")

#Positive, Negative or Zero
num=int(input("Enter any number: "))
if(num=="0"):
    print("It is Zero.")    
elif(num<0):
    print("Num is negative.")
else:
    print("Num is Positive.")   
print("----------")

# Largest of Two Numbers
a=int(input("Enter a: "))
b=int(input("Enter b: "))
if(a>b):
    print("a is larger.")     
elif(a<b):
    print("b is larger.")
else:
    print("Both are equal.")    
print("----------")    
