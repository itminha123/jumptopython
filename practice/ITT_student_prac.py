import json
result = []

def student_print(i):
    try:
        print("-ID: %s \n-이름: %s \n-나이: %s \n-주소: %s " % (i["ID"], i["이름"], i["나이"], i["주소"]))
        print("-수강정보 \n >과거 수강 횟수: %s" % (i["수강정보"]["과거 수강 횟수"]))
        for j in (i["수강정보"]["현재 수강 과목"]):
            print("\t+강의코드: %s \n\t+강의명: %s \n\t+강사: %s \n\t+개강일: %s \n\t+종료일: %s \n"
                  % (j["강의코드"], j["강의명"], j["강사"], j["개강일"], j["종료일"]))
    except:
        pass

def student_count_print(search_list):
    if len(search_list) >= 2:
        print(" << 요약 정보 >>")
    for i in search_list:
        if len(search_list) == 1:
            student_print(i)
        elif len(search_list) >= 2:
            print("ID: %s  이름: %s" % (i["ID"], i["이름"]))

def student_search(search):
    search_list = []
    student_search_input = input(search + ": ")
    for i in result:
        if student_search_input in i[search]:
            search_list.append(i)
    student_count_print(search_list)

def lecture_search(search):
    search_list = []
    lecture_search_input = input(search + ": ")
    for i in result:
        if "현재 수강 과목" in i:
            for j in (i["수강정보"]["현재 수강 과목"]):
                if lecture_search_input in j[search]:
                    search_list.append(i)
    student_count_print(search_list)

def student_change(change):
    print("현재의 %s: %s"%(change, i[change]))
    after = input("변경 될 %s: " % change )
    del i[change]
    i[change] = after
    json_write()

def lecture_change(change):
    if "현재 수강 과목" in i["수강정보"] :
        print("현재 수강중인 과목의 강의코드")
        for j in i["수강정보"]["현재 수강 과목"] :
            print("- %s" % j["강의코드"] ,end=' '  )
        print()
        change_code = input("변경 할 강의의 강의코드: ")
        for j in i["수강정보"]["현재 수강 과목"]:
            if change_code == j["강의코드"]:
                print("현재의 %s: %s" % (change, j[change]))
                after = input("변경 될 %s: " % change)
                del j[change]
                j[change] = after
                json_write()
    else: print("등록된 강의가 없습니다.")

def json_write():
    with open("ITT_Student.json", 'w', encoding='utf8') as outfile:
        readable_result = json.dumps( result , indent=4, sort_keys=True, ensure_ascii=False )
        outfile.write(readable_result)
        print('ITT_Student.json saved')

def text_write():
    try:
        with open("ITT_Student.text",'r') as file:
            file.readline()
    except:
        with open("ITT_Student.text",'w') as file:
            file.write('1')

try:
    with open("ITT_Student.json", encoding='UTF8') as json_file:
        json_object = json.load(json_file)
        json_string = json.dumps(json_object)
        result = json.loads(json_string)
    text_write()

except:
    print("파일이 없습니다.\n 아래 항목을 선택해주세요. \n")
    file_route = input("1. 신규 생성 2. 경로 설정 \n입력:")
    if file_route == '1' :
        json_write()
        text_write()
    elif file_route == '2' :
        route = input("경로를 입력하세요.")
        try:
            with open( route + "\\ITT_Student.json", encoding='UTF8') as json_file:
                json_object = json.load(json_file)
                json_string = json.dumps(json_object)
                result = json.load(json_string)
            text_write()
        except:
            print("경로에 파일이 없습니다.")

