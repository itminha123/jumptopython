import json

with open("201612_해외방문객정보_.json", encoding='UTF8') as json_file:
    json_object = json.load(json_file)
    json_string = json.dumps(json_object)
    result = json.loads(json_string)

jsonresult = sorted(result, key= lambda i : i["visit_cnt"], reverse=True)

with open('201612_해외방문객_Top10.json' , 'w', encoding='utf8') as outfile:
    retJson = json.dumps(jsonresult[:10], indent=4, sort_keys=True, ensure_ascii=False)
    outfile.write(retJson)