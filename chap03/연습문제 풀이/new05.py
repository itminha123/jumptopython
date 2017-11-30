
Ticket = 3
vip = 5
visit = 0
등급 = {'유아':'무료','어린이':2000,'청소년':3000,'성인':5000,'노인':'무료'}
while True:
    나이=int(input("나이를 입력하세요."))
    if 나이 >=0 and 나이<4:
        print("귀하는 [유아] 등급이며 요금은 무료 입니다.")
        type = '유아'
    elif 나이 >=4 and 나이 <=13:
        print("귀하는 [어린이]등급이며 요금은[2000]원 입니다.")
        type = '어린이'
    elif 나이 >=14 and 나이 <=18:
        print("귀하는 [청소년]등급이며 요금은[3000]원 입니다.")
        type = '청소년'
    elif 나이 >=19 and 나이 <=65:
        print("귀하는 [성인]등급이며 요금은[5000]원 입니다.")
        type = '성인'
    elif 나이 >=66:
        print("귀하는 [노인]등급이며 요금은 무료 입니다.")
        type = '노인'
    if 나이 >= 4 and 나이 <= 65:
        pay = int(input("요금 유형을 선택하세요.(1:현금, 2:공원 전용 신용 카드)"))
        if pay == 1:
            money = int(input('요금을 입력하세요:'))
            if money == 등급[type]:
                print("감사합니다. 티켓을 발행합니다.")
                visit = visit + 1
            elif money > 등급[type]:
                print("감사합니다. 티켓을 발행하고 거스름돈 %d를 반환합니다." % (money - 등급[type]))
                visit = visit + 1
            else:
                print('"%d가 모자랍니다. 이력 하신 %d를 반환합니다."' % (등급[type] - money, money))
        elif pay == 2:
            if 나이>=60 and 나이<=65:
                print("%d원 결제 되었습니다. 티켓을 발행합니다." % ((등급[type] * 0.9)*0.95 ))
                visit = visit + 1
            else:
                print("%d원 결제 되었습니다. 티켓을 발행합니다." %(등급[type]* 0.9))
                visit = visit + 1
        else:
            print("1번 또는 2번 을 눌러주세요")
            continue
        if ((visit % 7) == 0 and visit < 22):
            Ticket -= 1
            print("축하합니다. 1주년 이벤트에 당첨되었습니다. 여기 무료 티켓을 발행합니다. 잔여 티켓 %d장" % (Ticket))
        elif ((visit % 4) == 0) and visit < 21:
            vip -= 1
            print("축하 합니다. 연간회원권 구매 이벤트에 당첨되셨습니다. 연간 회원 할인 티켓을 발행합니다. 잔여 할인티켓 %d장" % (vip))
    else:
        입력값 = 0
        break







