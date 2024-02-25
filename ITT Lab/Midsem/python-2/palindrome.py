s = "nama"
n = len(s)
flg = True

for i in range(0,n):
    if s[i] != s[n-i-1]:
        flg = False

print(flg)
