import sqlite3

conn = sqlite3.connect('tblemp.db')
print("database open successfully")

eid = int(input("enter the number :\n"))
conn.execute("update tblemp set salary = 125000 where eid = %d"%(eid))
conn.commit()
print("total number of rows updated :",conn.total_changes)

cursor = conn.execute("select eid,fname,lname,jdate,salary,m_id,post from tblemp")
for i in cursor:
    print("eid =",i[0])
    print("fname =",i[1])
    print("lname =",i[2])
    print("jdate =",i[3])
    print("salary =",i[4])
    print("m_id =",i[5])
    print("post =",i[6])
print("updated successfully")
conn. close()