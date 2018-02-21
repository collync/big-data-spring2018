#PYTHON THINKS IN OBJECTS
import math

fun_list = ['are', 'we','fun']
fun_list.sort()
print(fun_list)
#in-place method

more_fun = ['i','know','that','i','!']
more_fun_sort= sorted(more_fun)
print(more_fun_sort)
#stores as variable

#BRANCHING if/else statements

flag = False
if flag:
    x=1
    print ("Flag is true.")
else:
    print ("Flag is false.")


x = range(10)
x = [1,2,3,4,5,6,7,8,9]

for i in x:
    print(i)
#we can make things only print until a certain point
for i in x:
    print(i)
    if (i>5):
        break
    print(i)

#can do this if it's a list of strings too

x=0
for i in range(100):
    x = x+1
    # x+=1 is also the statements
    print (x)

def for_sum(x,y):
    for i in range(y):
        x += i
    return x



for i in x:
    .....print (i*2)

#Vectorization

import numpy as np


a = [1,2,3,4,5]
b = [6,7,8,9,10]
c = []

for
