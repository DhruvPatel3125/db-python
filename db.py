import sqlite3

conn = sqlite3.connect('tblemp223.db')
print("open data successfuly")
conn.execute('''create table tblemp223(eid,fname,lname,jdate,salary,m_id,post);''')

conn.execute("insert into tblemp223 values(101,'hemant','sharma','20-jan-1995',50000,0,'manager')");


conn.execute("insert into tblemp223 values(102,'rita','gandhi','20-dec-1997',45000,0,'manager')");

conn.execute("insert into tblemp223(eid,fname,lname,jdate,salary,m_id,post)\
             values(103,'maya','mistry','20-dec-1997',30000,101,'programmer')");
conn.commit()
print("records created successfully")
conn.close()


# insert into tblemp values(101,'hemant','sharma','20-jan-1995',50000,0,'manager');
# insert into tblemp values(102,'rita','gandhi','20-dec-1997',45000,0,'manager');
# insert into tblemp values(103,'maya','mistry','20-dec-1997',30000,101,'programmer');
# insert into tblemp values(104,'riya','patel','15-nov-2001',28000,102,'programmer');
# insert into tblemp values(105,'shreya','patel','17-oct-2010',5000,101,'peon');
# insert into tblemp values(106,'karan','patel','19-aug-2015',5000,102,'peon');
# insert into tblemp values(107,'peyanshi','vyas','05-jun-2011',15000,101,'clerk');
# insert into tblemp values(108,'mehul','mehta','06-may-2010',17000,102,'clerk');
# insert into tblemp values(109,'krupali','patil','08-apr-2015',10000,101,'accountant');
# insert into tblemp values(110,'maitry','vyas','11-mar-2017',10000,102,'accountant');
# # insert into tblemp values(111,'mohan','mehta','27-feb-2020',15000,101,'electrician');

# cursor = conn.execute("select eid,fname,lname,jdate,salary,m_id,post")
# for row in cursor:
#     print("employee eid=", row[0])
#     print("employee fname = ",row[1])
#     print("employee lname =",row[2])
#     print("employee jdate =",row[3])
#     print("employee salary =",row[4])
#     print("employee managerid =",row[5])

#     print("employee post =",row[6],"\n")

#     print("operation done successfully")
# conn.close()