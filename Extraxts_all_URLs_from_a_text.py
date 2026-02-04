#firstly import a librar re
import re


#take input from user
text = input("please enter your text: ")


#pattern to match URLs starting with http(s) oe www
pattern = r'(https?://[^\s]+|www\.[^\s]+)'


#Find all URLs in the text
find = re.findall(pattern, text)


#if url found then run this block
if find:

    
    #and print this
    print("URL detected: ", find)


#otherwise run this block
else:

    #and print this line
    print("NO url detected")

    
