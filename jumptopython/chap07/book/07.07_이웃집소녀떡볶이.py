import urllib.request
from bs4 import BeautifulSoup
from pandas import DataFrame
import os
max_page = 5

index = 'index'
result = []
for page_index in range(1, max_page + 1):
    twoso_URL = 'http://2sofood.com/bbs/board.php?bo_table=store&city=&gu=&dong=&page=%s' % str(page_index)
    # print(twoso_URL)
    response = urllib.request.urlopen(twoso_URL)
    soupDate = BeautifulSoup(response.read(),'html.parser')
    names = soupDate.find_all("p", attrs={"class":"storeName"})
    store_adds = soupDate.find_all("p", attrs={"class":"storeAdd"})
    store_phone = soupDate.find_all("p", attrs={"class":"storeTell"})
    # print(name)
    # print(store_add)
    # print(store_phone)
    store_name = []
    for name in names:
        name = name.get_text(strip=True)
        store_name.append([name])
    # print(store_name)
    store_add = []
    for add in store_adds :
        add = list(add.strings)
        # print(add)
        store_add.append(add)
    # print(store_add)
    store_tell = []
    for phone in store_phone:
        phone = list(phone.strings)
        store_tell.append(phone)
    # print(store_tell)

    for i in range(len(store_add)):
        result.append(store_name[i]+store_add[i]+store_tell[i])

eso_table = DataFrame(result , columns=("Name", "Address", "Tell"))
eso_table.to_csv("eso1.csv", encoding='cp949', mode='w', index=False)

deagu= []
seoul = []
gyeong_buk = []
gyeong_gi = []
busan = []
chung_buk = []
jeon_buk = []
ulsan = []
for i in result:
    if i[1][0] + i[1][1]== '대구':
        deagu.append(i)
for i in result:
    if '서울' in i[1]:
        seoul.append(i)
    elif '경북'in i[1]:
        gyeong_buk.append(i)
    elif '경기' in i[1]:
        gyeong_gi.append(i)
    elif '부산' in i[1]:
        busan.append(i)
    elif '충북' in i[1]:
        chung_buk.append(i)
    elif '전북' in i[1]:
        jeon_buk.append(i)
    elif '울산' in i[1]:
        ulsan.append(i)

total = (len(gyeong_gi)+len(gyeong_buk)+len(seoul)+len(busan)+len(chung_buk)+len(jeon_buk)+len(ulsan)+len(deagu))

# print("대구",len(deagu),(len(deagu) * 100)/total)
# print("경기",len(gyeong_gi),(len(gyeong_gi) * 100)/total)
# print("경북",len(gyeong_buk),(len(gyeong_buk) * 100)/total)
# print("서울",len(seoul),(len(seoul) * 100)/total)
# print("부산",len(busan),(len(busan) * 100)/total)
# print("충북",len(chung_buk),(len(chung_buk) * 100)/total)
# print("전북",len(jeon_buk),(len(jeon_buk) * 100)/total)
# print("울산",len(ulsan),(len(ulsan) * 100)/total)
# print("총합",total)
# deagu_percent=((len(deagu) * 100)/total)
# print(deagu_percent)

# b = [i[1][0]+i[1][1] for i in result ]
# print(b)

print("웹 스콜링을 시작합니다.")
print("지역"+"\t\t"+"|"+"\t"+"지점명"+"\t\t\t\t\t\t"+"|"+"\t"+"주소")
print('-'*110)
i=0
while i < total:
    print((result[i][1][0]+result[i][1][1]),end="\t\t")
    print("| %-20s" % result[i][0],end="\t\t")
    print("| %s" % result[i][1])
    i += 1

print("검색된 레코드수:%s" %str(total))

area = ["서울","경기","충북","경북","대구","부산","울산","전북"]
area_count = [len(seoul),len(gyeong_gi),len(chung_buk),len(gyeong_buk),len(deagu),len(busan),len(ulsan),len(jeon_buk)]
percent = []

final_result = []
for i in range(len(area)):
    percent.append((area_count[i]/total)*100)
    final_result.append([area[i]]+[area_count[i]]+[percent[i]])
    print("%s\t\t%s\t\t%s" % ((area[i],str(area_count[i]),str(percent[i]))))

# print(final_result)
eso_table = DataFrame(final_result , columns=("지역", "지점수", "점유율"))
eso_table.to_csv("eso2.csv", encoding='cp949', mode='w', index=False)