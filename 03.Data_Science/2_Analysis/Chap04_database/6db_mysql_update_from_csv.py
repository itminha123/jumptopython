import csv
import MySQLdb
import sys

#csv 입력 파일 경로와 파일명
input_file = sys.argv[1]

# MYSQL 데이터베이스에 접속한다.
con = MySQLdb.connect(host='localhost', port=3306, db='my_suppliers', user='iot', passwd='1234')
c = con.cursor()

#csv파일을 읽고, 특정 행의 데이터를 갱신한다.
file_reader = csv.reader(open(input_file, 'r'), delimiter=',')
header = next(file_reader, None)
for row in file_reader:
    data=[]
    for column_index in range(len(header)):
        data.append(str(row[column_index]).strip())
    print(data)
    c.execute("""UPDATE Suppliers SET Cost=%s, Purchase_Date=%s WHERE Supplier_Name=%s;""", data)
con.commit()

#Suppliers 테이블에 질의한다.
c.execute("select * from Suppliers")
rows = c.fetchall()
for row in rows:
    output = []
    for column_index in range(len(row)):
        output.append(str(row[column_index]))
    print(output)