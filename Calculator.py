def addition (a,b):
return(a+b)

def subtraction (a,b):
return(a-b)

def multiiplication (a,b):
return(a*b)

def division(a,b):
if b == 0:
return("Number can not divide by zero")
else:
return(a/b)

number a = int(input("Enter num1:"))

print("Choose the Operation:")
print("1.Add")
print("2.Sub")
print("3.Multi")
print("4.Div")
print("5.Close All")

choice = int(input("choice the operation:"))
number b = int(input("Enter num2:"))

if choice == 1:
print("Addition is", add(number a,number b))
elif choice == 2:
print("Subtraction is", sub(number a,number b))
elif choice == 3:
print("Multiplication is ", mult(number a,number b))
elif choice ==4:
print("Division is", div(number a,number b))
elif choice == 5:
print("Calculation is Cancel")
else:

print("Enter number is invalid")
