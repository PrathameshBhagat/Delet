given_list=[]
num= int(input("Enter the number of elements in list:"))
for x in range(0,num):
   element=input("Enter element" + str(x+1) + ":") 
   given_list.append(element)
print(given_list)
new_list=[]
count=0
remove=input("Enter word to remove: ")
n=int(input("Enter the occurrence to remove: "))
for i in given_list:
   if(i==remove):
       count=count+1
       if(count!=n):
         new_list.append(i)
   else:
      new_list.append(i)
if(count==0):
   print("Item not found ")
else:
   print("The number of repetitions is: ",count)
   print("Updated list is: ",new_list) 
   print("The distinct elements are: ",set(given_list))