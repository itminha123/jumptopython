


while 1:
    try:
        start =int(input("공배수의 첫번째수를 입력해주세요:\n(0 <- 종료)"))
        if start == 0:
            print("쳇... bye")
            break
        end   =int(input("공배수의 두번째 수를 입력해주세요:"))
        scope =int(input("구하고 싶은 공배수의 범위를 지정해주세요:"))

        for i in range(scope):
            if i % start == 0 and i % end == 0:
                print(i)
        print("구하고 싶은 공배수 입니다.")
    except:
        print("숫자만 입력하세요")










