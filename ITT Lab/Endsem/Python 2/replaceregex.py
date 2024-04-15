import re

pattern = r"world"
word = "universe"
s = "Hello world!"

s = re.sub(pattern,word,s)

print(s)