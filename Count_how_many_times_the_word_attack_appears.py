#firstly import re library
import re


#take input from  user
text = input("Please enter your text: ").lower()


#regex pattern to match the word 'attack' exactly
pattern = r'\battack\b'


#Find all occurrences
find = re.findall(pattern, text)

#count the matches 
count = len(find)


#Print the result
print(f"The word 'attack' appaers {count} times.")
