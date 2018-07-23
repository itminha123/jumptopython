import urllib.request
from  bs4 import  BeautifulSoup
from pandas import  DataFrame


max_page = 103
result = []
index = "index"
for page_idx in range(1,max_page+1):
    Cheogajip_URL = 'http://www.cheogajip.co.kr/bbs/board.php?bo_table=store&page=%s'%str(page_idx)
    # print(Cheogajip_URL)
    response = urllib.request.urlopen(Cheogajip_URL)
    # print(response)
    soupData = BeautifulSoup(response,'html.parser')
    # print(soupData)
    store_trs = soupData.find_all('td',attrs={'class':'td_date','class':'td_subject',"class":"td_date"})
    print(store_trs)
    cnt = 0
    if(store_trs):
        for i in store_trs:
            tr_tag = list(i.strings)

            cnt += 3


            # print(store_name)
            # store_address = list(store_trs.strings[i+1])
            # print(store_address)
    #             phone_number = tr_tag[5]
    #             result.append([store_name]+[store_address]+[phone_number])
    #             result.append(store_name)
#
# cheogajip_table = DataFrame(result, columns=('store_name','store_address','phone_number'))
# cheogajip_table.to_csv("cheogajip.csv", encoding="cp949", mode='w', index= True)
#
# print("end")