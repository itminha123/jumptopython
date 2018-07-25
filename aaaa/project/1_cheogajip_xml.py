import urllib.request
from bs4 import BeautifulSoup
from pandas import DataFrame

max_page = 104
result = []
store_location = []
store_name = []
store_address = []
phone_number = []
print("웹 크롤링을 시작합니다.")
for page_idx in range(1, max_page+1):
    Cheogajip_URL = 'http://www.cheogajip.co.kr/bbs/board.php?bo_table=store&page=%s'%str(page_idx)
    response = urllib.request.urlopen(Cheogajip_URL)
    soupData = BeautifulSoup(response, 'html.parser')
    store_trs = soupData.find_all('td',)         # html td 정보를 가져옴(매장정보가 있어서)
    print(page_idx)

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

area_count =[]

area = ["서울특별시", "경기도", "인천광역시", "강원도", "충청북도", "충청남도", "대전광역시", "세종특별자치시",
        "광주광역시", "전라북도", "전라남도", "경상북도", "경상남도", "대구광역시", "부산광역시", "울산광역시",
        "제주특별자치도"]

cnt = 0;
count = 0;
for i in area:                                  # 전국 매장 수 구하기
    for j in result:
        if i in j:
            cnt += 1
            count += 1
    area_cnt = [i, cnt]
    area_count.append(area_cnt)
    cnt = 0

for i in area_count:
    print(i[0],"매장수: %d" %i[1])

ratio = []                                      # 지역매장 점유율 구하기
for i in area_count:
    ratio.append(i[1]/len(result)*100)

import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)                    # 한글 지원

plt.pie(ratio, labels=area, shadow=True, startangle=90, autopct='%1.1f%%')  # 원형차트 만들기
plt.show()