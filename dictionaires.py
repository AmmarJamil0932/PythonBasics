# Dictionaries are unordered collection of items . 
# They store data in key value pairs . Keys must 
#Unique and immutable

#Creating Dictionaries
empty_dict = {}
print(type(empty_dict))
empty_dict2 = dict()
print(type(empty_dict))

students = {"name":"Ammar","age":21,"grade":'A'}
print(type(students))

#Single key is always used for eg in databases
#every key must be unique
students = {"name":"Ammar","age":21,"name":'A'}
print(students)