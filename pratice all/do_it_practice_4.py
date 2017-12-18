# 프로그램 실행시 실행 인자를 받아 텍스트를 처리하는 메모장 프로그램을 작성한다.
# 입력 받는 문자열은 모두 영어로만 입력을 받는다.
# 예시) python memo.py -a "Life is too short"
# -a 입력시 'memo.txt' 파일이 있으면 열고 없으면 아래와 같이 물어본다.
# 아래 중 선택하세요.
# 1. 새로 생성하시겠습니까?
# 2. 파일 경로를 입력하겠습니다.
# 1인 경우에는 memo.txt를 새로 생성한다. 2인 경우에는 memo.txt 파일이 있는 경로를 입력한다.
# -au 옵션으로 입력시 입력받는 모든 영어 문자를 대문자로 변경하여 처리한다.
# -v가 들어온경우 파일에 있는 문자열을 모두 화면에 출력한다.
# 'memo.txt' 파일이 있으면 열고 없으면 아래와 같이 물어본다.
# 아래 중 선택하세요:
# 1. 종료하시겠습니까?
# 2. 파일 경로를 입력하세요.

import sys

option = sys.argv[1]

def file_add():
    if option == '-a':
        memo = sys.argv[2]
        f=open('memo.txt','a')
        f.write(memo)
        f.write('\n')
        f.close()
    elif option == '-au' :
        memo = sys.argv[2]
        result = memo.upper()
        f=open('memo.txt','a')
        f.write(result)
        f.write('\n')
        f.close()

if option == '-v':
    try :
        f = open('memo.txt','r')
        memo = f.read()
        print(memo)
    except:
        files = int(input('1. 종료하시겠습니까? \n2. 파일 경로를 입력하세요'))
        if files == 1 :
            while True:
                break
        elif files == 2:
            route = input('경로:')
            f = open(route + '\\memo.txt','r')
            memo = f.read()
            print(memo)

else:
    try:
        f = open('memo.txt','r')
        file_add()
    except:
        file = int(input('1. 새로 생성하시겠습니까?\n2.파일 경로를 입력하겠습니다.'))
        if file == 1 :
            file_add()
        elif file ==2 :
            file_location = input('파일 경로를 입력하세요.')
            f = open(file_location + '\\memo.txt','r')
            file_add()





