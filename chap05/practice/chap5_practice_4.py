
def sum(a,b):
    result = a+b
    return result

while True :
    print('숫자의 공백을 주세요 예) 4 5')
    number = input('두 수를 입력하세요. (종료:프로그램종료):').split()
    if number[0] == '종료' :
        break

    if    len(number) == 2 :
        try:
            a = int(number[0])
            b = int(number[1])
        except:
            try:
                number[0] == int(number[0])
            except:
                print('첫번째 입력이 %s 입니다.' % number[0])
            try:
                number[1] == int(number[1])
            except:
                print('두번째 입력이 %s 입니다.' % number[1])
        else:
            print(sum(a, b))
    else:
        print('두 수를 입력하세요.')



