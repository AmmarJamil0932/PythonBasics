'''lst=[]
print(type(lst))

names=["Ammar", "Jamil" , 21]
print(names)

mixed_list=[1,2,"Jacob", True , 201]
print(mixed_list)

#Accessing list Elements
#List is 0 indexed
names = ["James","John","David", "Clark","Joseph","Ali"]
print(names[4])
print(names[1])
print(names[-1])

print(names[1:]) # From 1 to last
print(names[:3]) # Excluding 3

#Modifying the list Elements
names[1]="Daniyal"
print(names)

#List Methods
names = ["James","John","David", "Clark","Joseph","Ali"]
names.append("Clear")
print(names)

names.insert(3,"Robert")
print(names)

names.remove("Clark")
print(names)

names.pop()
names.pop()

print(names)

index=names.index("James")
print(index)

names.reverse()
print(names)
#Slicing list
numbers = [1,2,3,4,5,6,7,8,9,10]
print(numbers[1:3])
print(numbers[:5])
print(numbers[5:])
print(numbers[::2])
print(numbers[::-3])

#Interating over list
for i in numbers:
    print(i)
# Iterating with index
for index, numbers in enumerate(numbers):
    print(index,numbers)'''
    
# List Comprehension
lst = []
for i in range(5):
    lst.append(i**2)
    
print(lst)

print([i**2 for i in range(10)])
    