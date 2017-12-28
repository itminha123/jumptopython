import math
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
    return max(row_name)

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




