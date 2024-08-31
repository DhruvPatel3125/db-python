import sqlite3
conn = sqlite3.connect('c:\\sqlite\\sales.db')

conn.execute("drop table salesman")
conn.execute("create table salesman(sid int,name varchar2(10),city varchar2(10),commission number)")
print("table created")



conn.execute("insert into salesman values(5001,'mohan patel','Anand',0.15)")
conn.execute("insert into salesman values(5002,'nail shah','surat',0.13)")
conn.execute("insert into salesman values(5005,'preet vyas','ahemdabad',0.11)")
conn.execute("insert into salesman values(5006,'jeevan mehta','navsari',0.14)")
conn.execute("insert into salesman values(5003,'paul adam','nadiad',0.12)")
conn.execute("insert into salesman values(5007,'Ramesh patel','surat',0.13)")

print("record inserting")
for i in range(3):
    sid = int(input("Enter  salesman id:"))
    name = str(input("Enter the name:"))
    city = str(input("Enter the city:"))
    commission = float(input("Enter the commission:"))
    
    conn.execute(f"insert into salesman values {sid,name,city,commission}")

# conn.execute(f"insert into salesman values {sid,name,city,commission}")
# conn.execute(f"insert into salesman values {sid,name,city,commission}")
conn.commit
# sid = int(input("Enter salesman id:"))
# name = str(input("Enter the name:"))
# city = str(input("Enter the city:"))
# commission = float(input("Enter the commission:"))

# query = "insert into salesman values (?, ?, ?, ?)"
# conn.execute(query, (sid, name, city, commission))
# conn.commit()
# a=conn.execute(f"update salesman set commission = 0.15 where sid = {sid}")

# a=conn.execute("update salesman set city ='bharuch'where commission  = 0.13")

a=conn.execute("select * from  salesman")


# row=a.fetchone()
# print(row)
# for i in row:
#     print(i)
# print(a.fetchone())


# row=a.fetchall()
# for i in range(3,5):
#     if i<len(row):
#         print(row[i])


# row = a.fetchall()
# for i in range(3,5):
#     if i<len(row):
#         print(row[i])


for i in a:
    print(i)




   


