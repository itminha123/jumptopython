

while True:
    student_input = input("1.학생 정보입력 \n2.학생 정보조회 \n3.학생 정보수정 \n4.학생 정보삭제 \n5,프로그램 종료")
    student_id = 'it001'
    student_name = input("이름:")
    student_age = input("나이:")
    student_add = input("주소:")
    lecture_count = input("과거 수강 횟수:")
    lecture_code = input("강의코드:")
    lecture_name = input("강의명")
    lecture_teacher = input("강사:")
    lecture_start = input("개강일:")
    lecture_end = input("종료일:")


result =[
    {
        "ID": student_id,
        "이름": student_name,
        "나이": student_age,
        "주소": student_add,
        "과거 수강 횟수":lecture_count,
        "수강정보":[
        {

            "강의코드":lecture_code,
            "강의명":lecture_name,
            "강사":lecture_teacher,
            "개강일":lecture_start,
            "종료일":lecture_end
        }
    ]
    }
]


