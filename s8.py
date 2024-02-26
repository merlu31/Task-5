# Write a python program that takes a string and returns true if it is anagram otherwise it is false
def check(s1, s2):
	# the sorted strings are checked 
	if(sorted(s1)== sorted(s2)):
		print("TRUE") 
	else:
		print("FALSE")		 
# driver code 
s1 ="guvi"
s2 ="geek"
check(s1, s2)