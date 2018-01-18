import json
result = []

def student_print(i):
    try:
        print("이름:%s 나이:%s 주소:%s " % (i['이름'], i['나이'], i['주소']))
        print("수강정보\n" + "과거 수강횟수:%s\n" % (i['수강정보']['과거 수강횟수']))
        for j in (i["수강정보"]["현재 수강정보"]):
            print("현재 수강정보\n" + "강사코드:%s 강의명:%s 강사:%s 개강일:%s 종료일:%s "
              % ((j['강의코드']),(j['강의명']),(j['강사']),(j['개강일']),(j['종료일'])))
    except: pass

def student_search(search):
    student_search_input = input(search+":")
    for i in result:
        if student_search_input == i[search]:
            student_print(i)

def student_change(change):
    after = input()
    del i[change]
    i[change] = after

def student_lecture_change(change,name):
    after_code = input("변경할 강의의 수강코드:")
    after = input(name)
    for j in i["수강정보"]["현재 수강정보"]:
        if j == j["강의코드"]:
            del j[change]
            i[change] = after

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
    with open("ITT_student.json", 'w', encoding='utf8') as outfile:
        readable_result = json.dumps(result, indent=4, sort_keys=True, ensure_ascii=False)
        outfile.write(readable_result)

while True:
    lecture = []
    print("<< json기반 주소록 관리 프로그램 >>")
    student_inupt = input("1.학생 정보입력 \n2.학생 정보조회 \n3.학생 정보수정 \n4.학생 정보삭제 \n5.프로그램 종료\n")
    if student_inupt == '5':
        break

    if student_inupt == '1':
        try:
            with open('ITT_student.text', 'r') as file:
                file_index = file.readline()
                file_index = int(file_index)
                student_name = input("이름:")
                student_age = input("나이:")
                student_add = input("주소:")
                lecture_count = input("과거 수강 횟수:")
                while True:
                    student_lecture=input("1.강의추가 2.종료")
                    if student_lecture == '1':
                        lecture_code = input("강의코드:")
                        lecture_name = input("강의명")
                        lecture_teacher = input("강사:")
                        lecture_start = input("개강일:")
                        lecture_end = input("종료일:")
                        lecture.append({"강의코드": lecture_code, "강의명": lecture_name, "강사": lecture_teacher, "개강일": lecture_start, "종료일": lecture_end})
                    elif student_lecture == '2':
                        break
                student = {"ID": "ITT%03d" % int(file_index), "이름": student_name, "나이": student_age, "주소": student_add,"수강정보": { "과거 수강횟수": lecture_count, "현재 수강정보": lecture}}
                result.append(student)
                json_write()
                file_index += 1
                with open('ITT_student.text', 'w') as file:
                    file.write(str(file_index))
        except FileNotFoundError:
            with open('ITT_student.text', 'w') as file:
                file.write("2")

    elif student_inupt == '2':
        student_value = input("1.전체 학생정보 조회, 2.개인 학생정보 조회")
        if student_value == '1':
            for i in result:
                student_print(i)
        elif student_value == '2':
            print("검색할 항목을 선택하세요.")
            search_input = input("1.ID 2.이름 3.나이 4. 주소 5. 과거 수강횟수")
            if search_input == '1':
                student_search("ID")
            elif search_input == "2":
                student_search("이름")
            elif search_input == "3":
                student_search("나이")
            elif search_input == "4":
                student_search("주소")
            elif search_input == '5':
                student_search("과거 수강횟수")

    elif student_inupt == '3':
        print("수정 할 학생정보의 ID를 입력하세요:")
        id_input = input()
        for i in result:
            if id_input == i["ID"]:
                print("수정할 항목을 선택하세요:")
                search_change = input("1.이름 2.나이. 3.주소 4.과거 수강횟수 5.강의코드 6.")
                if search_change == '1':
                    print("이름:")
                    student_change("이름")
                    json_write()
                elif search_change == '2':
                    print("나이:")
                    student_change("나이")
                    json_write()
                elif search_change == '3':
                    print("주소:")
                    student_change("주소")
                    json_write()
                elif search_change == '4':
                    i = (i["수강정보"])
                    print("과거 수강횟수")
                    student_change("과거 수강횟수")
                    json_write()
                elif search_change == '5':
                    student_lecture_change("강의코드","강의코드:")
                    json_write()

    elif student_inupt == '4':
        delete_id = input("ID를 입력하세요:")
        print("삭제 할 항목을 선택하세요.")
        delete = input("1.학생정보 삭제 2.현재 수강 과목삭제")
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
                            j.clear()
                            (i['수강정보']['현재 수강정보']).remove({})
                            json_write()

















