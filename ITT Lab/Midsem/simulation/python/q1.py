sentence = input("enter ")
l1 = sentence.split()
dict1 = {}

for i in l1:
    if i in dict1.keys():
        dict1[i]+=1
    else:
        dict1[i] = 1

print(dict1)
print(len(l1))