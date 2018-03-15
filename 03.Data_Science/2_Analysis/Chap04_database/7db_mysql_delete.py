import MySQLdb

# MYSQL 데이터베이스에 접속한다.
con = MySQLdb.connect(host='localhost', port=3306, db='my_suppliers', user='iot', passwd='1234')
c = con.cursor()

c.execute("DELETE FROM Suppliers WHERE Supplier_Name='Supplier X';")
con.commit()

#Suppliers 테이블에 질의한다.
c.execute("select * from Suppliers")
rows = c.fetchall()
for row in rows:
    output = []
    for column_index in range(len(row)):
        output.append(str(row[column_index]))
    print(output)