import json
result = []

def student_print(i):
    try:
        print("*ID:%s \n*이름:%s \n*나이:%s \n*주소:%s " % (i['ID'], i['이름'], i['나이'], i['주소']))
        print(" 수강정보\n" + " -과거 수강횟수:%s" % (i['수강정보']['과거 수강횟수']))
        for j in (i["수강정보"]["현재 수강정보"]):
            print(" -현재 수강정보\n" + "  강사코드:%s \n  강의명:%s \n  강사:%s \n  개강일:%s \n  종료일:%s "
              % ((j['강의코드']),(j['강의명']),(j['강사']),(j['개강일']),(j['종료일'])))
    except: pass

def student_search(search):
    student_search_input = input(search+":")
    search_list = []
    for i in result:
        if student_search_input in i[search]:
            search_list.append(i)
    print("<< 요약 정보 >>")
    for i in search_list:
        if len(search_list) == 1:
            student_print(i)
        elif len(search_list) >= 2:
            print("ID:"+i["ID"],"이름:" + i["이름"])

def student_lecture_search(search):
    student_search_input = input(search+":")
    search_list = []
    for i in result:
        try:
            if "현재 수강정보" in i["수강정보"]:
                for j in i["수강정보"]["현재 수강정보"]:
                    if student_search_input == j[search]:
                        search_list.append(i)
        except: pass
    print("<< 요약 정보 >>")
    for i in search_list:
        if len(search_list) == 1:
            student_print(i)
        elif len(search_list) >= 2:
            print("ID:"+i["ID"],"이름:" + i["이름"])

def student_change(change):
    after = input()
    del i[change]
    i[change] = after
    json_write()

def student_lecture_change(change,name):
    try:
        if "현재 수강정보" in i["수강정보"]:
            after_code = input("변경할 강의의 강의코드:")
            for j in i["수강정보"]["현재 수강정보"]:
                if after_code == j["강의코드"]:
                    after = input(name)
                    del j[change]
                    j[change] = after
                    json_write()
        else: print("강의코드가 없습니다. 다시 입력하세요.")
    except:
        print("등록된 강의가 없습니다.")

def json_write():
    with open("ITT_student.json", 'w', encoding='utf8') as outfile:
        readable_result = json.dumps(result, indent=4, sort_keys=True, ensure_ascii=False)
        outfile.write(readable_result)
        print('ITT_student.json saved')

try:
    with open("ITT_student.json", encoding='UTF8') as json_file:
        json_object = json.load(json_file)
        json_string = json.dumps(json_object)
        result = json.loads(json_string)
except:
    print("파일이 없습니다. \n파일을 생성하겠습니다.")
    file_route = input("1. 기존 경로에 생성 2. 새로운 경로에 생성")
    if file_route == '1':
        json_write()
        with open('ITT_student.text', 'w') as file:
            file.write("1")
    elif file_route == '2':
        route = input("경로를 입력하세요:")
        try:
            with open( route + "\\ITT_student.json", encoding='UTF8') as json_file:
                json_object = json.load(json_file)
                json_string = json.dumps(json_object)
                result = json.loads(json_string)

        except:
            with open(route + "\\ITT_student.json", 'w', encoding='utf8') as outfile:
                readable_result = json.dumps(result, indent=4, sort_keys=True, ensure_ascii=False)
                outfile.write(readable_result)
                print('ITT_student.json saved')
            with open('ITT_student.text', 'w') as file:
                file.write("1")

