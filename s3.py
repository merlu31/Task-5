#write a python program that takes a string and returns a new strings with the all the vowels removed
# Function to remove vowels 
def rem_vowel(string): 
	vowels = ['a','e','i','o','u'] 
	result = [letter for letter in string if letter.lower() not in vowels] 
	result = ''.join(result) 
	print(result) 
string = "Guvi Geek Networks private Limited"
rem_vowel(string) 
string = "I Love Python Class"
rem_vowel(string) 