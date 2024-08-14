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