while True:
    lecture = []
    print("\n<< json기반 주소록 관리 프로그램 >>")
    student_inupt = input("1. 학생 정보입력 \n2. 학생 정보조회 \n3. 학생 정보수정 \n4. 학생 정보삭제 \n5. 프로그램 종료")
    if student_inupt == '5':
        break

    if student_inupt == '1':
        # try:
            with open('ITT_student.text', 'r') as file:
                file_index = file.readline()
                file_index = int(file_index)
                student_name = input("이름:")
                student_age = input("나이:")
                student_add = input("주소:")
                lecture_count = input("과거 수강 횟수:")
                while True:
                    student_lecture=input("1. 강의추가 2. 종료")
                    if student_lecture == '1':
                        lecture_code = input("강의코드:")
                        lecture_name = input("강의명")
                        lecture_teacher = input("강사:")
                        lecture_start = input("개강일:")
                        lecture_end = input("종료일:")
                        lecture.append({"강의코드": lecture_code, "강의명": lecture_name,
                                        "강사": lecture_teacher, "개강일": lecture_start, "종료일": lecture_end})
                    elif student_lecture == '2':
                        break
                student = {"ID": "ITT%03d" % int(file_index), "이름": student_name, "나이": student_age,
                           "주소": student_add,"수강정보": { "과거 수강횟수": lecture_count }}
                try:
                    if len(lecture) > 0 :
                        (student["수강정보"])["현재 수강정보"] = lecture
                except: pass

                result.append(student)
                json_write()
                file_index += 1
                with open('ITT_student.text', 'w') as file:
                    file.write(str(file_index))
        # except FileNotFoundError:
        #     with open('ITT_student.text', 'w') as file:
        #         file.write("1")

    elif student_inupt == '2':
        student_value = input("1. 전체 학생정보 조회, 2. 개인 학생정보 조회")
        if student_value == '1':
            for i in result:
                student_print(i)
        elif student_value == '2':
            print("검색할 항목을 선택하세요.")
            search_input = input("1. ID \n2. 이름 \n3. 나이 \n4. 주소 \n5. 과거 수강횟수\n"
                                 "6. 현재 강의를 수강하는 학생 \n7. 현재 수강 과목의 강의명 \n"
                                 "8. 현재 수강 과목의 강사 \n0.되돌아가기")
            if search_input == '1':
                student_search("ID")
            elif search_input == "2":
                student_search("이름")
            elif search_input == "3":
                student_search("나이")
            elif search_input == "4":
                student_search("주소")
            elif search_input == '5':
                student_search_input = input("과거수강횟수:")
                search_list = []
                for i in result:
                    if student_search_input == i["수강정보"]["과거 수강횟수"]:
                        search_list.append(i)
                for i in search_list:
                    if len(search_list) == 1:
                        student_print(i)
                    elif len(search_list) >= 2:
                        print("ID: "+i["ID"], "이름: "+i["이름"] )
            elif search_input == '6':
                for i in result:
                    try:
                        if "현재 수강정보" in i["수강정보"]:
                            print("ID: "+i["ID"], "이름: "+i["이름"])
                    except:
                        pass
            elif search_input == '7':
                student_lecture_search("강의명")
            elif search_input == '8':
                student_lecture_search("강사")
            elif search_input == '0':
                continue

    elif student_inupt == '3':
        print("수정 할 학생정보의 ID를 입력하세요:")
        id_input = input()
        for i in result:
            if id_input == i["ID"]:
                print("수정할 항목을 선택하세요:")
                search_change = input("1. 이름 \n2. 나이. \n3. 주소 \n4. 과거 수강횟수 \n5. 강의코드 \n"
                                      "6. 강의명 \n7. 강사 \n8. 개강일 \n9. 종료일 \n10. 강의 추가하기\n0. 되돌아가기")
                if search_change == '1':
                    print("변경 될 이름:")
                    student_change("이름")
                elif search_change == '2':
                    print("변경 될 나이:")
                    student_change("나이")
                elif search_change == '3':
                    print("변경 될 주소:")
                    student_change("주소")
                elif search_change == '4':
                    i = (i["수강정보"])
                    print("과거 수강횟수")
                    student_change("과거 수강횟수")
                elif search_change == '5':
                    student_lecture_change("강의코드","변경 될 강의코드:")
                elif search_change == '6':
                    student_lecture_change("강의명","변경 될 강의명:")
                elif search_change == '7':
                    student_lecture_change("강사","변경 될 강사:")
                elif search_change == '8':
                    student_lecture_change("개강일","변경 될 개강일:")
                elif search_change == '9':
                    student_lecture_change("종료일","변경 될 종료일:")
                elif search_change == '10':
                    lecture_code = input("추가 할 강의코드:")
                    lecture_name = input("추가 할 강의명")
                    lecture_teacher = input("추가 할 강사:")
                    lecture_start = input("추가 할 개강일:")
                    lecture_end = input("추가 할 종료일:")
                    if "현재 수강정보" in i["수강정보"]:
                        (i["수강정보"]["현재 수강정보"]).append({"강의코드": lecture_code,
                                                       "강의명": lecture_name, "강사": lecture_teacher,
                                                       "개강일": lecture_start, "종료일": lecture_end})
                        json_write()
                    else:
                        i["수강정보"]["현재 수강정보"] = [
                            {"강의코드": lecture_code, "강의명": lecture_name, "강사": lecture_teacher,
                             "개강일": lecture_start,
                             "종료일": lecture_end}]
                        json_write()
                elif search_change == '0':
                    break

    elif student_inupt == '4':
        delete_id = input("ID를 입력하세요:")
        print("삭제 할 항목을 선택하세요.")
        delete = input("1. 학생정보 삭제 2. 현재 수강 과목삭제")
        for i in result:
            if delete_id == i["ID"]:
                if delete == '1':
                    i.clear()
                    result.remove({})
                    json_write()
                elif delete == '2':
                    delete_subject = input("강의코드:")
                    for j in (i['수강정보']['현재 수강정보']):
                        if delete_subject == j["강의코드"]:
                            if len(i['수강정보']["현재 수강정보"]) == 1 :
                                del (i["수강정보"]["현재 수강정보"])
                                json_write()
                            elif len(i['수강정보']['현재 수강정보']) >= 2:
                                j.clear()
                                (i['수강정보']['현재 수강정보']).remove({})
                                json_write()

















