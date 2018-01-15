import urllib.request
from bs4 import BeautifulSoup
from pandas import DataFrame
import os
import math
max_page = 5

index = 'index'
result = []
for page_index in range(1, max_page + 1):
    twoso_URL = 'http://2sofood.com/bbs/board.php?bo_table=store&city=&gu=&dong=&page=%s' % str(page_index)
    # print(twoso_URL)
    response = urllib.request.urlopen(twoso_URL)
    soupDate = BeautifulSoup(response.read(),'html.parser')
    # store_trs = soupDate.find_all("div", attrs={'class':'addinfo'})
    # print(store_trs)
    names = soupDate.find_all("p", attrs={"class":"storeName"})
    store_adds = soupDate.find_all("p", attrs={"class":"storeAdd"})
    store_phone = soupDate.find_all("p", attrs={"class":"storeTell"})
    # print(name)
    # print(store_add)
    # print(store_phone)
    store_name = []
    for name in names:
        name = name.get_text(strip=True)
        # name = list(name.strings)
        store_name.append([name])
    # print(store_name)
    store_add = []
    for add in store_adds :
        add = list(add.strings)
        # print(add)
        # if os.istext('대구'):
        # if add[0] == '대':
        store_add.append(add)
    # print(store_add)
    store_tell = []
    for phone in store_phone:
        phone = list(phone.strings)
        store_tell.append(phone)
    # print(store_tell)

    for i in range(len(store_add)):
        result.append(store_name[i]+store_add[i]+store_tell[i])

# print(result)
# print(store_add.count('대구'))
# if result[0][1] == "대구" :
#     eso_table = DataFrame(result, columns=("Name", "Address", "Tell"))
#     eso_table.to_csv("eso1.csv", encoding='cp949', mode='w', index=False)

deagu= []
for i in result:
    if i[1][0] == '대':
        deagu.append(i)
# print(deagu)
# eso_table = DataFrame(result2 , columns=("Name", "Address", "Tell"))
# eso_table.to_csv("eso1.csv", encoding='cp949', mode='w', index=False)
seoul = []
gyeong_buk = []
gyeong_gi = []
busan = []
chung_buk = []
jeon_buk = []
ulsan = []
for i in result:
    if i[1][0] == '서':
        seoul.append(i)
    elif i[1][0] == '경'and i[1][1] == '북':
        gyeong_buk.append(i)
    elif i[1][0] == '경' and i[1][1] == '기':
        gyeong_gi.append(i)
    elif i[1][0] == '부':
        busan.append(i)
    elif i[1][0] == '충' and i[1][1] == '북':
        chung_buk.append(i)
    elif i[1][0] == '전' and i[1][1] == '북':
        jeon_buk.append(i)
    elif i[1][0] == '울' :
        ulsan.append(i)

total = (len(gyeong_gi)+len(gyeong_buk)+len(seoul)+len(busan)+len(chung_buk)+len(jeon_buk)+len(ulsan)+len(deagu))

# print("지역"+"|"+"주소")
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


# result[0]
# print(result[0][0])
print("웹 스콜링을 시작합니다.")
print("지역"+"\t\t"+"|"+"\t"+"지점명"+"\t\t\t\t\t\t"+"|"+"\t"+"주소")
print('-------------------------------------------------------------------------------------')
i=0
while i < 64:
    print((result[i][1][0]+result[i][1][1]),end="\t\t")
    print("| %-20s" % result[i][0],end="\t\t")
    print("| %-26s" % result[i][1])
    i += 1

print("검색된 레코드수:%s"%str(total))


# eso_table = DataFrame(result2 , columns=("Name", "Address", "Tell"))
# eso_table.to_csv("eso2.csv", encoding='cp949', mode='w', index=False)