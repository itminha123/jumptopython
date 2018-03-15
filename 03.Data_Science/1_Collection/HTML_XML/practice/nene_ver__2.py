import urllib.request , os , glob
from pandas import  DataFrame
result = []

import  xml.etree.ElementTree as ET
response = urllib.request.urlopen('http://nenechicken.com/subpage/where_list.asp?target_step2=%s&proc_type=step1&target_step1=%s'%(urllib.parse.quote('전체'),urllib.parse.quote('전체')))

xml = response.read().decode('UTF-8')
root = ET.fromstring(xml)

for element in root.findall('item'):
    store_name = element.findtext('aname1')
    store_sido = element.findtext('aname2')
    store_gungu = element.findtext('aname3')
    store_address = element.findtext('aname5')

    result.append([store_name]+[store_sido]+[store_gungu]+[store_address])

nene_table = DataFrame(result,columns=('store','sido','gungu','store_address'))

try:
    count = 1
    number =1
    number2 =2
    file_list = glob.glob("D:\\python\\01.jumptopython\\01.jumptopython\\chap07\\practice\\V1_BigData\\Nene_Data[1]/nene*")
    print(file_list)
    while True:
        if len(file_list) == 3:
            os.system("mkdir V1_BigData\\Nene_Data[%s]"% number2)
            number2 += 1
            number += 1
            break
        try:
            f = open("D:\\python\\01.jumptopython\\01.jumptopython\\chap07\\practice\\V1_BigData\\Nene_Data[%s]\\nene%s.csv" % (number ,count) , 'r')
            data = f.read()
            count += 1
        except:
            nene_table.to_csv('V1_BigData\\Nene_Data[%s]\\nene%s.csv' % (number ,count) , encoding="cp949", mode='w', index=True)
            break

except:
    os.system("mkdir V1_BigData\\Nene_Data[1]")
    nene_table.to_csv('V1_BigData\\Nene_Data[1]\\nene.csv', encoding="cp949", mode='w', index=True)
print("End")

