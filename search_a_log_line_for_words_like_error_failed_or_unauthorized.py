#import re library
import re

#take input from user
line = input("Enter a log line: ")


#regex pattern to detect keywords: error, failed, or unauthorized
pattern = r'(error|failed|unauthorized)'


#search the log line for the pattern
find = re.search(pattern,line)


#if any keywords found then run this block
if find:

    #print this line
    print("! Alert: Found an important  keywords!")

#otherwise run this block
else:

    #print this line
    print("No issues detected.")
