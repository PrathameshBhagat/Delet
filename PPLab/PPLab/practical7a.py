import pickle
F = open("Student.dat", "wb")
while True:
    op = int(input("Enter 1 to add data and 0 to quit = "))
    if (op == 1):
        name = input("Enter Your Name : ")
        rollno = int(input("Enter Your Roll Number : "))
        pickle.dump([name, rollno], F)
    elif (op == 0):
        break

F = open("Student.dat", "rb")

print("\nContents in File \n")

while True:
    try:
        l = pickle.load(F)
        print(l)
    except EOFError:
        break
F.close()