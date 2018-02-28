#py -m pip install mysqlclient
import csv
import MySQLdb
import sys
from datetime import datetime, date

#csv 입력 파일 경로와 파일명
input_file = sys.argv[1]

# MYSQL 데이터베이스에 접속한다.
con = MySQLdb.connect(host='localhost', port=3306, db='my_suppliers', user='iot', passwd='1234')
c = con.cursor()

#파일 읽기
#Suppliers 테이블에 데이터를 입력한다.
file_reader = csv.reader(open(input_file, 'r'), delimiter=',')
header = next(file_reader, None)
for row in file_reader:
    data=[]
    for column_index in range(len(header)):
        if column_index < 4:
            data.append(str(row[column_index]).lstrip('$').replace(',','').strip())
        else:
            a_date = datetime.date(datetime.strptime(str(row[column_index]), '%m/%d/%y'))
            # %Y를 쓰면 연도를 2016으로 저장하고 %y를 쓰면 15로 저장한다.
            a_date = a_date.strftime("%Y-%m-%d")
            data.append(a_date)
    print(data)
    c.execute("""INSERT INTO Suppliers VALUES (%s, %s, %s, %s, %s);""", data)
con.commit()
print('')

#Suppliers 테이블에 질의한다.

c.execute("select * from Suppliers")
rows = c.fetchall()
for row in rows:
    row_list_output = []
    for column_index in range(len(row)):
        row_list_output.append(str(row[column_index]))
    print(row_list_output)