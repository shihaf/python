import random

lst=list()

num=int(input("enter the number of names: "))
while num!=0:

    lst.append(input("enter name : "))
    num=num-1
print(random.choice(lst))
    
 
