import re

pattern = r"world"
word = "universe"
s = "hello world!"
res = re.sub(pattern,word,s)

print(res)