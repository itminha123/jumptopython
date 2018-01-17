import json

result = []
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
    student_inupt = input("1.학생 정보입력 2.학생 정보조회 3.학생 정보수정 4.학생 정보삭제 5.프로그램 종료")
    if student_inupt == '5':
        break
    if student_inupt == '1':
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
        student = {"ID": "ITT%d" % (len(result) + 1), "이름": student_name, "나이": student_age, "주소": student_add,"수강정보": { "과거 수강횟수": lecture_count, "현재 수강정보": lecture}}
        result.append(student)
        with open("ITT_student.json",'w',encoding='utf8') as outfile:
            readable_result = json.dumps(result, indent=4,sort_keys=True,ensure_ascii=False)
            outfile.write(readable_result)
            print('ITT_student.json saved')
    elif student_inupt == '2':

        student_value = input("검색 값을 입력해주세요:")
        for i in result:
            if student_value in i :
                print(i)








