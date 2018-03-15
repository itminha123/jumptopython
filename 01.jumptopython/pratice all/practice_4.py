

while 1:
    print("숫자마다 공백을 주세요. 예)3 4 5")

    fluid = input("세개의 양수를 입력하세요 (종료-1):").split(' ')
    if len(fluid) == 3:
        a=int(fluid[0])
        b=int(fluid[1])
        c=int(fluid[2])
        if c % a == 0 and c % b == 0:

            print("%d는 %d와 %d의 공배수 입니다." % (c, b, a))
        else:
            print("%d는 %d와 %d의 공배수가 아닙니다." % (c, b, a))
    elif fluid[0] == '-1' :
        break



