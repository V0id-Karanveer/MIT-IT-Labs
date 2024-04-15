def fibo(n):
    if n == 0:
        return 0
    if n==1:
        return 1
    return fibo(n-1)+fibo(n-2)

num = int(input("Enter the numbers: "))

for i in range(num):
    print(fibo(i))