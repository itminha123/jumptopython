#http://nenechicken.com/subpage/where/where_list.asp?target_step1=%EC%A0%84%EC%B2%B4&target_step2=%EC%A0%84%EC%B2%B4&proc_type=step1
import urllib.request
import os
import time
from pandas import DataFrame
import xml.etree.ElementTree as ET

result = []
dir_name = "V2_BigData"
dir_delimiter = "\\"
nene_dir = "Nene_Data"
nene_file = "nene"
csv = ".csv"
record_limit = 3

def make_dir(index) :
    os.mkdir(dir_name + dir_delimiter + nene_dir+str(index))
    return None

def make_nene(dir_index, file_index) :
    destination_csv = dir_name + dir_delimiter + nene_dir + str(dir_index) + dir_delimiter + nene_file + str(file_index) + csv;
    nene_table.to_csv(destination_csv,encoding="cp949", mode='w', index=True)
    return None

response = urllib.request.urlopen('http://nenechicken.com/subpage/where_list.asp?target_step2=%s&proc_type=step1&target_step1=%s'%(urllib.parse.quote('전체'),urllib.parse.quote('전체')))
xml = response.read().decode('UTF-8')
root = ET.fromstring(xml)

for element in root.findall('item'):
    store_name = element.findtext('aname1')
    store_sido = element.findtext('aname2')
    store_gungu = element.findtext('aname3')
    store_address = element.findtext('aname5')
    result.append([store_name]+[store_sido]+[store_gungu]+[store_address])

nene_table = DataFrame(result,columns=('sotre','sido','gungu','store_address'))

try : os.mkdir(dir_name)
except : pass
try :
    with open(dir_name + dir_delimiter + "nene_index.txt", 'r') as file :
        file_index = file.readline()
        file_index = int(file_index)
        dir_index = int(file_index / record_limit)
        if file_index % record_limit != 0 :
            dir_index = dir_index+1
        if file_index % record_limit == 1 :
            make_dir(dir_index)
        make_nene(dir_index, file_index)
        n= 0
        for i in range(100, len(nene_table), 100):
            nene_table[n:i].to_csv()

        file_index += 1
    with open(dir_name + dir_delimiter + "nene_index.txt", 'w') as file :
        file.write(str(file_index))
except FileNotFoundError :
    with open(dir_name + dir_delimiter + "nene_index.txt", 'w') as file :
        file.write('2')
    make_dir(1)
    make_nene(1, 1)
print("End")

