str = input("Enter a string : ")
x = str.split()
dict = {}
for word in x:
    if (word[0] not in dict.keys()):
        dict[word[0]] = [word]
    else:
        if( word not in dict[word[0]]):
            dict[word[0]].append(word)

print(dict) 