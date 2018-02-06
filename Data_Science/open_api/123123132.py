import time
import datetime
import json


# yyyymm = "{0}{1:0>2}".format(time.strftime("%Y",time.localtime(time.time())),time.strftime("%m",time.localtime(time.time())))
# yyyymm = time.strftime("%Y%m%d",time.localtime(time.time()))
# print(yyyymm)

# baseTime = time.strftime("%H%M",time.localtime(time.time()))
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
#
#
# while True:
#     if time.strftime("%S") == '20':
#         print("ee")
#         time.sleep(1)
#
# print(time.strftime("%M%S"))
#
# if int(time.strftime("%H") + '45') <= int(time.strftime("%H%M")):
#     basetime = ("{0:0>2}{1}".format(time.strftime("%H"), "45"))
#     basetime = time.strftime("%H")+'45'
#     print(basetime)
#     print(time.strftime("%H")+'45')
# else:
#     basetime = ("{0:0>2}{1}".format(str(int(time.strftime("%H")) - 1), "45"))
#     print(basetime)
#
# print()
# print("{0:0>2}{1}".format(time.strftime("%H"),"45"))
# print(time.strftime("%H")+'45')
#
# count = 0
# zero = False
# while True:
#     if count != 0 and  zero == False:
#         print("0이 아니야")
#         zero = True
#     count += 1
#
#
# def sum(num):
#     if num == 10:
#         return 10
#     else:
#         return num+sum(num+1)
#
# num = 1
# print(sum(num))


num = int(input("숫자"))
print("* " * (num-1))
for i in range(1,(num+1),2):
    print(("*"),("{:^%d}"%(num)).format("*" * i),("*"))
    # print(("{:>%d}"%(num+1)).format("|"))

for j in range((num-2),0,-2):
    print(("*"),("{:^%d}"%(num)).format("*" * j),("*"))
print("* " * (num - 1))
# print("")

# print("* "*8)
# for i in range(6):
#     print("*"," "*11,"*")
# print("* "*8)