import math
import csv
with open("C:\\Users\\USER\\Downloads\\Demographic_Statistics_By_Zip_Code.csv",newline='') as infile:
    data = list(csv.reader(infile))

def my_sum(row_name):
    result= 0
    for i in row_name:
        result += int(i)
    print(result)

def my_average(row_name):
    result =0
    for i in row_name:
        result += int(i)
    print(result/len(row_name))

def my_max(row_name):
    print(max(row_name))

def my_min(row_name):
    return min(row_name)

def my_deviation(row_name):
    result =0
    for i in row_name:
        result += int(i)
    average=result/len(row_name)

    for i in row_name:
        deviation= int(i) - average
    return  deviation

def my_variance(row_name):
    result =0
    for i in row_name:
        result += int(i)
    average=result/len(row_name)
    vari_sum = 0
    for i in row_name:
        vari_sum += ((int(i) - average)**2)
    variance = vari_sum/len(row_name)
    return row_name

def my_standard_deviation(row_name):
    result =0
    for i in row_name:
        result += int(i)
    average=result/len(row_name)
    vari_sum = 0
    for i in row_name:
        vari_sum += ((int(i) - average)**2)
    variance = vari_sum/len(row_name)
    standard_deviation = math.sqrt(variance)
    return row_name

def ascendeant_descendent(row_name):
    for i in row_name:
        print(sorted(i),end=' ')
    for j in row_name:
        print(j,end=' ')
    print()

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

def print_row(row_instance, type="int"):
    if type == "int":
        list(map(int, row_instance))
    elif type == "float":
        list(map(float, row_instance))
    for i in row_instance:
        print(i, end=' ')

def get_csv_rowinstance(row_name):
    row_index = data[0].index(row_name)
    row_instance=[]
    for column in data[1:]:
        row_instance.append(column[row_index])
    return row_instance


# check_type(get_csv_rowinstance("PERCENT FEMALE"))
# print_row(get_csv_rowinstance("COUNT FEMALE"))
# print_row(get_csv_rowinstance("COUNT FEMALE"))

# print_row(get_cvs_rowInstance("COUNT FEMALE"))
# my_max(check_type(get_csv_rowinstance("COUNT FEMALE")))
# my_max(row_name)
my_sum(check_type(get_csv_rowinstance("COUNT FEMALE")))
# my_sum(check_type(get_csv_rowinstance("PERCENT FEMALE")))




