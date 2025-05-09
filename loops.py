## for loop

'''for i in range(1,5):
    print(i)
    
for i in range(10,2,-1):
    print(i)'''
    
'''str = "Ammar Jamil"
for i in str:
    print(i)'''
    
## while loop
## The while loop continues to execute
## as long as the condition is true

'''count = 0
while count<5:
    print(count)
    count=count+1'''
 
## Loop control Statement
##break
#The break statement exits the loop prematurely
'''for i in range(10):
    if i==5:
        break
    print(i)'''
    
#continue
## The continue statement skips the current iteration
## and continues with the next
'''for i in range (20):
    if i%2==0:
        continue
    print(i)

##pass
##The pass statement is a null operation; it does nothing
for i in range(5):
    if i==3:
        pass
    print(i) '''

#Nested loops
for i in range(3):
    for j in range(2):
        print(f"1:{i} and j:{j}")
        
#Example : Calculate the sum of first n natural
#numbers using a while and for loop
n=10
sum=0
count=1
while count<=n:
    sum=sum+count
    count=count+1
print("The sum is ",sum)


n=10
sum=0
for i in range(11):
    sum=sum+i
print("The sum is ",sum)

# Prime numbers between 1 and 50

for num in range(1,51):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                break
        else:
            print(num)
    
