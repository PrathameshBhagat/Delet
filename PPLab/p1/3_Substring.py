
stg = input("Enter the String : ")
substg = input("Enter the Sub-String you want to Find : ")
result = stg.find(substg)
if(result >= 0):
    print("Sub-String <" +substg+ "> is Present in Given String.")
else :
    print("Sub-String <" +substg+ "> is NOT Present in Given String.")
