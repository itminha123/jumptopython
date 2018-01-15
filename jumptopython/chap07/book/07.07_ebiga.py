import  urllib.request
from bs4 import BeautifulSoup
from pandas import  DataFrame

max_page = 10
result = []
index = "index"

for page_index in range(1,max_page+1):
    ebiga_URL = "http://www.ebiga.co.kr/home/bbs/board.php?bo_table=store&page=%s" %str(page_index)
    response = urllib.request.urlopen(ebiga_URL)
    # print(response)
    soupdata = BeautifulSoup(response.read(),'html.parser')
    # print(soupdata)
    store_trs = soupdata.find_all('')