import urllib.request
import datetime
import json
import time
import threading
import fine_dust

g_AI_speaker = False
g_Radiator = False
g_Gas_Valve = False
g_Balcony_Windows = False
g_Door = False
g_AI_Mode = False
g_humidifier = False
g_dehumidifier = False
g_air_cleaner = False

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

def get_weather(base_date,base_time,nx,ny):
    end_point = "http://newsky2.kma.go.kr/service/SecndSrtpdFrcstInfoService2/ForecastTimeData"

    parameters = "?_type=json&serviceKey=" + access_key
    parameters += "&base_date=" + base_date
    parameters += "&base_time=" + base_time
    parameters += "&nx=" + nx
    parameters += "&ny=" + ny
    parameters += "&numOfRows=100"

    url = end_point + parameters
    retdata = get_request_url(url)
    if (retdata == None) :
        return None
    else:
        return json.loads(retdata)

def weather_main():
    jsonresult = []
    basedate = time.strftime("%Y%m%d")
    if int(time.strftime("%H")+'45') <= int(time.strftime("%H%M")):
        basetime = time.strftime("%H")+'45'
    else:
        basetime = ("{0:0>2}{1}".format(str(int(time.strftime("%H")) - 1), "45"))
    nx = '89'
    ny = '91'

    jsondata = get_weather(basedate,basetime,nx,ny)
    if (jsondata['response']['header']['resultMsg'] == 'OK'):
        for i in (jsondata['response']['body']['items']['item']):
            jsonresult.append({"baseDate": i["baseDate"],'baseTime': i['baseTime'],'category': i["category"],
                               'fcstDate': i['fcstDate'],'fcstTime': i['fcstTime'],'fcstValue': i['fcstValue'],
                               'nx': i['nx'],'ny': i['ny']})
    with open('날씨정보.json','w',encoding='utf8') as outfile:
        retjson = json.dumps(jsonresult, indent=4, sort_keys=True, ensure_ascii=False)
        outfile.write(retjson)

def get_finedust():
    end_point="http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty"

    parameters = "?_returnType=json&serviceKey="+access_key
    parameters+="&sidoName="+urllib.request.quote('대구')
    parameters+="&numOfRows=100"
    parameters+="&ver=1.3"

    url=end_point+parameters

    retData = get_request_url(url)
    # print(retData)
    json.loads(retData)
    if(retData == None):
        return None
    else:
        return json.loads(retData)

def finedust_main():
    jsonresult=[]
    jsondata = get_finedust()
    for i in jsondata["list"]:
        jsonresult.append({"datatime":i["dataTime"],"pm25Value":i["pm25Value"],
                           "pm25Grade":i["pm25Grade"],"stationName":i["stationName"]})

    with open('미세먼지.json','w',encoding='utf8') as outfile:
        retJson = json.dumps(jsonresult,indent=4,sort_keys=True,ensure_ascii=False)
        outfile.write(retJson)

def get_simulation_finedust(station_name):
    with open("미세먼지.json", encoding='UTF8') as jsonfile:
        json_object = json.load(jsonfile)
        json_stings = json.dumps(json_object)
        result = json.loads(json_stings)
    for i in result:
        if i["stationName"] == station_name:
            if i["pm25Grade"] == 3 or  i["pm25Grade"] == 4 :
                print("미세먼지 농도가 좋지 안습니다.")
                print("공기청정기를 켜겠습니다.")
                if g_air_cleaner == False:
                    g_air_cleaner = True
                else: print("공기 청정기가 켜져있습니다.")

def print_main_menu():
    print("\n<< 스마트 홈네트워크 ver0.1 >>")
    print("1. 장비상태 확인")
    print("2. 장비제어")
    print("3. 스마트모드")
    print("4. 시뮬레이션모드")
    print("5. 프로그램 종료")

def check_device(device,name,state1,state2):
    print(name +" 상태: ",end='')
    if(device == True): print(state1)
    else: print(state2)

