#first import re library
import re

#take input from user
password = input("Please enter any letter: ")

#pattern for uppercase letter
pattern = r'[A-Z]'

#check if atleast one uppercase exixts
find = re.search(pattern,password)


#if exists run this loop 
if find:

    #print this line 
    print("yes, password has atleast one uppercase letter")
    
#if there is no uppercase then run thos "else" loop
else:

    #print this line
    print("No, password does not have an uppercase letter")
    
