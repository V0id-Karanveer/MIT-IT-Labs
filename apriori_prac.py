import pandas
import itertools as iter

freq = []


def issubset(sub,main):
    for i in sub:
        if i not in main:
            return False
    return True


def init():
    df = pandas.read_excel("database.xlsx")
    df.index = df["TID"]
    df.drop("TID",axis=1)
    for row in df["Itemsets"]:
        trans =[]
        for i in row:
            if i!=",":
                trans.append(i)
                if i not in uniq:
                    uniq[i] = 1
                else:
                    uniq[i]+=1
        itemsets.append(trans)
    for value,count in uniq.items():
        if count>=minsup:
            l.append(list(value))
    for i in l:
        freq.append(i)
    return df


def gencandidate(l,k):
    c = []
    c1 = []
    ctemp = []
    for i in range(0,len(l)-1):
        for j in range(i+1,len(l)):
            temp = []
            temp = list(set(l[i]+l[j]))
            ctemp = iter.combinations(temp,k)
            for r in ctemp:
                if r not in c:
                    r = list(r)
                    r.sort()
                    c.append(r)
    for i in c:
        if i not in c1:
            c1.append(i)
    return c1


def genfreq(c,l):
    supp = {}
    for i in c:
        supp[tuple(i)]=0
        for j in itemsets:
            if issubset(i,j):
                supp[tuple(i)]+=1
    for value,count in supp.items():
        if count>=minsup:
            l.append(list(value))
    for i in l:
        freq.append(i)


def prune(c,l,k):
    remove = []
    for index,c1 in enumerate(c):
        ctemp = iter.combinations(c1,k-1)
        check = [list(temp) for temp in ctemp]
        for i in check:
            if issubset(i,l):
                if index not in remove:
                    remove.append(index)
    remove.sort()
    remove.reverse()
    for i in remove:
        c.pop(i)


uniq = {}
l = []
freq =[]
minsup = 2
itemsets = []
c = []
k=2
df=init()


while len(l)!=0:
    c = gencandidate(l,k)
    prune(c,l,k)
    l = []
    genfreq(c,l)
    k+=1

final = []

for i in freq:
    if i not in final:
        final.append(i)

print(freq)

