import urllib.request
from bs4 import BeautifulSoup
from pandas import DataFrame

max_page = 103
result = []
store_location = []
store_name = []
store_address = []
phone_number = []
print("웹 크롤링을 시작합니다.")
for page_idx in range(1,max_page+1):
    Cheogajip_URL = 'http://www.cheogajip.co.kr/bbs/board.php?bo_table=store&page=%s'%str(page_idx)
    response = urllib.request.urlopen(Cheogajip_URL)
    soupData = BeautifulSoup(response, 'html.parser')
    store_trs = soupData.find_all('td',)         # html td 정보를 가져옴(매장정보가 있어서)

    cnt = 0
    for i in store_trs:                          # 매장 정보를 지역명 지점명 주소 전화번호
        tr_tag = list(i.strings)                 # 로 구분하여 저장한다.
        if (cnt % 4) == 0 :
            store_location.append(tr_tag)
        elif (cnt % 4) == 1 :
            store_name.append(tr_tag)
        elif (cnt % 4) == 2 :
            store_address.append(tr_tag)
        elif (cnt % 4) == 3 :
            phone_number.append(tr_tag)
        cnt += 1

for j in range(len(store_name)):
    result.append(store_location[j] + store_name[j] + store_address[j] + phone_number[j])

print(result)
print("전국 처갓집 치킨 매장수:", len(result))

cheogajip_table = DataFrame(result, columns=('store_location', 'store_name', 'store_address', 'phone_number'))
cheogajip_table.to_csv("cheogajip.csv", encoding="cp949", mode='w', index= True)

print("end")