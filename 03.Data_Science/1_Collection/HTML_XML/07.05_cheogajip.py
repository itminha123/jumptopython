import urllib.request
from bs4 import BeautifulSoup
from pandas import  DataFrame


max_page = 103
result = []
index = "index"
store_location = []
store_name = []
store_address = []
phone_number = []

for page_idx in range(1,max_page+1):
    Cheogajip_URL = 'http://www.cheogajip.co.kr/bbs/board.php?bo_table=store&page=%s'%str(page_idx)
    # print(Cheogajip_URL)
    response = urllib.request.urlopen(Cheogajip_URL)
    # print(response)
    soupData = BeautifulSoup(response,'html.parser')
    # print(soupData)
    store_trs = soupData.find_all('td',)
    # store_address = soupData.find_all('td', attrs={'class': 'td_subject'})
    # phone_number = soupData.find_all('td', attrs={'class': 'td_date'})
    print(store_trs)
    cnt = 0
    for i in store_trs:
        tr_tag = list(i.strings)
        # print(tr_tag)
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
print(len(result))
#
# cheogajip_table = DataFrame(result, columns=('store_location','store_name','store_address','phone_number'))
# cheogajip_table.to_csv("cheogajip.csv", encoding="cp949", mode='w', index= True)
#
# print("end")