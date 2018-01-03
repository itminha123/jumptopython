import csv
import math

with open("",newline='') as f:
    data = list(csv.reader(f))

def get_csv_rowinstance(row_name):
    row_index= data[0].index(row_name)
    row_instance=[]
    for i in data[1:]:
        row_instance.append(i[row_index])
    return row_instance

def get_csv_columninstance(col_name):
    for column in data[1:]:
        if column[0] == col_name:
            return col_name

def print_row_col(row_name):
    for i in row_name:
        print(i,end='')
    print()

def my_check(row_instance):
    for i in range(len(row_instance)):
        try:
            row_instance[i]=int(row_instance[i])
        except ValueError:
            row_instance[i] = float(row_instance[i])
    return row_instance

def my_sum(row_name):
    result = 0
    for i in row_name:
        result += i
    return result