def check_device_status():
    print()
    check_device(g_Radiator, "난방기", '작동', '정지')
    check_device(g_Gas_Valve, "가스밸브", '열림', '닫힘')
    check_device(g_Balcony_Windows, "발코니 윈도우", '열림', '닫힘')
    check_device(g_Door, "출입문", '열림', '닫힘')
    check_device(g_humidifier, '가습기', '작동', '정지')
    check_device(g_dehumidifier, '제습기', '작동', '정지')
    check_device(g_air_cleaner, '공기청정기', '작동', '정지')

def print_device_menu():
    print("\n상태 변경할 기기를 선택하세요")
    print("1. 난방기")
    print("2. 가스밸브")
    print("3. 발코니(베란다)창")
    print("4. 출입문")
    print("5. 가습기")
    print("6. 제습기")
    print("7. 공기청정기")

def control_device():
    global g_Radiator, g_Gas_Valve, g_Balcony_Windows, g_Door, g_humidifier, g_dehumidifier,g_air_cleaner
    check_device_status()
    print_device_menu()
    menu_num = input("번호를 입력하세요: ")

    if menu_num == '1':
        g_Radiator = not g_Radiator
        check_device(g_Radiator, '난방기', '작동', '정지')
    elif menu_num == '2':
        g_Gas_Valve = not g_Radiator
        check_device(g_Gas_Valve, "가스밸브",'열림','닫힘')
    elif menu_num == '3' :
        g_Balcony_Windows = not g_Balcony_Windows
        check_device(g_Balcony_Windows, "발코니 윈도우",'열림','닫힘')
    elif menu_num == '4' :
        g_Door = not g_Door
        check_device(g_Door, "출입문",'열림','닫힘')
    elif menu_num == '5' :
        g_humidifier = not g_humidifier
        check_device(g_humidifier,'가습기','작동','정지')
    elif menu_num == '6' :
        g_dehumidifier = not g_dehumidifier
        check_device(g_dehumidifier,'제습기','작동','정지')
    elif menu_num == '7' :
        g_air_cleaner = not g_air_cleaner
        check_device(g_air_cleaner, '공기청정기', '작동', '정지')

def get_simulation_rain(file_name):
    global g_Balcony_Windows, g_humidifier, g_dehumidifier
    with open(file_name, encoding='UTF8') as json_file:
        json_object = json.load(json_file)
        json_string = json.dumps(json_object)
        result = json.loads(json_string)
    for i in result:
        if "PTY" == i["category"]:
            if i["fcstValue"] != 0:
                print("비가 옵니다.")
                if g_Balcony_Windows == True:
                    g_Balcony_Windows = False
                    print("창문을 닫겠습니다.")
                else: print("창문이 닫겨있습니다.")
                break

def get_simulation_humidity(filename):
    global g_humidifier, g_dehumidifier
    with open(filename, encoding='UTF8') as json_file:
        json_object = json.load(json_file)
        json_string = json.dumps(json_object)
        result = json.loads(json_string)
    for i in result:
        if 'REH' == i['category']:
            if int(i["fcstValue"]) < 40:
                print("건조 합니다.")
                if g_humidifier == False:
                    g_humidifier = True
                    print("가습기를 켭니다.")
                    if g_dehumidifier == True: g_dehumidifier = False
                    break
                else:
                    print("가습기가 켜져 있습니다.")
                    break
            elif int(i['fcstValue']) > 60:
                print("습도가 높습니다.")
                if g_dehumidifier == False:
                    g_dehumidifier = True
                    print("제습기를 켭니다.")
                    if g_humidifier == True: g_humidifier = False
                    break
                else:
                    print('제습기가 켜져 있습니다.')
                    break
            else:
                if g_dehumidifier == True or g_humidifier == True:
                    g_dehumidifier = False
                    g_humidifier = False
                    print("날씨가 상쾌 합니다.")
                    print("제습기 , 가습기를 끄겠습니다.")
                    break

