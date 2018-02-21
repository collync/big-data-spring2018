#A LISTS
#A.1 Creating a list of 4 strings
my_list = ["king","t'challa","wakanda","forever"]
#A.2 Print 3rd item on the list
print (my_list[2])
#A.3 Print the 1st and 2nd item using index slicing
print (my_list[0:2])
#A.4 Add a new string with text "last" to the end of the list and print the LISTS
my_list.append("text")
print(my_list)
#A.5 Get the list length and print it
print(len(my_list))
#A.6 Replace the last item in the list with the string "new" and print
#Adopted from Matthias Eisen http://matthiaseisen.com/pp/patterns/p0031/
my_list[-1] = "new"
print (my_list)


#B. STRINGS
sentence_words = ['I', 'am', 'learning', 'Python', 'to', 'munge', 'large', 'datasets', 'and', 'visualize', 'them']
#B.1 Converst list into a normal sentence with join and then Print
#Based on Joran Beasley https://stackoverflow.com/questions/12309976/convert-list-into-string-with-spaces-in-python
sentence = " ".join(sentence_words)
print (sentence)

#B.2 Reverse order of this list using .reverse, print it
sentence_words.reverse()
print (sentence_words)

#B3 use .sort to sort list using default sort order
sentence_words.sort()
print (sentence_words)

#B4 Use sorted and descript how they differ
sorted(sentence_words)
#The .sort method modifies the existing list through the function, while the sorted() method sorts the list and leaves the original intact.
#However, both sort the elements of the list in the same order.

#B5 do a case-insensitive alphabetical sort
case_insensitive_list = sorted(sentence_words, key=lambda s: s.lower())
print (case_insensitive_list)
