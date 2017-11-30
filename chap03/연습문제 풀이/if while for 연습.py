x=0
while True:
    입력값=int(input("사용자 입력:"))
    if 입력값 %2 == 1:
        for i in range(입력값*2) :
            if i %2 ==1 :
                if i <= 입력값:
                    spaces = 입력값 - i
                    stars = i
                    print(" " * spaces + "* " * stars)
                else:
                    spaces = i - 입력값
                    stars = 2 * 입력값 - i
                    print(" " * spaces + "* " * stars)
    elif 입력값 >= x+2:
        print("홀수를 입력하세요.")

    else:
        입력값 = 0
        print("마름모 연습프로그램을 이용해 주셔서 감사합니다.")
        break


