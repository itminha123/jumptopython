result = [
    {
        "ID": "ITT1",
        "나이": "32",
        "수강정보": {
            "과거 수강횟수": "0",
            "현재 수강정보": [
                {
                    "강사": "이현구",
                    "강의명": "빅데이터",
                    "강의코드": "bd171106",
                    "개강일": "20171106",
                    "종료일": "20180905"
                }
            ]
        },
        "이름": "전민하",
        "주소": "대구시 서구 원대동3가"
    },
    {
        "ID": "ITT2",
        "나이": "32",
        "수강정보": {
            "과거 수강횟수": "1",
            "현재 수강정보": [
                {
                    "강사": "이현구",
                    "강의명": "빅데이터",
                    "강의코드": "bd171106",
                    "개강일": "20171106",
                    "종료일": "20180905"
                },
                {
                    "강사": "이현구",
                    "강의명": "c언어",
                    "강의코드": "cl180101",
                    "개강일": "20180101",
                    "종료일": "20180601"
                }
            ]
        },
        "이름": "김기정",
        "주소": "대구시 동구 파티마병원옆"
    },
    {
        "ID": "ITT3",
        "나이": "29",
        "수강정보": {
            "과거 수강횟수": "1",
            "현재 수강정보": [
                {
                    "강사": "이현구",
                    "강의명": "c언어",
                    "강의코드": "cl180101",
                    "개강일": "20180101",
                    "종료일": "20180601"
                }
            ]
        },
        "이름": "전수범",
        "주소": "대구시 달서구"
    },
    {
        "ID": "ITT4",
        "나이": "29",
        "수강정보": {
            "과거 수강횟수": "1",
            "현재 수강정보": [
                {
                    "강사": "이현구",
                    "강의명": "파이썬",
                    "강의코드": "py180110",
                    "개강일": "2018-01-10",
                    "종료일": "2018-06-10"
                }
            ]
        },
        "이름": "김인한",
        "주소": "대구시 경대정문앞"
    },
    {
        "ID": "ITT007",
        "나이": "bb",
        "수강정보": {
            "과거 수강횟수": "bb",
            "현재 수강정보": [
                {
                    "강사": "b",
                    "강의명": "b",
                    "강의코드": "bb",
                    "개강일": "b",
                    "종료일": "b"
                },
                {
                    "강사": "b",
                    "강의명": "b",
                    "강의코드": "b",
                    "개강일": "b",
                    "종료일": "b"
                }
            ]
        },
        "이름": "김기정",
        "주소": "bb"
    },
    {
        "ID": "ITT011",
        "나이": "a",
        "수강정보": {
            "과거 수강횟수": "a"
        },
        "이름": "a",
        "주소": "a"
    }
]
# a = input("입력:")
# search_list = []
# search_list.append({"강의코드": lecture_code, "강의명": lecture_name,
#                 "강사": lecture_teacher, "개강일": lecture_start, "종료일": lecture_end})
lecture_code = input("강의코드: ")

lecture_name = input("강의명")
lecture_teacher = input("강사:")
lecture_start = input("개강일:")
lecture_end = input("종료일:")

for i in result:
    if "ITT011" == i["ID"]:
            if "현재 수강정보" in i["수강정보"]:
                (i["수강정보"]["현재 수강정보"]).append({"강의코드": lecture_code,
                                              "강의명": lecture_name, "강사": lecture_teacher,
                                              "개강일": lecture_start, "종료일": lecture_end})
                print(i)
            else:
                i["수강정보"]["현재 수강정보"] = [
                    {"강의코드": lecture_code, "강의명": lecture_name, "강사": lecture_teacher, "개강일": lecture_start,
                     "종료일": lecture_end}]
                print(i)








# for i in result:
#     if 'ITT011' == i["ID"]:
#         try:
#             if   "현재 수강정보" in i["수강정보"] :
#                 print(i["ID"],i["이름"])
#         except: print("e")



# print(search_list)




# a = input("입력:")
# b = input("변경:")
# for i in result:
#     if a == i["이름"]:
#         del i["이름"]
#         i["이름"] = b
#         print(i)

# for i in (result[4]["수강정보"]["현재 수강정보"]):
#     if i["강의코드"] == a :
#         print()
# iii=input("입력")
# aaaaa = []
# for i in result:
#     bbbbb = i["이름"]
#     for i in range(len(result)):
    # try:
    #     if iii in i["나이"]:
    #         aaaaa.append(i)
        # elif iii == i["이름"][0]+i["이름"][1]:
        #     aaaaa.append(i)
        # elif iii == i["이름"][0]+i["이름"][1]+bbbbb[2]:
        #     aaaaa.append(i)
        # elif iii == bbbbb[0]+bbbbb[1]+bbbbb[2]+bbbbb[3]:
        #     aaaaa.append(i)
    # except:pass
# for i in aaaaa:
#     if len(aaaaa) == 1:
#         print(i)
#     elif len(aaaaa) >= 2:
#         print(i["ID"])

# print(result[0]["이름"][1])

        # search_index = i[search]
        # try:
        #     if student_search_input == search_index[0]:
        #         search_list.append(i)
        #     elif student_search_input == search_index[0]+search_index[1]:
        #         search_list.append(i)
        #     elif student_search_input == search_index[0]+search_index[1]+search_index[2]:
        #         search_list.append(i)
        #     elif student_search_input == search_index[0]+search_index[1]+search_index[2]+search_index[3]:
        #         search_list.append(i)
        #     elif student_search_input == search_index[0]+search_index[1]+search_index[2]+search_index[3]+search_index[4]:
        #         search_list.append(i)
        #     elif student_search_input == search_index[0]+search_index[1]+search_index[2]+\
        #             search_index[3]+search_index[4]+search_index[5]:
        #         search_list.append(i)
        # except: pass