# 1. write a python program to calculate the total number of vowels and count each individual vowel 
# A,E,I,O,U in the string "Guvi Geeks Network Private Limited"?
def vowel_count(str):
	# Creating a list of vowels
	vowels = "aeiouAEIOU"
	# Using list comprehension to count the number of vowels in the string
	count = len([char for char in str if char in vowels])
	# Printing the count of vowels in the string
	print("No. of vowels :", count)
str = "Guvi Geek Network Private Limited"
vowel_count(str)