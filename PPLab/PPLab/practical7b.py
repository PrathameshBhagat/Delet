import pickle
with open ("customer.dat", "wb") as F1:
    while True:
        op = int(input("Enter 1 to add data and 0 to quit = "))
        if (op == 1):
            name = input ("Enter Custmer Name : ")
            city = input ("Enter Your City : ")
            amount = int (input("Enter Amount : "))
            pickle.dump([city,name,amount], F1)
        elif op == 0:
            break
F1 = open ("customer.dat","rb")
while True:
    try:
        l = pickle.load(F1)
        if (l[0].lower()=="delhi"):
            print(l)
    except EOFError:
        print("No Entry Found")
        break
F1.close()