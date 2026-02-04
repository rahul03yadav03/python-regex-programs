#firstly import re library
import re


#take input from the user
password = input("Please enter your Passwords: ")


#regex pattern
upper = r"[A-Z]"                     #at least one uppercse

lower = r"[a-z]"                     #at least one lowercase

digit = r"\d"                        #at least one digit

special = r"[!@$%^&*(/).,/?<\>;:'{}[\]`~]"        #at least 0ne special character

min_length = 8                                        #minimum lenghth requirements


#check all conditions, if true then:
if (len(password)>= min_length
    and re.search(upper,password)
    and re.search(lower,password)
    and re.search(digit, password)
    and re.search(special, password)):

    #print this line
    print("STRONG PASSWORD")


#otherwise run this block
else:

    #and print this line
    print("WEAK PASSWORD.Make sure it has uppercse, lowercase, digit, special char, and minimum 8 characters.")
