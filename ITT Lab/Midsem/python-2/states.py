states = "Mississippi Alabama Texas Massachusetts Kansas"
words = states.split()
statesList = []

for i in words:
    if i[-3:] == "xas":
        statesList.append(i)

for i in words:
    if (i[0] == "k" or i[0] == "K") and (i[-1]=="s" or i[-1]=="S"):
        statesList.append(i)

for i in words:
    if i[0] == "M" and i[-1] == "s":
        statesList.append(i)

for i in words:
    if i[-1] == "a":
        statesList.append(i)

for i in words:
    if i[0] == "M":
        statesList.append(i)

print(statesList)