import csv
import MySQLdb
import sys

#csv 입력 파일 경로와 파일명
output_file = sys.argv[1]

# MYSQL 데이터베이스에 접속한다.
con = MySQLdb.connect(host='localhost', port=3306, db='my_suppliers', user='iot', passwd='1234')
c = con.cursor()

#파일 객체를 만들고, 헤더 행을 작성한다.
filewriter = csv.writer(open(output_file, 'w', newline=''), delimiter=',')
header = ['Supplier Name', 'Invoice Numver', 'Part Number', 'Cost', 'Purchase Date']
filewriter.writerow(header)

#Suppliers 테이블을 검색하고 결과를 csv 파일에 쓴다.
c.execute("""select *
                from Suppliers
                where Cost > 700.0;""")
rows = c.fetchall()
for row in rows:
    filewriter.writerow(row)