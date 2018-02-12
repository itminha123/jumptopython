
def make_nene(index) :
    nene = "nene"
    csv = ".csv"
    nene_table.to_csv(nene + index + csv, encoding="cp949", mode='w', index=True)
    return None

try :
    with open("nene_index.txt", 'r') as file :
        index = file.readline()
        make_nene(index)
        index = int(index)
        index += 1
        index = str(index)
    with open("nene_index.txt", 'w') as file :
        file.write(index)
except FileNotFoundError :
    with open("nene_index.txt", 'w') as file :
        file.write('2')
    make_nene('1')
print("End")

if os.path.isfile("E:\workspace\Python\Jumptopy\XML\V1_BigData\\nene.csv"):
    if os.path.isfile("E:\workspace\Python\Jumptopy\XML\V1_BigData\\count.txt"):
        count_number = open("E:\workspace\Python\Jumptopy\XML\V1_BigData\\count.txt", 'r')
        count = str(count_number.readline())
        count_number.close()
        nene_table.to_csv('nene%s.csv' % count, encoding="cp949", mode='w', index=True)
        count = int(count) + 1
        count = str(count)
        count_number_new = open("E:\workspace\Python\Jumptopy\XML\V1_BigData\\count.txt", 'w')
        count_number_new.write(count)
        count_number_new.close()
    else:
        make_count = open("E:\workspace\Python\Jumptopy\XML\V1_BigData\\count.txt",'a')
        data = '1'
        make_count.write(data)
        make_count.close()
        count_number = open("E:\workspace\Python\Jumptopy\XML\V1_BigData\\count.txt", 'r')
        count = str(count_number.readline())
        count_number.close()
        nene_table.to_csv('nene%s.csv' % count, encoding="cp949", mode='w', index=True)
        count = int(count) + 1
        count = str(count)
        count_number_new = open("E:\workspace\Python\Jumptopy\XML\V1_BigData\\count.txt", 'w')
        count_number_new.write(count)
        count_number_new.close()

else:
    nene_table.to_csv('E:\workspace\Python\Jumptopy\XML\V1_BigData\\nene.csv', encoding="cp949", mode='w', index=True)
