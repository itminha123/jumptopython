import sqlite3

#메모리에 SQLite3 데이터베이스를 만든다.
#네 가지 속성을 지닌 sales 테이블을 만든다.
con =sqlite3.connect('Suppliers.db')
query = """CREATE TABLE IF NOT EXISTS sales
        (customer VARCHAR(20),
        product VARCHAR(20),
        amount FLOAT,
        date DATE);"""
con.execute(query)
con.commit()

con.execute("DELETE FROM Suppliers WHERE Supplier_Name='Supplier Z';")
con.commit()

#Suppliers 테이블에 질의한다.
cursor = con.execute("select * from Suppliers")
rows = cursor.fetchall()
for row in rows:
    output = []
    for column_index in range(len(row)):
        output.append(str(row[column_index]))
    print(output)