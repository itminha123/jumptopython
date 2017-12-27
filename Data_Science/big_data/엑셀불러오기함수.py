import csv
with open("C:\\Users\\USER\\Downloads\\Demographic_Statistics_By_Zip_Code.csv", newline='') as infile:
    data = list(csv.reader(infile))

def get_csv_rowinstance(row_name):
    row_index = data[0].index(row_name)
    # print("The index" + str(row_index))
    row_instance = []
    for cloumn in data[1:]:
        row_instance.append(cloumn[row_index])
    # print(row_instance)
    return row_instance

# get_csv_rowinstance("COUNT FEMALE")

def print_row(row_instance,type='int'):
        if type == 'int' :
            list(map(int,row_instance))
        elif type == 'float' :
            list(map(float,row_instance))

        for i in row_instance:
            print(i)

def print_col(col_instance):
    for i in col_instance:
        print_row(i)

# print_row(get_csv_rowinstance("PERCENT FEMALE"),'float')

def get_csv_colinstance(col_name):
    name = list(get_csv_rowinstance("JURISDICTION NAME"))
    col_index=name.index(str(int(col_name)+1))
    col_instance=[2]
    for cloumn in data[col_index]:
        col_instance.append(cloumn)

    return col_instance


def print_col(col_instance) :
    # if type == 'int':
    #     list(map(int,col_instance))
    # elif type == 'float':
    #     list(map(float,col_instance))
    for i in col_instance:
        print(i)


while True:
    number = int(input("Access 데이타유형 ( 1.행 , 2.열 , 3.종료 )"))
    if number == 3 :
        break
    if number == 1:
        column = input("Access Key를 입력하세요:")
        print("행 데이터는 아래와 같습니다.")
        print_row(get_csv_rowinstance(column))

    elif number == 2:
        row = input("Access Key를 입력하세요:")
        print("열 데이터는 아래와 같습니다.")
        print_col(get_csv_colinstance(row))




