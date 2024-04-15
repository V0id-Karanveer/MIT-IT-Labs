s = "abaca"
flag = 1
for i in range(int(len(s)/2)):
    if s[i]!=s[len(s)-i-1]:
        flag = 0

print(flag)