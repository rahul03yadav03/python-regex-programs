#import  a library name regex 
import re


#take input from user
string = input("PLease enter any string: ")


#define regex for email address
#[a-zA-Z0-9._%+-]+ --> username (letters and numbers)
#@                --> mandatory @ symobl
#[a-zA-Z0-9._]+   --> domain name
#\.               --> dot (.)
#[a-zA-Z]{2,}     --> domain extension (com, org , in , etc)
pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"


#Find all email addresses matching the pattern
find = re.findall(pattern,string)


#print the list of matched email addresses 
print("Here is your all email address: ",find)
