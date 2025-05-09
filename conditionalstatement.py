## if statement
age = 10
if age>=20:
    print("You are allowed to vote in election")
    
## else
## The else is executed statement if the if condition is false
age = 16

if age>=18:
    print("You are allowed to vote. ")
else:
    print("You are not allowed to vote ")

## elif statement : for multiple conditions

age = 17
if age<13:
    print("You are 13 years old")
elif age<18:
    print("You are a teenager")
else:
    print("You are an adult ")


## nested conditional statements
## number even odd , negative

'''num = int(input("Enter the number "))

if num>0:
    print("The number is positive")
    if num%2==0:
        print("The number is even")
    else:
        print("The number is odd")
else:
    print("The number is zero negative")'''
    
## Practical Eaxmples
## Determine if a year is a leap year using nested condition statement

'''year = int(input("Enter the year "))
if year%4==0:
    if year&100==0:
        print("It is a leap year")
else:
    print("It is not a leap year")
    '''
    

var1 = int(input("Enter first number "))
var2 = int(input("Enter second number "))

choice = str(input("Enter your choice "))

if choice == '+':
    result = var1+var2
    print("The result of addition is ",result)
elif choice == '-':
    result = var1-var2
    print("The result of subtraction is ",var2)
elif choice == '*':
    result = var1*var2
    print("The result of multiplication is ",result )
elif choice =='/':
    result = var1/var2
    print("The result of division is ", result)
else:
    print("Enter valid choice")
    
    