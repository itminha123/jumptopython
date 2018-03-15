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


# 디렉토리안의 csv확장자를 가지고 있는 파일들을 찾아준다.
# file_list = glob.glob("*.csv")
#
# f = nene_table.to_csv('nene.csv', encoding='cp949', mode='w', index=True)
#     try:
#         if file_list[-1] == open("nene"+str(count)+".csv",'r'):
#             count = count + 1
#             nene_table.to_csv('nene'+count+'.csv' , encoding='cp949', mode='w', index=True)
#     except:
#         nene_table.to_csv('nene'+count+'.csv'  , encoding='cp949', mode='w', index=True)


try:
    count = 1
    while True:
        try:
            f = open("D:\\python\\01.jumptopython\\01.jumptopython\\chap07\\practice\\V1_BigData\\nene%s.csv" % count, 'r')
            data = f.read()
            count += 1
        except:
            nene_table.to_csv('V1_BigData\\nene%s.csv' % count, encoding="cp949", mode='w', index=True)
            break
except:
    os.system("mkdir V1_BigData")
    nene_table.to_csv('V1_BigData\\nene.csv', encoding="cp949", mode='w', index=True)
print("End")