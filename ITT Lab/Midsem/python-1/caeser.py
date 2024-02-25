import string

# Using the string.ascii_lowercase to get all lowercase letters
alpha = list(string.ascii_lowercase)

s = "zoo"
res = ""

for i in range(len(s)):
    res = res+alpha[(alpha.index(s[i])+3)%26]

print(res)

