#Demonstrate working of all string functions in Python

str = input("Enter the string : ")
string = str

#capitalize() : Upper Case first letter of the word and lower case others.
print('capitalize() : ', str.capitalize())

str = string
#count() : counts the occurence of a word in a string
s = input("Enter the word to be counted : ")
print('count() : ', str.count(s))

str = string
#find() : Returns the index where the parameter is found in the given string
s = input("Enter the word to be found : ")
print('At index : ', str.find(s))
