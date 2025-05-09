
def even(num):
    if num%2==0:
        return True
    
# filter with a lambda function and multiple condition
numbers=[1,2,3,4,5,6,7,8,9]
even_and_greater_then_five=list(filter(lambda x:x>5 and x%2==0 , numbers))
print(even_and_greater_then_five)

#filter to check if the aGE IS GREATER than
#25 in dictionary

