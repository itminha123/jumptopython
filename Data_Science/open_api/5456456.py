import urllib.request
import datetime
import json
import  xml.etree.ElementTree as ET
from  pandas import  DataFrame
from bs4 import BeautifulSoup

access_key="UREVmQGGPyZcH9gz8eKshT%2Ffyo6paHADoJ4G2P1LuuJMY%2FqoBjGdMJ2icmwgclLU1cVM8YLzAz4qrpeKmfEKEg%3D%3D"


def get_request_url(url):
    req = urllib.request.Request(url)

    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            print("[%s] Url Request Success"%datetime.datetime.now())
            return response.read().decode('utf-8')
    except Exception as e:
        print(e)
        print("[%s] Error for URL:%s"%(datetime.datetime.now(),url))
        return None

def get_finedust():
    end_point="http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty"

    parameters = "?_returnType=json&serviceKey="+access_key
    parameters+="&sidoName="+urllib.request.quote('대구')
    parameters+="&numOfRows=100"
    parameters+="&ver=1.3"

    url=end_point+parameters

    retData = get_request_url(url)
    print(retData)
    json.loads(retData)
    if(retData == None):
        return None
    else:
        return json.loads(retData)

def finedust_main():
    # jsonresult=[]
    jsondata = get_finedust()
    # for i in jsondata["list"]:
    #     jsonresult.append({"datatime":i["dataTime"],"pm25Value":i["pm25Value"],
    #                        "pm25Grade":i["pm25Grade"],"stationName":i["stationName"]})

    with open('미세2.json','w',encoding='utf8') as outfile:
        retJson = json.dumps(jsondata,indent=4,sort_keys=True,ensure_ascii=False)
        outfile.write(retJson)

def get_car():
    end_point= 'http://car.daegu.go.kr/openapi-data/service/rest/data2/dgincident'

    parameters = "?serviceKey=" + access_key
    parameters += "&numOfRows=1"
    # parameters += "&pageNo=1"

    url = end_point + parameters
    retData = get_request_url(url)

    soup = BeautifulSoup(retData, "html.parser")
    print(soup)
#
get_car()
# if __name__ == '__main__':
    # finedust_main()
#

