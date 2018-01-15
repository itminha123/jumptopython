import urllib.request
from bs4 import BeautifulSoup
from pandas import DataFrame
import os
max_page = 5

index = 'index'
store_name = []
store_add = []
store_tell = []
result = []
for page_index in range(1, max_page + 1):
    twoso_URL = 'http://2sofood.com/bbs/board.php?bo_table=store&city=&gu=&dong=&page=%s' % str(page_index)
    # print(twoso_URL)
    response = urllib.request.urlopen(twoso_URL)
    soupDate = BeautifulSoup(response.read(),'html.parser')
    store_all = soupDate.find_all('p')
# print(store_all)
    for i in range(0, len(store_all)- 1 , 3):
        store_name.append(store_all[i].get_text(strip=True))
        store_add.append(store_all[i+1].text)
        store_tell.append((store_all[i+2].text))
print(store_name)
print(store_add)
print(store_tell)


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
    if '서울' in i[1]:
        seoul.append(i)
    elif '경북' in i[1]:
        gyeong_buk.append(i)
    elif '경기' in i[1]:
        gyeong_gi.append(i)
    elif '부산' in i[1]:
        busan.append(i)
    elif '충북' and i[1][1] == '북':
        chung_buk.append(i)
    elif i[1][0] == '전' and i[1][1] == '북':
        jeon_buk.append(i)
    elif i[1][0] == '울' :
        ulsan.append(i)
print(seoul)
total = (len(gyeong_gi)+len(gyeong_buk)+len(seoul)+len(busan)+len(chung_buk)+len(jeon_buk)+len(ulsan)+len(deagu))

