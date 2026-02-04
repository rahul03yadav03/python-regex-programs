#import  a library name regex 
import re


#take input (Paragraph) from user 
paragraph = input("Please enter paragraph: ")


#define regex for email address
#[a-zA-Z0-9._%+-]+ --> username (letters and numbers)
#@                --> mandatory @ symobl
#[a-zA-Z0-9._]+   --> domain name
#\.               --> dot (.)
#[a-zA-Z]{2,}     --> domain extension (com, org , in , etc)
pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"


#Find all email addresses matching the pattern
find = re.findall(pattern,paragraph)


#print the list of matched email addresses 
print("Here is your all email address: ",find)
