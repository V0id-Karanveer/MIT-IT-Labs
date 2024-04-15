import string

alpha = list(string.ascii_lowercase)

word = input("Enter word to encrypt: ")
word2 = ""

for i in word:
    indx = alpha.index(i)
    word2 += alpha[(indx+3)%26]

print(word2)