import sqlite3

conn = sqlite3.connect('employees.sqlite3')

cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Employee ')
cur.execute('''CREATE TABLE Employee(
    EmpId integer, 
    FirstName varchar(20), 
    LastName varchar(20), 
    Email varchar(25), 
    PhoneNo varchar(25), 
    Salary integer
)''')

sqlInsert =  "INSERT INTO Employee VALUES(?,?,?,?,?,?)"
val = (1,'John','King','john.king@abc.com','123.123.1834',33000)
val = (1,'James','Lion','james.lion@def.com','123.456.1834',55000)

cur.execute(sqlInsert , val)

emp = [ 
    (4,'Lex','De Haan','lex@test.com','123.456.4569',15000),
    (3,'Neena','Kochhar','neena@test.com','123.456.4568',17000)
]

print("\n------------------------Original------------------------\n")


cur.executemany("INSERT INTO Employee VALUES(?,?,?,?,?,?)" , emp)

item = cur.execute("SELECT * FROM Employee")
for i in item:
        print(i)

print("\n------------------------After Updating------------------------\n")

cur.execute('''UPDATE Employee
SET email = 'jking@test.com'
WHERE EmpId = 1;''')



item = cur.execute("SELECT * FROM Employee")
for i in item:
        print(i)
        
print("\n------------------------After Deleting------------------------\n")

cur.execute("DELETE FROM Employee WHERE EmpId = 4")
item = cur.execute("SELECT * FROM Employee")
for i in item:
        print(i)

print("\n------------------------Salary Between 5000 and 20000------------------------\n")


item = cur.execute("SELECT * FROM Employee Where Salary Between 5000 and 20000")
for i in item:
        print(i)

print("\n------------------------After Ordering------------------------\n")


item = cur.execute("SELECT * FROM Employee ORDER BY FirstName")
for i in item:
        print(i)


print("\n------------------------Name that Starts with J------------------------\n")


item = cur.execute("SELECT * FROM Employee WHERE FirstName LIKE 'J%' ")
for i in item:
        print(i)

conn.close()
