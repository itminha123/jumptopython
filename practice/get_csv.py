import csv
import math

with open("Demographic_Statistics_By_Zip_Code.csv", newline='') as infile:
    data = list(csv.reader(infile))

def get_csv_rowinstance(row_name):
    row_index = data[0].index(row_name)
    row_instance=[]
    for row in data[1:]:
        row_instance.append(row[row_index])
    # print(row_instance)
    return row_instance


def get_csv_colimninstance(col_name):
    for column in data[1:]:
        if column[0] == col_name:
            return column

def my_check(row_instance):
    for i in range(len(row_instance)):
        try:
            row_instance[i]=int(row_instance[i])
        except ValueError:
            row_instance[i]=float(row_instance[i])
    # print(row_instance)
    return row_instance

def print_row(row_name):
    for i in row_name:
        print(i,end=' ')
    print()

def my_sum(row_name):
    result = 0
    for i in row_name:
        result += i
    return result

def my_average(row_name):
    average = my_sum(row_name)/len(row_name)
    return average

def my_max(row_name):
    max_ = max(my_check(get_csv_rowinstance(row_name)))
    return max_

def my_min(row_name):
    min_ = min(my_check(get_csv_rowinstance(row_name)))
    return min_

def my_deviation(row_name):
    for i in row_name:
        print(i,end='\t\t')
        deviation= i - my_average(row_name)
        print(deviation)

def my_variance(row_name):
    veri_sum = 0
    for i in row_name:
        veri_sum += ((i - my_average(row_name))**2)
    veriance = veri_sum / len(row_name)
    return veriance

def my_standard_deviation(row_name):
    standard_deviation = math.sqrt(my_variance(row_name))
    return standard_deviation

def my_ascendant(row_name):
    return sorted(row_name)

def my_decendant(row_name):
    result= row_name
    result.sort(reverse=True)
    return result



while True:
    get_csv= input("1.열 2.행 3.총합 4.평균 5.최대값 6.최소값 7.편차 8.표준편차 9.분산 "
                   "10.오름차순 11.내림차순 (종료=0)")
    head_row = input("Header Column을 입력하세요:")
    if get_csv or head_row == '0':
        break
    elif get_csv =='1':
        print_row(get_csv_colimninstance(head_row))
    elif get_csv =='2':
        print_row(get_csv_rowinstance(head_row))
    elif get_csv =='3':
        print_row(get_csv_rowinstance(head_row))
        print("총합:",my_sum(my_check(get_csv_rowinstance(head_row))))
    elif get_csv == '4':
        print_row(get_csv_rowinstance(head_row))
        print("평균:",my_average(my_check(get_csv_rowinstance(head_row))))
    elif get_csv == '5':
        print_row(get_csv_rowinstance(head_row))
        print("최대값:",my_max(head_row))
    elif get_csv == '6':
        print_row(get_csv_rowinstance(head_row))
        print("최소값:",my_min(head_row))
    elif get_csv == '7':
        print("편차")
        my_deviation(my_check(get_csv_rowinstance(head_row)))
    elif get_csv == '8':
        print_row(get_csv_rowinstance(head_row))
        print("표준편차:",my_standard_deviation(my_check(get_csv_rowinstance(head_row))))
    elif get_csv == '9':
        print_row(get_csv_rowinstance(head_row))
        print("분산:",my_variance(my_check(get_csv_rowinstance(head_row))))
    elif get_csv == '10':
        print("오름차순")
        print_row(my_ascendant(my_check(get_csv_rowinstance(head_row))))
    elif get_csv =='11':
        print("내림차순")
        print_row(my_decendant(my_check(get_csv_rowinstance(head_row))))
    else:
        print("똑바로 해라잉")





# print_row(get_csv_rowinstance("COUNT FEMALE"))
# print_row(my_check(get_csv_rowinstance("COUNT FEMALE")))
# my_sum(my_check(get_csv_rowinstance("COUNT FEMALE")))
# get_csv_rowinstance("COUNT FEMALE")
# print_row(get_csv_colimninstance("10001"))
# my_average(my_check(get_csv_rowinstance("COUNT FEMALE")))
# print(my_max("COUNT FEMALE"))
# my_deviation(my_check(get_csv_rowinstance("COUNT FEMALE")))
# my_variance(my_check(get_csv_rowinstance("COUNT FEMALE")))
# while True:
#     print()

# my_standard_deviation(my_check(get_csv_rowinstance("COUNT FEMALE")))
#
# print_row(my_ascendant(my_check(get_csv_rowinstance("COUNT FEMALE"))))
#
# print_row(my_decendant(my_check(get_csv_rowinstance("PERCENT FEMALE"))))