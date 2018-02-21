import math
print (math.pi)

# importing the pi  <—— documentation
from math import pi

# floating point data type
I=4.0
Print (I(
j=1
Print(j)
Text = “I’m going to be a string when I grow up.”
print (text)
text[4]
Type (text) <— tells you if it’s a string

J=4.2
j.is_integer()


number =7
number_dec =3.6
Result = number+number_dec
print(result)

dedication = "Your planet,love."
#shows the characters between these numbers, should return Your
dedication[0:4]

dedication_supp = "Your reality, honey."
#concatonating (joining) two strings
paean = dedication + " " + dedication_supp
print(paean)
# .find is a method; find looks for the phrase in the brackets returns the position
paean.find("love") #first position in the list that starts this collection of strings
paean[paean.find("love")] #brackets specify positions within a string, should return the element position in the [] in the phrase paean

paean_lenth=2
#replaces {} with the variables defined in format
msg = "I wrote you a paean. It goes like {} then it goes like {} it as {} lines.format(dedication, dedication supp, paean_length)"

#F string

msg = f"I wrote you a paen in goes like {dedication} then goes like {something}"

print msg

# Boolean < true or false

reality = true
non_reality = false

print (reality and not non_reality)
eric_height = 6.0
liana_height =5.75

#is eric_height equal ==, not equal !=, etc to liana_height
print (eric_height == liana_height)

x=1
y=1.0

print (x==y) # returns true
print (x is y) # returns false

# list
#object lieral
l_one = []
l_two = [1,2.0,'a',"abcd", True, x] #multiple types, '' and "" same syntax in python

l_two.append(1) #sticks another element in the list
print(l_two)

l_three=['a','b','c','d']

l_two.append(l_three)
print (l_two) #it's become a list within the list D:

squares = [ ]

for i in range(5):
    squares.append(i * i)
print(squares)

squares = [i * i for i in range(5)] #specifies a range of things and perform the operation i*i on it
print squares








#DICTIONARIES
#lists are square brackets, dictionaries are curly brackets; define dictionary using key: value pairs
#specify key and the values
#dictionaries are like tables
d_one = {'key1':1, 'key2': "moose", 'key3':4}
print (d_one)
# we retrieve values in a LIST using index position; in dictionaries we use the keys

d_one['key1'] #returns all the values stored in key1


d_one[6] = 'six' #creates a key: value pair where key is 6 and pair is "six"
#DICTIONARIES DON'T STORE ORDER
