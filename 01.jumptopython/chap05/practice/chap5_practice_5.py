
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
            try:
                number[1] != 0
                print(a + b)
                print(a - b)
                print(a * b)
                print(a / b)
            except:
                print('죄송합니다. 두 번째 입력에서 0을 입력하셨습니다. 분모는 0이 되어서는 안됩니다.')
    else:
        print('두 수를 입력하세요.')
