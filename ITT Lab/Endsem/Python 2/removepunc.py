s = "The quick brown fox jumps over the lazy dog, but the dog doesn't seem to care; it just continues sleeping peacefully!"
s2 = ""

for i in s:
    if i in ",;!.":
        s2+=" "
    else:
        s2+=i
print(s2)