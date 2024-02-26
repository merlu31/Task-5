# write a python program that takes a string and returns the number of unique characters in it
# characters present in the string str
S = "guvi geek networks private limited"
a = ""
for i in S:
	if i not in a:
		a += i
print(len(a))