def update_scheduler():
    global g_AI_speaker
    while True:
        if g_AI_Mode == True:
            if time.strftime("%M%S") == '4530':
                weather_main()
                get_simulation_rain('날씨정보.json')
                get_simulation_humidity('날씨정보.json')
                print_main_menu()
                print("메뉴를 선택하세요: ")
                time.sleep(1)
            elif time.strftime("%H%M%S") == '122800':
                weather_main()
                with open('날씨정보.json', encoding='UTF8') as json_file:
                    json_object = json.load(json_file)
                    json_string = json.dumps(json_object)
                    result = json.loads(json_string)
                rain_list = []
                temperature_list = []
                for i in result:
                    if "PTY" == i["category"]:
                        rain_list.append(i)
                    elif "T1H" == i["category"]:
                        temperature_list.append(i)


                if rain_list[0]["fcstValue"] != 0:
                    g_AI_speaker = True
                    print("현재 비가 와요~ \n우산 가져 가세요")
                    g_AI_speaker = False
                    print_main_menu()
                    print("메뉴를 선택하세요: ")
                elif rain_list[0]["fcstValue"] == 0 and rain_list[-1]["fcstValue"] != 0 :
                    g_AI_speaker = True
                    print("비가 올 예정이에요~ \n우산 가져 가세요")
                    g_AI_speaker = False
                    print_main_menu()
                    print("메뉴를 선택하세요: ")
        else:
            continue

t = threading.Thread(target=update_scheduler)
t.daemon = True
t.start()

def total_simulation(file_name,category,value):
    jsonresult = [{'baseDate': time.strftime("%Y%m%d"), 'baseTime': time.strftime("%H%M"),'category': category,
                   'fcstDate': time.strftime("%Y%m%d"),'fcstTime': time.strftime("%H%M"),'fcstValue': value,
                   'nx': "89" ,'ny': "91"}]
    with open(file_name , 'w', encoding='utf8') as outfile:
        retJson = json.dumps(jsonresult, indent=4, sort_keys=True, ensure_ascii=False)
        outfile.write(retJson)

def smart_mode():
    global  g_AI_Mode
    print("\n1. 인공지능 모드 조회")
    print("2. 인공지능 모드 상태 변경")
    print("3. 실시간 기상정보 Update")
    print("4. 실시간 미세먼지 정보 update")
    print("0. 되돌아가기")
    menu_num = (input("메뉴를 선택하세요: "))

    if menu_num == '1':
        print("현재 인공지능 모드: ", end='')
        if g_AI_Mode == True:print("작동")
        else: print("중지")
    if menu_num == '2':
        g_AI_Mode = not g_AI_Mode
        print("현재 인공지능 모드: ", end='')
        if g_AI_Mode == True:print("작동")
        else: print("중지")
        if g_AI_Mode == True:
            weather_main()
            get_simulation_rain('날씨정보.json')
            get_simulation_humidity('날씨정보.json')
    elif menu_num == '3':
        weather_main()
        get_simulation_rain('날씨정보.json')
        get_simulation_humidity('날씨정보.json')
    elif menu_num == '4':
        finedust_main()
        get_simulation_finedust("신암동")
    elif menu_num == '0':
        pass
    else:print("단디 입력하이소!")

def simulation_mode():
    print("\n1. 비오는날 시뮬레이션")
    print("2. 습한날 시뮬레이션")
    print("3. 건조한날 시뮬레이션")
    print("4. 상쾌한날 시뮬레이션")
    menu_num = input("입력: ")
    if menu_num == '1':
        total_simulation('rain_시뮬레이션.json','PTY',1)
        get_simulation_rain('rain_시뮬레이션.json')
    elif menu_num == '2':
        total_simulation("humidity_시뮬레이션.json",'REH',75)
        get_simulation_humidity("humidity_시뮬레이션.json")
    elif menu_num =='3':
        total_simulation("humidity_시뮬레이션.json",'REH',26)
        get_simulation_humidity("humidity_시뮬레이션.json")
    elif menu_num == '4':
        total_simulation("humidity_시뮬레이션.json",'REH', 51)
        get_simulation_humidity("humidity_시뮬레이션.json")

while True:
    print_main_menu()
    menu_num = input("메뉴를 선택하세요: ")

    if(menu_num == '1'):
        check_device_status()
    elif(menu_num == '2'):
        control_device()
    elif(menu_num == '3'):
        smart_mode()
    elif(menu_num== '4'):
        simulation_mode()
    elif(menu_num == '5'):
        break
    else: print("단디 입력해라!")



