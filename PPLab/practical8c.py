import csv
with open ("Books.csv", "w" , newline='') as F1:
    csvwriter = csv.writer(F1)
    while True:
        op = int(input("Enter 1 to add data and 0 to quit = "))
        if (op == 1):
            bookno = input("Enter Your Book No : ") 
            bname = input("Enter Your Name : ") 
            bauthor = input("Enter Author Name : ") 
            bpublisher = input("Enter Publisher Name : ") 
            bprice = int(input("Enter Price : "))   
            csvwriter.writerow([bookno, bname , bauthor , bpublisher , bprice])
        elif op == 0:
            break

F1.close()

F1 = open ("Books.csv","r")
dict = {}

csvreader = csv.reader(F1 , delimiter='@')
count=0
while True:
    try:
        for row in csvreader:
            count+=1
        break
    except EOFError:
        print("No Entry Found")
        break
print("Total No of Records = ", count)

F1.close()