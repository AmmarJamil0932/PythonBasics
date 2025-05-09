# Semantics is how we are able to arrange the words . 
# It means interpreations
# Basics syntax rules in python
'''
This is a multi lines
comment .  While hash means
single line comments
'''
## 1- Case sensitivity : Python is case sensitive
name = "Ammar"
Name = "Jamil"
print(name)
print(Name)

## 2 - Identation - It is used to define blocks of code
# It provides consistent use of spaces
age = 20
if age >18:
    print(age)
# The second print is outside the if block    
print(age)

## Line Continuation
# Using backslash we can continue a clause
total=1+2+3+4+5+6\
+4+5
print(total)

# Multiple Statements on a single line
x=5 ; y=10; z= x+y
print(z)

# Variable Assignment : Compiler automatically understands
# the datatype at run type
age = 20
print(type(age))
print(age)

# Type Inference
variable = True
print(type(variable))


