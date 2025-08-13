def add(x,y):
    return(x+y)

def sub(x,y):
    return(x-y)

def mult(x,y):
    return(x*y)

def div(x,y):
    if y == 0: 
        return("Can not divide by zero")
    else:
        return(x/y)


num1 = int(input("Enter num1:"))

print("Choose the Operation:")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
print("5.Cancel")

choice = int(input("Enter the operation:"))

num2 = int(input("Enter num2:"))

if choice == 1:
    print("Addition is", add(num1,num2))
elif choice == 2:
    print("Subtraction is",sub(num1,num2))
elif choice == 3:
    print("Multiplication is ",mult(num1,num2))
elif choice ==4:
    print("Division is", div(num1,num2))
elif choice == 5:
    print("Calculation is Cancel")
else:

    print("Invalid")
