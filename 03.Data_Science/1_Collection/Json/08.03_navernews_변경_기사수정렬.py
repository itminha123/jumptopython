import urllib.request
import datetime
import json

app_id ="QuStly4CvlpyMUh0H5rj"
app_pw = "leuZfZihj3"

def get_request_url(url):
    req = urllib.request.Request(url)
    req.add_header("X-Naver-Client-Id",app_id)
    req.add_header("X-Naver-Client-Secret",app_pw)
    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            print("[%s] Url Request Success" % datetime.datetime.now())
            return  response.read().decode('utf-8')
    except Exception as e:
        print(e)
        print("[%s] Error for URL: %s"(datetime.datetime.now(),url))
        return None

def getNaverSearchResult(sNode,search_text,page_start,display):
    base = "https://openapi.naver.com/v1/search"
    node = "/%s.json"% sNode

    paramerters = "?query=%s&start=%s&display=%s"%(urllib.parse.quote(search_text),page_start,display)
    url = base + node +paramerters
    retData = get_request_url(url)
    if(retData == None):
        return  None
    else:
        return json.loads(retData)

def getPostData(post,jsonResult):

    title = post["title"]
    description = post["description"]
    org_link = post["originallink"]
    link = post["link"]

    pData = datetime.datetime.strptime(post["pubDate"],"%a, %d %b %Y %H:%M:%S +0900")
    pData = pData.strftime("%Y-%m-%d %H:%M:%S")

    if "&quot;" in post["title"] or post["description"] or post['org_link'] or post["pData"]:
        title = title.replace("&quot;","\"")
        description = description.replace("&quot;","\"")
        org_link = org_link.replace("&quot;","\"")
    if "&lt;" in post["title"] or post["description"] or post['org_link'] or post["pData"]:
        title = title.replace("&lt;","<")
        description =  description.replace("&lt;","<")
        org_link = org_link.replace("&lt;","<")
    if "&gt;" in post["title"] or post["description"] or post['org_link'] or post["pData"]:
        title = title.replace("&gt;",">")
        description = description.replace("&gt;",">")
        org_link = org_link.replace("&gt;",">")
    if "<b>" in post["title"] or post["description"] or post['org_link'] or post["pData"]:
        title = title.replace("<b>"," ")
        description = description.replace("<b>"," ")
        org_link = org_link.replace("<b>"," ")
    if "</b>" in post["title"] or post["description"] or post['org_link'] or post["pData"]:
        title = title.replace("</b>","")
        description = description.replace("</b>","")
        org_link = org_link.replace("</b>","")

    # org_link = org_link.sprit("/")
    # if org_link[2]==org_link[2]:

    jsonResult.append({'title':title, 'description':description, "org_link":org_link, "pData":pData})
    return

def main():
    jsonResult = []

    sNode = "news"
    search_text = '이명박'
    display_count = 100
    jsonSearch = getNaverSearchResult(sNode,search_text,1,display_count)
    index = 1
    while ((jsonSearch != None) and (jsonSearch['display'] != 0) and index < 9):
        for post in jsonSearch["items"]:
            getPostData(post,jsonResult)

        nStart = jsonSearch['start'] + jsonSearch['display']
        jsonSearch = getNaverSearchResult(sNode,search_text,nStart,display_count)
        index = index +1

    with open('%s_naver_%s.json'%(search_text,sNode), 'w', encoding='utf8') as outfile:
        retjson = json.dumps(jsonResult, indent=4, sort_keys=True, ensure_ascii=False)
        outfile.write(retjson)
    print("%s_naver_%s.json SAVED" %(search_text,sNode))

    # result2 = []
    # result3 = set(result2)
    # for i in jsonResult:
    #     result = i["org_link"].sprit("/")
    #     result2.append(result[2])
    # for i in range(len(result3)):
    #     print(result2.count(result3[i]))


if __name__ == '__main__':
    main()


