#first import re library
import re


#take input from user
phone_number = input("Please enter your phone numnber: ")


#regrex pattern to match phone numbers in the format 123-456-7890
pattern = r'\d{3}-\d{3}-\d{4}'


#search for the pattern in the user input
find = re.search(pattern,phone_number)


#if there is something, then run this block
if find:

    
    #and print this line
    print("Valid phone number formate!")


#otherwise run this block
else:

    #print this line
    print("Invalid phone number formate!")
