import urllib.request
import datetime
import json
import time
import threading

g_Radiator = False
g_Gas_Valve = False
g_Balcony_Windows = False
g_Door = False
g_AI_Mode = False

access_key = "UREVmQGGPyZcH9gz8eKshT%2Ffyo6paHADoJ4G2P1LuuJMY%2FqoBjGdMJ2icmwgclLU1cVM8YLzAz4qrpeKmfEKEg%3D%3D"

def get_request_url(url):
    req = urllib.request.Request(url)

    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            print("\n[%s] Url Request Success" % datetime.datetime.now())
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
    if int(time.strftime("%H")+'45') <= int(time.strftime("%H%M")):
        basetime = time.strftime("%H")+'45'
    else:
        basetime = str(int(time.strftime("%H"))-1)+'45'

    nx = "89"
    ny = "91"

    jsondata = getweather(basedate, basetime, nx, ny)
    if (jsondata['response']['header']['resultMsg'] == 'OK'):
        for i in (jsondata['response']['body']['items']['item']):
            jsonresult.append({'baseDate': i['baseDate'],'baseTime': i['baseTime'],'category': i["category"],
                               'fcstDate': i['fcstDate'],'fcstTime': i['fcstTime'],
                               'fcstValue': i['fcstValue'],'nx': i['nx'],'ny': i['ny']})
    with open('%s_%s_날씨정보.json' % (basedate, basetime), 'w', encoding='utf8') as outfile:
        retJson = json.dumps(jsonresult, indent=4, sort_keys=True, ensure_ascii=False)
        outfile.write(retJson)

def print_main_menu():
    print("\n1. 장비상태 확인")
    print("2. 장비제어")
    print("3. 스마트모드")
    print("4. 프로그램 종료")

def check_device(device,name):
    print(name +" 상태: ",end='')
    if(device == True): print("작동")
    else: print("정지")

def check_device_status():
    check_device(g_Radiator,"난방기")
    check_device(g_Gas_Valve,"가스밸브")
    check_device(g_Balcony_Windows,"발코니 윈도우")
    check_device(g_Door,"출입문")

def print_device_menu():
    print("상태 변경할 기기를 선택하세요")
    print("1. 난방기")
    print("2. 가스밸브")
    print("3. 발코니(베란다)창")
    print("4. 출입문")

def control_device():
    global g_Radiator, g_Gas_Valve, g_Balcony_Windows, g_Door
    check_device_status()
    print_device_menu()
    menu_num = int(input("번호를 입력하세요: "))

    if menu_num == 1 :
        g_Radiator = not g_Radiator
    elif menu_num == 2 :
        g_Gas_Valve = not g_Radiator
    elif menu_num == 3 :
        g_Balcony_Windows = not g_Balcony_Windows
    elif menu_num == 4 :
        g_Door = not g_Door

def get_rain_weather(file_name):
    global g_Balcony_Windows
    with open(file_name, encoding='UTF8') as json_file:
        json_object = json.load(json_file)
        json_string = json.dumps(json_object)
        result = json.loads(json_string)
    for i in result:
        if "PTY" in i["category"]:
            if i["fcstValue"] != 0:
                print("비가 옵니다.")
                if g_Balcony_Windows == True:
                    g_Balcony_Windows = False
                    print("창문을 닫겠습니다.")
                else: print("창문이 닫겨있습니다.")
                break

def update_scheduler():
    global g_Balcony_Windows
    while True:
        if g_AI_Mode == True:
            if time.strftime("%S") == '30':
                main()
                get_rain_weather('%s_%s_날씨정보.json'% (time.strftime("%Y%m%d"),time.strftime("%H%M")))
                time.sleep(1)
                print_main_menu()
                print("메뉴를 선택하세요: ")
        else:
            continue

t = threading.Thread(target=update_scheduler)
t.daemon = True
t.start()

def smart_mode():
    global  g_AI_Mode
    print("1. 인공지능 모드 조회")
    print("2. 인공지능 모드 상태 변경")
    print("3. 실시간 기상정보 Update")
    print("4. 비오는날 강수예보 시물레이션")
    menu_num = int(input("메뉴를 선택하세요: "))

    if menu_num == 1:
        print("현재 인공지능 모드: ", end='')
        if g_AI_Mode == True:print("작동")
        else: print("중지")
    if menu_num == 2:
        g_AI_Mode = not g_AI_Mode
        print("현재 인공지능 모드: ", end='')
        if g_AI_Mode == True:print("작동")
        else: print("중지")
    elif menu_num == 3:
        main()
    elif menu_num == 4:
        get_rain_weather("20180129_1424_날씨정보2.json")

while True:
    print_main_menu()
    menu_num = int(input("메뉴를 선택하세요: "))

    if(menu_num == 1):
        check_device_status()
    elif(menu_num == 2):
        control_device()
    elif(menu_num == 3):
        smart_mode()
    elif(menu_num == 4):
        break



