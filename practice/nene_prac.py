import os
import urllib.request
from  pandas import  DataFrame
import  xml.etree.ElementTree as ET

response = urllib.request.urlopen('http://nenechicken.com/subpage/where_list.asp?target_step2=%s&proc_type=step1&target_step1=%s'%(urllib.parse.quote('전체'),urllib.parse.quote('전체')))
html = response.read().decode('UTF-8')
root = ET.fromstring(html)


result = []

for element in root.findall('item'):
    store_name = element.findtext('aname1')
    store_sido = element.findtext('aname2')
    store_gungu = element.findtext('aname3')
    store_address = element.findtext('aname5')

    result.append([store_name]+[store_sido]+[store_gungu]+[store_address])

nene_table = DataFrame(result, columns=('store','sido','gungu','store_address'))
# nene_table.to_csv('nene.csv',encoding="cp949",mode='w',index=True)

dir_name = "v1_bigdata"
backslash = "\\"
nene_dir = "nene_data"
nene_file = "nene"
csv = ".csv"

def make_nene(file_index):
    nene_csv = dir_name+backslash + nene_dir + backslash + nene_file + str(file_index) + csv
    nene_table.to_csv(nene_csv, encoding="cp949", mode='w', index=True)

try: os.mkdir(dir_name)
except: pass
try:
    with open(dir_name + backslash + "nene_index.txt",'r') as file:
        file_index = file.readline()
        file_index = int(file_index)
        make_nene(file_index)
        file_index += 1
    with open(dir_name + backslash + "nene_index.txt",'w') as file:
        file.write(str(file_index))

except FileNotFoundError:
    with open(dir_name+ backslash + "nene_index.txt",'w') as file:
        file.write("2")
    os.mkdir(dir_name + backslash + nene_dir)
    make_nene(1)




print("end")