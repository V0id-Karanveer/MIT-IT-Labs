import states

arr = states.states.split()
statesList = []
for i in arr:
    if i[-3:] == "xas":
        print(i)
        statesList.append(i)

for i in arr:
    if i[0] == 'K' and i[-1] == 's':
        print(i)
        statesList.append(i)

for i in arr:
    if i[0] == 'M' and i[-1] == 's':
        print(i)
        statesList.append(i)

for i in arr:
    if i[-1] == 'a':
        print(i)
        statesList.append(i)

for i in arr:
    if i[0]== 'M':
        print(i)
        statesList.append(i)
        break

print(statesList)


