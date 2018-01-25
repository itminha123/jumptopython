import json
from pprint import pprint

with open("jtbcnews_facebook_2018-01-24_2018-01-25.json", encoding='UTF8') as json_file:
    json_object = json.load(json_file)
    json_string = json.dumps(json_object)
    result = json.loads(json_string)

# pprint(result["data"])
# result
final_result = []
for i in result['data']:
    if "name" in i :
        final_result.append([i["name"]]+[i["link"]]+[i["shares"]])
    # i["shares"]["count"]=int(i["shares"]["count"])
# print(final_result)
    # final_result.append()
    #
    # sorted(i["shares"]["count"])
    # print(i)
    # if "shares" in i :
    #     print(i["comments"]["shares"])
# (result["data"]["shares"]["count"]) = int(result["data"]["shares"]["count"])
final_result = sorted( final_result , key=lambda i : i[2]["count"], reverse=True)
# print(final_result)

for i in final_result:
    print(i)
    # print(i[0],i[1])