while True:
    lecture = []
    print("<< json기반 주소록 관리 프로그램 >>")
    student_input = input("1. 학생 정보입력 \n2. 학생 정보조회 \n3. 학생 정보수정 \n4. 학생 정보삭제 \n5. 프로그램 종료 \n\n입력: ")
    if student_input == '5':
        break

    if student_input == '1':
        with open("ITT_Student.text", 'r') as file :
            file_index = file.readline()
            file_index = int(file_index)
            student_name = input("예) 홍길동 \n이름: ")
            student_age = input("예) 20 \n나이: ")
            student_address = input("예) 대구시 동구 아양로 \n주소:")
            lecture_count = input("예) 0 \n과거 수강 횟수: ")
            while True:
                lecture_add= input("1.강의추가 2.종료 \n입력: ")
                if lecture_add == '1' :
                    lecture_code = input("예) it180120 \n강의코드: ")
                    lecture_name = input("예) 사물인터넷 \n강의명: ")
                    lecture_teacher = input("예) 이순신 \n강사: ")
                    lecture_start = input("예) 2018-01-01 \n개강일: ")
                    lecture_end = input("예) 2018-05-01 \n종료일: ")
                    lecture.append({"강의코드": lecture_code, "강의명":lecture_name,
                                    "강사":lecture_teacher, "개강일": lecture_start, "종료일": lecture_end})
                elif lecture_add == '2':
                    break
            student= {"ID": "ITT%03d" % int(file_index),"이름": student_name, "나이": student_age,
                      "주소": student_address, "수강정보": {"과거 수강 횟수": lecture_count}}
            if len(lecture) > 0 :
                (student["수강정보"])["현재 수강 과목"] = lecture
            result.append(student)
            json_write()
            file_index += 1
            with open("ITT_Student.text", 'w') as file :
                file.write(str(file_index))

    elif student_input == '2':
        search_input = input("1. 전체 학생정보 조회 2. 개인 학생정보 조회 \n입력: ")
        if search_input == '1' :
            for i in result :
                student_print(i)
        elif search_input == '2' :
            print("검색 항목을 선택하세요.")
            student_search_item = input("1. ID \n2. 이름 \n3. 나이 \n4. 주소 \n5. 과거 수강 횟수 \n6. 현재 강의를 수강하는 학생"
                                   "\n7. 현재 수강 과목의 강의명 \n8. 현재 수강 과목의 강사 \n(되돌아가기= 0) \n입력: ")
            if student_search_item == '1':
                student_search("ID")
            elif student_search_item == '2':
                student_search("이름")
            elif student_search_item == '3':
                student_search("나이")
            elif student_search_item == '4':
                student_search("주소")
            elif student_search_item == '5':
                search_list = []
                student_search_input = input("과거 수강 횟수: ")
                for i in result:
                    if student_search_input in (i["수강정보"]["과거 수강 횟수"]):
                        search_list.append(i)
                student_count_print(search_list)
            elif student_search_item =='6':
                for i in result:
                    if "현재 수강 과목" in i :
                        print("ID: %s  이름: %s" % (i["ID"], i["이름"]))
            elif student_search_item == '7':
                lecture_search("강의명")
            elif student_search_item == '8':
                lecture_search("강사")

    elif student_input == '3':
        print("수정 할 ID를 입력하세요. ")
        change_id = input("ID: ")
        for i in result:
            if change_id == i["ID"]:
                print("수정 할 항목을 선택하세요.")
                change_item = input("1. 이름 \n2. 나이 \n3. 주소 \n4. 과거 수강 횟수 \n5. 강의코드 "
                                    "\n6. 강의명 \n7. 강사 \n8. 개강일 \n9. 종료일 \n(되돌아가기= 0) \n입력: ")
                if change_item == '1':
                    student_change("이름")
                elif change_item == '2':
                    student_change("나이")
                elif change_item =='3':
                    student_change("주소")
                elif change_item == '4':
                    i = i["수강정보"]
                    student_change("과거 수강 횟수")
                elif change_item == '5':
                    lecture_change("강의코드")
                elif change_item == '6':
                    lecture_change("강의명")
                elif change_item == '7':
                    lecture_change("강사")
                elif change_item == '8':
                    lecture_change("개강일")
                elif change_item == '9':
                    lecture_change("종료일")
                elif change_item =='0':
                    break

    elif student_input == '4':
        print("삭제 할 ID를 입력하세요.")
        delete_id = input("ID: ")
        for i in result:
            if delete_id == i["ID"] :
                print("삭제 할 항목을 선택하세요.")
                delete_item = input("1. 학생정보 삭제 2. 현재 수강 과목 삭제 \n입력: ")
                if delete_item == '1':
                    i.clear()
                    result.remove({})
                    json_write()
                elif delete_item == '2':
                    if "현재 수강 과목" in i["수강정보"] :
                        print("현재 수강중인 강의코드")
                        for j in (i["수강정보"]["현재 수강 과목"]) :
                            print("- %s" % j["강의코드"], end=' ')
                            print()
                        delete_subject = input("강의코드:")
                        for j in (i["수강정보"]["현재 수강 과목"]) :
                            if delete_subject == j["강의코드"]:
                                if len(i["수강정보"]["현재 수강 과목"]) == 1 :
                                    del (i["수강정보"]["현재 수강 과목"])
                                    json_write()
                                elif len(i["수강정보"]["현재 수강 과목"]) >= 2:
                                    j.clear()
                                    (i["수강정보"]["현재 수강 과목"]).remove({})
                                    json_write()
                    else: print("현재 수강 과목이 없습니다.")












































