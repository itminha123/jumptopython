import os
import sys
import urllib.request
import datetime
import time
import json

import matplotlib.pyplot as plt
import matplotlib
from  matplotlib import font_manager, rc

access_key = ""

def get_request_url(url):
    req = urllib.request.Request(url)
    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            print("[%s] Url Request Success" %datetime.datetime.now())
            return response.read().decode('utf-8')
    except Exception as e:
        print(e)
        print("[%s] Error for URL: %s" %(datetime.datetime.now(), url))
        return None

# [CODE 1]
def getNatVisitor (yyyymm, nat_cd, ed_cd):
    end_point = "http://openapi.tour.go.kr/openapi/service/EdrcntTourismStatsService/getEdrcntTourismStatsList"

    parameters  = "?_type=json&serviceKey=" + access_key
    parameters += "&YM=" + yyyymm
    parameters += "&NAT_CD=" + nat_cd
    parameters += "&ED_CD=" + ed_cd

    url = end_point + parameters

    retData = get_request_url(url)

    if retData == None :
        return None
    else:
        return json.loads(retData)

    def main():
        json_result = []
        # 중국: 112 / 일본: 130 / 미국: 275
        national_code = "112"
        ed_cd = "E"

        nStart_year = 2011
        nEnd_year = 2017

        for year in range(nStart_year, nEnd_year):
            for month in range(1, 13):
                yyyymm = "{0}{1:0>2}".format(str(year),str(month))
                jsonData = getNatVisitor(yyyymm, national_code, ed_cd)

                if (jsonData['response']['header']['resultMsg']=='OK'):
                    krName = jsonData