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
    name = get_csv_rowinstance("JURISDICTION NAME")
    col_index = name.index(str(col_name))
    col_instance=[]
    for cloumn in data[col_index]:
        col_instance.append(cloumn)
    print(col_instance)
    return col_instance


get_csv_colinstance(10002)
