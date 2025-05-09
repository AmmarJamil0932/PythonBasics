a = 100
print(a)

## Declaring and Assigning variables
age = 21
height = 6.1
name = "Ammar"
is_student=True
## Printing the variables

print("age:", age)
print("height:", height)
print("name:", name)

## Naming Convention
## Variable names should be descriptive
## They must start with a letter or an underscore . 
## Variables names are case-sensitive

#valid varaible names
first_name = "Ammar"
last_name = "Jamil"
 #Invalid varaibles names
 #1age = 30 , first-name = "Ammar"
 
 #case sensitivity Name and name are different
 
 # Understanding Varaible types
 # Pythonis dynamically typed , meaning type of a variable
 # is determined at run-time
age = 25 #int
height = 6.1 #float
name = "Ammar" #string
is_absent=True #bool
print(type(age))
print(type(is_absent))

#Type checking and Conversion
print(type(height))

my_age=21
print(type(my_age))
#Type Conversion
my_age_str = str(my_age)
print(type(my_age_str))

height = 6.1
type(height)
print(int(height))


# Dynamic Typing
#Python allows the type of a variable to change as the program executes

var = 10
print(var, type(var))

var = 10.5
print(var, type(var))

##input
age = input("Enter the age ")
print(age, type(age))



 
