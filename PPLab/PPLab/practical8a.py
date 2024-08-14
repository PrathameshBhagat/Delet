import csv

F = open("Student.csv", "w")

csvwriter = csv.writer(F)

while True:
    op = int(input("Enter 1 to add data and 0 to quit = "))
    if (op == 1):
        bookno = input("Enter Your Book No : ") 
        bname = input("Enter Your Name : ") 
        bauthor = input("Enter Author Name : ") 
        bpublisher = input("Enter Publisher Name : ") 
        bprice = int(input("Enter Price : "))   
        csvwriter.writerow([bookno, bname , bauthor , bpublisher , bprice])
    elif (op == 0):
        break
F.close()

F = open("Student.csv", "r")

print("\nContents in File \n")

csvreader = csv.reader(F)

while True:
    try:
        for row in csvreader:
            print(row)
    except EOFError:
        break
F.close()