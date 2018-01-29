import time
import datetime
import json


# yyyymm = "{0}{1:0>2}".format(time.strftime("%Y",time.localtime(time.time())),time.strftime("%m",time.localtime(time.time())))
# yyyymm = time.strftime("%Y%m%d",time.localtime(time.time()))
# print(yyyymm)

baseTime = time.strftime("%H%M",time.localtime(time.time()))
# print(baseTime)

# tt= str(int(time.strftime("%H"))-1)+'45'
# print(tt)
# for i in range(0,24):
#     print("{0:0>2}{1}".format(str(i),"45"))

# while True:
#     print(baseTime)
    # print('aa')
# i=0
# while True:
    # if 0 < i < 24 :
    #     print('pp')
    # datetime.datetime.now()
    # if baseTime == "{0:0>2}{1}".format(str('3'),"37"):
        # i += 1
        # print('cc')
# if int(time.strftime("%H")+'45') <= int(time.strftime("%H%M")):
#     print(time.strftime("%H")+'45')
# else:
#     print(str(int(time.strftime("%H"))-1)+'45')


{'baseDate': 20180129, 'baseTime': 1430, 'category': 'LGT', 'fcstDate': 20180129, 'fcstTime': 1500, 'fcstValue': 0, 'nx': 89, 'ny': 91}
{'baseDate': 20180129, 'baseTime': 1430, 'category': 'LGT', 'fcstDate': 20180129, 'fcstTime': 1600, 'fcstValue': 0, 'nx': 89, 'ny': 91}
{'baseDate': 20180129, 'baseTime': 1430, 'category': 'LGT', 'fcstDate': 20180129, 'fcstTime': 1700, 'fcstValue': 0, 'nx': 89, 'ny': 91}
{'baseDate': 20180129, 'baseTime': 1430, 'category': 'LGT', 'fcstDate': 20180129, 'fcstTime': 1800, 'fcstValue': 0, 'nx': 89, 'ny': 91}
{'baseDate': 20180129, 'baseTime': 1430, 'category': 'PTY', 'fcstDate': 20180129, 'fcstTime': 1500, 'fcstValue': 1, 'nx': 89, 'ny': 91}
{'baseDate': 20180129, 'baseTime': 1430, 'category': 'PTY', 'fcstDate': 20180129, 'fcstTime': 1600, 'fcstValue': 1, 'nx': 89, 'ny': 91}
{'baseDate': 20180129, 'baseTime': 1430, 'category': 'PTY', 'fcstDate': 20180129, 'fcstTime': 1700, 'fcstValue': 1, 'nx': 89, 'ny': 91}
{'baseDate': 20180129, 'baseTime': 1430, 'category': 'PTY', 'fcstDate': 20180129, 'fcstTime': 1800, 'fcstValue': 1, 'nx': 89, 'ny': 91}
{'baseDate': 20180129, 'baseTime': 1430, 'category': 'RN1', 'fcstDate': 20180129, 'fcstTime': 1500, 'fcstValue': 0, 'nx': 89, 'ny': 91}
{'baseDate': 20180129, 'baseTime': 1430, 'category': 'RN1', 'fcstDate': 20180129, 'fcstTime': 1600, 'fcstValue': 0, 'nx': 89, 'ny': 91}

# def get_rain_weather():
#     with open("20180129_1424_날씨정보2.json", encoding='UTF8') as json_file:
#         json_object = json.load(json_file)
#         json_string = json.dumps(json_object)
#         result = json.loads(json_string)
#     PYT_list =[]
#     for i in result:
#         if 'PTY' in i['category']:
#             if i["fcstValue"] != 0 :
#                 print("aa")
#
#
#
#
#
#
# get_rain_weather()


# while True:
#     if time.strftime("%S") == '20':
#         print("ee")
#         time.sleep(1)

print(time.strftime("%M%S"))
