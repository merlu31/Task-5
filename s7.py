# write a pyhton program that takes a string and returns the most frquent character in it.
test_str = "Guvi Geek Networks Private Limited"
# printing original string
print ("The original string is : " + test_str)
# creating an empty dictionary
freq = {}
# counting frequency of each character
for char in test_str:
	if char in freq:
		freq[char] += 1
	else:
		freq[char] = 1
# finding the character with maximum frequency
max_char = max(freq, key=freq.get)
# printing result
print("The maximum of all characters in Guvi Geek Network Private Limited is : " + str(max_char))