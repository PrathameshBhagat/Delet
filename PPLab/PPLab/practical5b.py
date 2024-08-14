my_string = input("Enter the String : ")
my_list = my_string.split()
new_dict = dict()
for i in my_list:
    new_dict.update({i : my_list.count(i)})

print(new_dict)
