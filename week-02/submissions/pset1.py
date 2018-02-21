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


#C RANDOM NUMBERS
#Returning an integer between a low and a high number supplied by the user, but that can be called with the low number optional (default to 0).
from random import randint

def return_int():
    #Ask for user input, help from aisbaa https://stackoverflow.com/questions/22402548/default-values-on-empty-user-input-in-python and https://stackoverflow.com/questions/35368418/how-to-user-input-while-defining-function
    get_low = int(input("Enter the lowest number: ") or "0")
    get_high = int(input("Enter the highest number: "))
    return randint(get_low, get_high)
#Print random number between bounds
print (return_int())

#D String Formatting Functions

#Write a function that expects two inputs. The first is a title that may be multiple words, the second is a number.

# testing
# def bestseller():
#     title_of_bestseller = str(input("Enter a title: ")).title()
#     placement = str(input("Enter a number: "))
#     best_sentence = ('The number ', placement, ' bestseller today is: ', title_of_bestseller)
#     return "".join(best_sentence)
# print (bestseller())

def bestseller2():
    title_of_bestseller2 = str(input("Enter a title: ")).title()
    placement2 = str(input("Enter a number: "))
    return ('The number {} bestseller today is: {}'.format(placement2,title_of_bestseller2)

print (bestseller())



#E. Password Validation

def validate_password():
    # Verifies a password that:
    # is 8-14 characters long
    # includes at least 2 digits (i.e., numbers)
    # includes at least 1 uppercase letter
    # includes at least 1 special character from this set: ['!', '?', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=']
    user_password = str(input("Enter your password: "))
    #lists to check characters against
    import string
    list_numbers=['0','1','2','3','4','5','6','7','8','9']
    list_letters=string.ascii_lowercase.upper()
    list_spec=['!', '?', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=']
    #empty lists for validating
    number_check=[]
    letters_check= []
    spec_char_check=[]
    #checking length

    #making lists for validation
    for i in user_password:
        if i in list_numbers:
            number_check.append(i)
    for i in user_password:
        if i in list_letters:
            letters_check.append(i)
    for i in user_password:
        if i in list_spec:
            spec_char_check.append(i)
    if len(user_password)>8 and len(user_password)<14 and len(number_check)>=2 and len(letters_check)>=1 and len(spec_char_check)>=1:
        print ("Success! Your password is valid.")
    else:
        print ("D'oh! Your password is insufficient, pls try again thx.")

validate_password()

F. Exponential Functions
def exp():
    int_one = int(input("Enter a number "))
    expo = int(input("Enter the exponent "))
    final = int_one
    for x in range(1,expo):
        final = final*int_one
    print (final)

exp()


#G. Extra Credit

def my_min(a_list):
    minimum=a_list[0]
    for i in a_list:
        if i<minimum:
            mimimum=i
    return minimum

def my_max(a_list):
    maximum=a_list[0]
    for i in a_list:
        if i>maximum:
            maximum=i
    return maximum
