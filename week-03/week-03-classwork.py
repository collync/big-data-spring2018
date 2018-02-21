#Some class notes!

#BRANCHING

flag = True
if flag:
    x=1
    print("Flag is 1.")
else if flag== 2:
    x = 2
    print("Flag is 2.")
else:
    x = 3
    print("Flag is 3.")

#FOR LOOPS

x = range(10)
x = [0,1,2,3,4,5,6,7,8,9]

for i in x:
    print(i)

for i in x:
    print(i*2)

for i in x:
    if ((i *2)> 5):
        break
    print(i)

my_list = ['This', 'is', 'Python']
for i in my_list:
    print(i)
    print(my_list.index(i)) #By default, the thing that's passed through the iterator is the value of the thing.
    #^ This shows the list, and checks the index position of that element.

x = 0
for i in range(100):
    x += i  # This is the same as saying x = x + i!
print(x)

def for_sum(x,y):
    for i in range(y):
        x+= i
    return x

for_sum(0,100)

#VECTORIZATION

import numpy as np
a = [1,2,3,4,5]
b = [6,7,8,9,10]
c = []

for i, j in zip(a,b):
    c.append(i+j)
print(c)
