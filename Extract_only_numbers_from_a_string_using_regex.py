#First import a re library
import re


#take input from user
string = input("Please enter any string: ")


#Regex pattern to find all numbers (one or more digits)
pattern = r'\d+'


#Find all numbers in the string
find = re.findall(pattern, string)


#Print the list of numbers found
print("Number found", find)
