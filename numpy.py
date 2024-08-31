# import sqlite3
# conn = sqlite3.connect('c:\\sqlite\\studsy4.db')
# # a=conn.execute('create table tblso(rno int,name varchar2(20))')
# # print("table created")
# conn.execute("insert into tblso values(1,'jinal')")
# conn.execute("insert into tblso values(2,'pinal')")
# conn.execute("insert into tblso values(3,'kinal')")
# conn.execute('commit')
# print('record inserted')

# res = conn.execute("select * from tblso")
# row = res.fetchall()
# print(row)
# print(row[0][0])


# # import sqlite3

# # # Connect to the database
# # conn = sqlite3.connect('c:\\sqlite\\studsy4.db')

# # # Create a cursor object
# # cursor = conn.cursor()

# # # Create table
# # cursor.execute('CREATE TABLE tbls (rno INT, name VARCHAR(20))')
# # print("Table created")

# # # Insert records
# # cursor.execute("INSERT INTO tbls VALUES (1, 'jinal')")
# # cursor.execute("INSERT INTO tbls VALUES (2, 'pinal')")
# # cursor.execute("INSERT INTO tbls VALUES (3, 'kinal')")

# # # Commit the transaction
# # conn.commit()
# # print('Records inserted')

# # # Close the connection
# # conn.close()


import sqlite3

# Connect to the database
conn = sqlite3.connect('c:\\sqlite\\studsy4.db')

# Create a cursor object
cursor = conn.cursor()

# Create table
cursor.execute('CREATE TABLE IF NOT EXISTS tbls (rno INT, name VARCHAR(20))')
print("Table created")

# List of records to be inserted
records = [(1, 'jinal'), (2, 'pinal'), (3, 'kinal')]

# Insert records using a for loop
for record in records:
    cursor.execute("INSERT INTO tbls VALUES (?, ?)", record)

# Commit the transaction
conn.commit()
print('Records inserted')

# Close the connection
conn.close()

res =conn.execute("select * from tbls")
rows = res.fetchall()
print("records:")
for row in rows:
    print("Roll no:",row[0],"name",row[1])
conn.close()