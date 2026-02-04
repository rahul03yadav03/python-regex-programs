#import a library name regex
import re

#take input from user
text = input("Please enter  your text: ")


# Define regex for IPv4 address
# \b                         --> word boundary (to avoid matching inside other numbers)
# (?:                        --> start non-capturing group for an octet
# 25[0-5]                    --> matches 250-255
# | 2[0-4]\d                 --> matches 200-249
# | 1\d\d                    --> matches 100-199
# | [1-9]?\d                 --> matches 0-99
# )
# \.                         --> dot separator
# {3}                        --> repeat the above 3 times (for first 3 octets)

# (?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d) --> last octet (0-255)

# \b                         --> word boundary at the end

pattern = r'\b(?:(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\.){3}(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\b'


#Find all ipv4 matching the pattern
find = re.findall(pattern,text)

#print the list of matched ipv4
print("Here is your all ipv4: ",find)
 
