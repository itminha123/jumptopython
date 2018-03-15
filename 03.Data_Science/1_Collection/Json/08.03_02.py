import json

news_domain_all_list = []
domain_info_list = []
num_of_corrupted_data=0

with open("이명박_naver_news.json", encoding="utf-8") as json_data:
    json_data_load = json.load(json_data)
    json_data_string = json.dumps(json_data_load)
    jsonResult = json.loads(json_data_string)
print("데이터 분석을 시작합니다..")
for x in jsonResult:
    try: news_domain_all_list.append(x["org_link"].split('/')[2])
    except:
        num_of_corrupted_data +=1
        print("'org_link'가 없는 기사를 발견했습니다.")

news_domain_unique_list=set(news_domain_all_list)

total_count=0
for one_of_unique in news_domain_unique_list:
    domain_info = [one_of_unique,0]
    for one_of_all in news_domain_all_list:
        if one_of_all == one_of_unique:
            domain_info[1] += 1
    domain_info_list.append(domain_info)
    total_count +=domain_info[1]

sorted_num_of_domain_info = sorted(domain_info_list, key=lambda k: k[1],reverse=True)

print("\n\n<네이버 검색 빅데이터 분석>")
print("검색어: 이명박")
print("전체 도메인 수: "+str(len(sorted_num_of_domain_info)))
print("전체 건수: "+str(total_count))
print("부정확한 데이터수"+str(num_of_corrupted_data))
print("\n- 도메인 별 뉴스 기사 분석")

for info in sorted_num_of_domain_info:
    print(" >> "+info[0]+": "+str(info[1])+"건")
