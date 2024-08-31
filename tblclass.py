import sqlite3
conn = sqlite3.connect('c:\\sqlite\\tblclass.db')
#a = conn.execute('create table tblclass1(cno int,cname varchar2(10),no_stud int)')
print('table created')

# conn.execute("insert into tblclass1 values(1,'math',40)")
# conn.execute("insert into tblclass1 values(2,'account',23)")
# conn.execute("insert into tblclass1 values(3,'bio',45)")
# conn.execute("insert into tblclass1 values(4,'chem',34)")
# conn.execute("insert into tblclass1 values(5,'phy',56)")
# conn.execute("insert into tblclass1 values(6,'ai',45)")
# conn.execute("insert into tblclass1 values(7,'eng',35)")
# conn.commit
# print("record inserted")

res = conn.execute('select * from  tblclass1')
d= res.fetchall()
for i in d:
    print(i[0],i[1],i[2])
