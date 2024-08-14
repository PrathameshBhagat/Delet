'''
#print count in file
f = open("myfile.txt", "w")
lines = ["Hello! Myself Suyash Sunil Patalbansi.\n", "I am a Second Year Computer Engineering student.\n", "I Love Programming."]
f.writelines(lines)
f.close()

f = open("myfile.txt", "r")
data = f.read()
count = 0
for i in data :
    count++
print("No. of characters : ", count)
f.close()
'''

'''
#print words of a file
f = open("myfile.txt", "w")
lines = ["Hello! Myself Suyash Sunil Patalbansi.\n", "I am a Second Year Computer Engineering student.\n", "I Love Programming."]
f.writelines(lines)
f.close()

f = open("myfile.txt", "r")
data = f.read()
w = data.split()
print(w)
count = 0
for i in w :
    count = count + 1
print("No. of characters : ", count)
f.close()
'''

'''
#print lines of a file
f = open("myfile.txt", "w")
lines = ["Hello! Myself Suyash Sunil Patalbansi.\n", "I am a Second Year Computer Engineering student.\n", "I Love Programming."]
f.writelines(lines)
f.close()

f = open("myfile.txt", "r")
data = f.readlines()
w = data.split()
print(w)
count = 0
for i in w :
    count = count + 1
print("No. of characters : ", count)
f.close()
'''

'''
#print words of a file
f = open("myfile.txt", "w")
lines = ["Hello! Myself Suyash Sunil Patalbansi.\n", "I am a Second Year Computer Engineering student.\n", "I Love Programming."]
f.writelines(lines)
f.close()

f = open("myfile.txt", "r")
data = f.read()
count = 0
for i in data :
    if i.islower() :
        count = count + 1
print("No. of characters : ", count)
f.close()
'''

'''
#print words of a file
f = open("myfile.txt", "w")
lines = ["Hello! Myself Suyash Sunil Patalbansi.\n", "I am a Second Year Computer Engineering student.\n", "I Love Programming."]
f.writelines(lines)
f.close()

f = open("myfile.txt", "r")
data = f.read()
w = data.split()
count = 0
for i in w :
    if i[0] == 'a' :
        count = count + 1
print("No. of characters : ", count)
f.close()
'''

'''
#user would be giving letter of his choice and check the occurence of letter in the file
f = open("myfile.txt", "w")
lines = ["Hello! Myself Suyash Sunil Patalbansi.\n", "I am a Second Year Computer Engineering student.\n", "I Love Programming."]
f.writelines(lines)
f.close()

f = open("myfile.txt", "r")
c = input("Enter the character : ")
data = f.read()
count = 0
for i in data :
    if i == c :
        count = count + 1
print("No. of characters : ", count)
f.close()
'''

'''
#user would be giving word of his choice and check the occurence of word in the file
f = open("myfile.txt", "w")
lines = ["Hello! Myself Suyash Sunil Patalbansi.\n", "I am a Second Year Computer Engineering student.\n", "I Love Programming."]
f.writelines(lines)
f.close()

f = open("myfile.txt", "r")
c = input("Enter the word : ")
data = f.read()
w = data.split()
count = 0
for i in w :
    if i == c :
        count = count + 1
print("No. of characters : ", count)
f.close()
'''

'''
#user would be giving word of his choice and check the occurence of word in the file
f = open("myfile.txt", "w")
lines = ["Hello! Myself Suyash Sunil Patalbansi.\n", "I am a Second Year Computer Engineering student.\n", "I Love Programming."]
f.writelines(lines)
f.close()

f = open("myfile.txt", "r")
c = input("Enter the word : ")
data = f.read()
w = data.split()
count = 0
flag = 0
for i in w :
    if i == c :
        flag = 1
if flag == 0 :
    print("Element not found")
else :
    print("Element found")
f.close()
'''

'''
#to print a file in reverse order
f = open("myfile.txt", "w")
lines = ["Hello! Myself Suyash Sunil Patalbansi.\n", "I am a Second Year Computer Engineering student.\n", "I Love Programming."]
f.writelines(lines)
f.close()

f = open("myfile.txt", "r")
data = f.read()
print(data[::-1])
f.close()
'''

#write a file into a file in reverse order
f = open("myfile.txt", "w")
lines = ["Hello! Myself Suyash Sunil Patalbansi.\n", "I am a Second Year Computer Engineering student.\n", "I Love Programming."]
f.writelines(lines)
f.close()

f = open("myfile.txt", "r")
data = f.read()
rev = data[::-1]
f.close()

f = open("filecopy.txt", "w")
f.write(rev)
f.close()














