import os
import time
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

dir_name = "v3_bigdata"
backslash = "\\"
nene_dir = "nene_data"
nene_file = "nene"
csv = ".csv"
recode_limit = 3
nene_time = time.strftime("%Y_%B_%A_%H_%M_%S",time.localtime(time.time()))
def make_dir(dir_index):
    os.mkdir(dir_name + backslash + nene_dir + str(dir_index))

def make_nene(dir_index,file_index):
    nene_csv = dir_name+backslash + nene_dir + str(dir_index) + backslash + nene_file + str(file_index) + csv
    nene_table.to_csv(nene_csv, encoding="cp949", mode='w', index=True)

def make_time(dir_index):
    nene_csv = dir_name +backslash + nene_dir + str(dir_index) + backslash + nene_file + str(nene_time)+csv
    nene_table.to_csv(nene_csv, encoding="cp949", mode='w', index=True)

try: os.mkdir(dir_name)
except: pass
try:
    with open(dir_name + backslash + "nene_index.txt",'r') as file:
        file_index = file.readline()
        file_index = int(file_index)
        dir_index = (int((file_index-1)/recode_limit)+1)
        try: make_dir(dir_index)
        except: pass
        make_time(dir_index)
        file_index += 1
    with open(dir_name + backslash + "nene_index.txt",'w') as file:
        file.write(str(file_index))

except FileNotFoundError:
    with open(dir_name+ backslash + "nene_index.txt",'w') as file:
        file.write("2")
    make_dir(1)
    make_time(1)





print("end")