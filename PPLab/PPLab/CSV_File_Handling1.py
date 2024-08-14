import csv

file = open("Book.csv", "w", newline="")
write = csv.writer(file)
write.writerow(['bookno', 'bname', 'bauthor', 'bpublisher', 'bprice'])
b = []
while True :
    print("Enter Book Details: ")
    bno = int(input("Enter the book number: "))
    bname = input("Enter book name: ")
    bauthor = input("Enter author of the book: ")
    bpub = input("Enter the book publisher: ")
    bpr = int(input("Enter the price of the book: "))
    book = [bno, bname, bauthor, bpub, bpr]
    b.append(book)
    ch = input("Do you want to continue: ")
    if ch == 'n' or ch == 'N' :
        break
for i in b :
    write.writerow(i)
file.close()
