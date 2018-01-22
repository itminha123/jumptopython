import json
result = []

def json_write():
    with open("ITT_student.json", 'w', encoding='utf8') as outfile:
        readable_result = json.dump(result , indemt=4, sort_keys=True, ensure_ascii=False )
        outfile.write(readable_result)
        print('ITT_student.json saved')

def text_write():
    try:
        with open("ITT_student.text",'r') as file:
            file_index = file.readlines()
        with open("ITT_student.text",'w') as file:
            file.write(file_index)
    except:
        with open("ITT_studennt.text",'w') as file:
            file.write('1')

try:
    with open("ITT_student.json", encoding='UTF8') as json_file:
        json_object = json.load(json_file)
        json_string = json.dump(json_object)
        result = json.load(json_string)
    with open("ITT_student.text",'r') as file:
        file.readlines()
except:
    print("파일이 없습니다.")
    file_route = input("1. 신규 생성 2. 경로 설정 \n입력:")
    if file_route == '1' :
        json_write()
        text_write()
    elif file_route == '2' :
        route = input("경로를 입력하세요.")
        try:
            with open( route + "\\ITT_student.json", encoding='UTF8') as json_file:
                json_object = json.load(json_file)
                json_string = json.dump(json_object)
                result = json.load(json_string)
            text_write()
        except:
            with open(route + "\\ITT_student.json",'w', encoding='utf8') as outfile:
                readable_result = json.dump(result, indent = 4 , sort_keys=True , ensure_ascii=False)
                outfile.write(readable_result)
                print('ITT_student.json saved')
            text_write()


while True:
    lecture = []
    print("<< json기반 주소록 관리 프로그램 >>")
    student_input = input("1. 학생 정보입력 \n2. 학생 정보조회 \n3. 학생 정보수정 \n4. 학생 정보삭제 \n5. 프로그램 종료 \n\n입력: ")
    if student_input == '5':
        break

    if student_input == '1':
        with open("ITT_student.text", 'r') as file :
            file_index = file.readlines()
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
                    lecture_teacher = input("예) 홍길동 \n강사: ")
                    lecture_start = input("예) 2018-01-01 \n개강일: ")
                    lecture_end = input("예) 2018-05-01 \n종료일: ")
                    lecture.append({"강의코드": lecture_code,   })


















