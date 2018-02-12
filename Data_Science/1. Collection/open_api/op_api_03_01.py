import urllib.request
import datetime
import json
import time

access_key = "UREVmQGGPyZcH9gz8eKshT%2Ffyo6paHADoJ4G2P1LuuJMY%2FqoBjGdMJ2icmwgclLU1cVM8YLzAz4qrpeKmfEKEg%3D%3D"

def get_request_url(url):
    req = urllib.request.Request(url)

    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            print("[%s] Url Request Success" % datetime.datetime.now())
            return response.read().decode('utf-8')
    except Exception as e:
        print(e)
        print("[%s] Error for URL:%s" % (datetime.datetime.now(), url))
        return None

def getweather(base_date,base_time,nx,ny):
    end_point = "http://newsky2.kma.go.kr/service/SecndSrtpdFrcstInfoService2/ForecastTimeData"

    parameters = "?_type=json&serviceKey=" + access_key
    parameters += "&base_date=" + base_date
    parameters += '&base_time=' + base_time
    parameters += '&nx=' + nx
    parameters += '&ny=' + ny

    url = end_point + parameters
    retData = get_request_url(url)
    if (retData == None):
        return None
    else:
        return json.loads(retData)

def main():
    jsonresult = []
    basedate = time.strftime("%Y%m%d")
    basetime = time.strftime("%H%M")
    nx = "89"
    ny = "91"

    jsondata = getweather(basedate, basetime, nx, ny)
    # for i in range(1,25):
    #     if basetime == "{0:0>2}{1}".format(str(i),'45'):
    if (jsondata['response']['header']['resultMsg'] == 'OK'):
        for i in (jsondata['response']['body']['items']['item']):
            jsonresult.append({'baseDate': i['baseDate'],
                               'baseTime': i['baseTime'],
                               'category': i["category"],
                               'fcstDate': i['fcstDate'],
                               'fcstTime': i['fcstTime'],
                               'fcstValue': i['fcstValue'],
                               'nx': i['nx'],
                               'ny': i['ny']
                               })
    print("%s_%s_날씨정보"%(basedate, basetime))
    with open('%s_%s_날씨정보2.json' % (basedate, basetime), 'w', encoding='utf8') as outfile:
        retJson = json.dumps(jsonresult, indent=4, sort_keys=True, ensure_ascii=False)
        outfile.write(retJson)

if __name__ == '__main__':
    main()
