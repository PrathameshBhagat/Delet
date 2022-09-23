import csv
with open ("employee.csv", "w" , newline='') as F1:

    writer = csv.writer(F1)

    while True:
        op = int(input("Enter 1 to add data and 0 to quit = "))
        if (op == 1):
            emp = input("Enter Emp = ")
            name = input ("Enter Customer Name : ")
            salary = int (input("Enter Salary : "))
            writer.writerow([emp,name,salary])
        elif op == 0:
            break
    
F1.close()

F1 = open ("employee.csv","r")

reader = csv.reader(F1 , delimiter=',')

while True:
    try:
        for row in reader:
            if( int(row[2]) > 800000 ):
                print(row)
        break
    except EOFError:
        print("No Entry Found")
        break
F1.close()
