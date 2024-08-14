#Program to check if String is palindrome or not
'''
str = input("Enter a String : ")
strrev = str[::-1]
if( str == strrev ):
    print("The string is palindrome")
else:
    print("The string is not palindrome")
'''

#To check if Substring is Presesnt or not 

'''
str = input("Enter a String : ")
substr = input("Enter a substring : ")
result = str.find(substr)
if (result >= 0 ):
    print("Substring is Present")
else:
    print("Substring is not Present")
'''

#Program to count occurance of word in a given String

'''
str = input("Enter the String : ")
str_list = str.split()
unique_words = set(str_list)
for words in unique_words:
    print("Frequency of " , words ," : " , str_list.count(words))
'''


#Program to remove the ith occurance of the given word in a list where words repeat

given_list = []
num = int(input("Enter no. of element in list : "))
for n in range(0, num):
    ele = input('enter element : ' )
    given_list.append(ele)
print(given_list)

new_list = []
count = 0
remove = input("Enter word to remove : ")
n = int(input("Enter occurence to remove : "))

for i in given_list:
    if(i == remove):
        count = count+1
        if(count == n ):
            pass
        else:
            new_list.append(i)
    else:
        new_list.append(i)

if(count < n ):
    print("Elemnt Not found")

print("the Number of Repetition is : " , count )
print("Original List : " , given_list )
print("Updated List : " , new_list )