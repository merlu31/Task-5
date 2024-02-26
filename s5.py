#write a python program that takes a string and returns true if it is palindrome otherwise false it is
# function which return reverse of a string
def isPalindrome(s):
	return s == s[::-1]
# Driver code
s = "limited"
ans = isPalindrome(s)
if ans:
	print("Yes")
else:
	print("No")