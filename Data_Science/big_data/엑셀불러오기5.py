import math
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

def print_row(row_instance, type='int'):
    if type == 'int':
        list(map(int, row_instance))
    elif type == 'float':
        list(map(float, row_instance))
    elif type == 'str':
        list(map(str, row_instance))

    for i in row_instance:
        print(i, end=' ')
    return  row_instance

def check_type(row_name):
    result = []
    for i in range(len(row_name)):
        try:
            row_name[i] = int(row_name[i])
            result.append(row_name[i])
        except :
            row_name[i] = float(row_name[i])
            result.append(row_name[i])
    print(result)

def get_csv_colinstance(col_name):
    name = list(get_csv_rowinstance("JURISDICTION NAME"))
    col_index=name.index(str(int(col_name)+1))
    col_instance=[2]
    for cloumn in data[col_index]:
        col_instance.append(cloumn)
    return col_instance

def print_col(col_instance) :
    for i in col_instance:
        print(i,end=' ')
    print()

def my_sum(row_name):
    for j in row_name:
        print(j, end=' ')
    print()
    result= 0
    for i in row_name:
        result += float(i)
    print('%g'%result)
    # return result

def my_average(row_name):
    for j in row_name:
        print(j,end=' ')
    print()
    result =0
    for i in row_name:
        result += float(i)
    print("%g" % (result/len(row_name)))

def my_max(row_name):
    for j in row_name:
        print(j,end=' ')
    print()
    a= max(list(map(float,row_name)))
    print("%g" % a)
    # return row_name

def my_min(row_name):
    for j in row_name:
        print(j,end=' ')
    print()
    print("%g" % (min(list(map(float,row_name)))))
    # return row_name

def my_deviation(row_name):
    result = 0
    for i in row_name:
        result += float(i)
    average = result / len(row_name)
    for j in row_name:
        print(j,end='        ')
        deviation = float(j) - average
        print("%g"%deviation)
    # return row_name

def my_variance(row_name):
    for j in row_name:
        print(j,end=' ')
    print()
    result = 0
    for i in row_name:
        result += float(i)
    average = result / len(row_name)
    vari_sum = 0
    for i in row_name:
        vari_sum += ((float(i) - average) ** 2)
    variance = vari_sum / len(row_name)
    print("%g" % variance)
    # return row_name

def my_standard_deviation(row_name):
    for j in row_name:
        print(j,end=' ')
    print()
    result = 0
    for i in row_name:
        result += float(i)
    average = result / len(row_name)
    vari_sum = 0
    for i in row_name:
        vari_sum += ((float(i) - average) ** 2)
    variance = vari_sum / len(row_name)
    standard_deviation = math.sqrt(variance)
    print("%g" % standard_deviation)
    # return row_name

def my_ascendeant(row_name):
    result = list(map(float,row_name))
    result.sort()
    for i in result:
        print("%g" % i, end=' ')
    print()
    # return row_name

def my_descendent(row_name):
    result= list(map(float,row_name))
    result.sort(reverse=True)
    for i in result:
        print("%g" % i,end=' ')
    print()

while True:
    number = input("1.총합 2.평균 3.최대값 4.최소값 5.편차 6.표준편차 7.분산 8.정렬 "
                       "9.행 10.열 (종료=0)")
    if number == '0':
        break

    elif number == '1' :
        row_name = input("Header Column을 입력하세요.")
        my_sum(get_csv_rowinstance(row_name))

    elif number == '2' :
        row_name = input("Header Column을 입력하세요.")
        my_average(get_csv_rowinstance(row_name))

    elif number == '3' :
        row_name = input("Header Column을 입력하세요.")
        my_max(get_csv_rowinstance(row_name))

    elif number == '4' :
        row_name = input("Header Column을 입력하세요.")
        my_min(get_csv_rowinstance(row_name))

    elif number == '5' :
        row_name = input("Header Column을 입력하세요.")
        my_deviation(get_csv_rowinstance(row_name))

    elif number == '6' :
        row_name = input("Header Column을 입력하세요.")
        my_standard_deviation(get_csv_rowinstance(row_name))

    elif number == '7' :
        row_name = input("Header Column을 입력하세요.")
        my_variance(get_csv_rowinstance(row_name))

    elif number == '8' :
        line_sort = input("1.오름차순 2.내림차순")
        if line_sort == '1' :
            row_name = input("Header Column을 입력하세요.")
            my_ascendeant(get_csv_rowinstance(row_name))
        elif line_sort == '2' :
            row_name = input("Header Column을 입력하세요.")
            my_descendent(get_csv_rowinstance(row_name))
        else:
            print_row("똑바로 해라잉")

    elif number == '9':
        column = input("Header Column을 입력하세요:")
        print("행 데이터는 아래와 같습니다.")
        print_row(get_csv_rowinstance(column))

    elif number == '10':
        row = input("Access Key를 입력하세요:")
        print("열 데이터는 아래와 같습니다.")
        print_col(get_csv_colinstance(row))
    else:
        print("똑바로 해라잉")




# my_average(print_row(get_csv_rowinstance("PERCENT FEMALE"),'float'))
# my_average(get_csv_rowinstance("PERCENT FEMALE"))
# my_sum(get_csv_rowinstance("COUNT FEMALE"))
# my_max(get_csv_rowinstance("PERCENT FEMALE"))
# my_min(get_csv_rowinstance("COUNT FEMALE"))
# my_deviation(get_csv_rowinstance("COUNT FEMALE"))
# my_standard_deviation(get_csv_rowinstance("COUNT FEMALE"))
# my_deviation(get_csv_rowinstance("COUNT FEMALE"))
# my_variance(get_csv_rowinstance("COUNT FEMALE"))
# my_average(get_csv_rowinstance("COUNT FEMALE"))
# my_ascendeant(get_csv_rowinstance("COUNT FEMALE"))
# my_descendent(get_csv_rowinstance("COUNT FEMALE"))
