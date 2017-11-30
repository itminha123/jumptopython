
Ticket = 3
vip = 5
visit = 0
while True:
    나이=int(input("나이를 입력하세요."))
    if 나이 >= 4 and 나이 <= 13:
        print("귀하는 [어린이]등급이며 요금은[2000]원 입니다.")
        pay = int(input("요금 유형을 선택하세요.(1:현금, 2:공원 전용 신용 카드)"))
        if pay == 1:
            money = int(input('요금을 입력하세요:'))
            if money == 2000:
                print("감사합니다. 티켓을 발행합니다.")
                visit = visit + 1
                if((visit % 7) == 0 and visit < 22):
                    Ticket -= 1
                    print("축하합니다. 1주년 이벤트에 당첨되었습니다. 여기 무료 티켓을 발행합니다. 잔여 티켓 %d장" % (Ticket))
                elif((visit % 3) == 0) and visit < 16:
                    vip -= 1
                    print("축하 합니다. 연간회원권 구매 이벤트에 당첨되셨습니다. 연간 회원 할인 티켓을 발행합니다. 잔여 할인티켓 %d장" % (vip))
            elif money > 2000:
                print("감사합니다. 티켓을 발행하고 거스름돈 %d를 반환합니다." % (money - 2000))
                visit = visit + 1
                if((visit % 7) == 0 and visit < 22):
                    Ticket -= 1
                    print("축하합니다. 1주년 이벤트에 당첨되었습니다. 여기 무료 티켓을 발행합니다. 잔여 티켓 %d장" % (Ticket))
                elif((visit % 3) == 0) and visit < 16:
                    vip -= 1
                    print("축하 합니다. 연간회원권 구매 이벤트에 당첨되셨습니다. 연간 회원 할인 티켓을 발행합니다. 잔여 할인티켓 %d장" % (vip))
            else:
                print('"%d가 모자랍니다. 이력 하신 %d를 반환합니다."' % (2000 - money, money))
        elif pay == 2:
            money = int(input('사람수를 선택해주세요.'))
            print("%d원 결제 되었습니다. 티켓을 발행합니다." % (2000 * money - (2000 * money / 10)))
            visit = visit + 1
            if ((visit % 7) == 0 and visit < 22):
                Ticket -= 1
                print("축하합니다. 1주년 이벤트에 당첨되었습니다. 여기 무료 티켓을 발행합니다. 잔여 티켓 %d장" % (Ticket))
            elif ((visit % 3) == 0) and visit < 16:
                vip -= 1
                print("축하 합니다. 연간회원권 구매 이벤트에 당첨되셨습니다. 연간 회원 할인 티켓을 발행합니다. 잔여 할인티켓 %d장" % (vip))
    if 나이 >= 14 and 나이 <= 18:
        print("귀하는 [어린이]등급이며 요금은[3000]원 입니다.")
        pay = int(input("요금 유형을 선택하세요.(1:현금, 2:공원 전용 신용 카드)"))
        if pay == 1:
            money = int(input('요금을 입력하세요:'))
            if money == 3000:
                print("감사합니다. 티켓을 발행합니다.")
                visit = visit + 1
                if((visit % 7) == 0 and visit < 22):
                    Ticket -= 1
                    print("축하합니다. 1주년 이벤트에 당첨되었습니다. 여기 무료 티켓을 발행합니다. 잔여 티켓 %d장" % (Ticket))
                elif((visit % 3) == 0) and visit < 16:
                    vip -= 1
                    print("축하 합니다. 연간회원권 구매 이벤트에 당첨되셨습니다. 연간 회원 할인 티켓을 발행합니다. 잔여 할인티켓 %d장" % (vip))
            elif money > 3000:
                print("감사합니다. 티켓을 발행하고 거스름돈 %d를 반환합니다." % (money - 3000))
                visit = visit + 1
                if((visit % 7) == 0 and visit < 22):
                    Ticket -= 1
                    print("축하합니다. 1주년 이벤트에 당첨되었습니다. 여기 무료 티켓을 발행합니다. 잔여 티켓 %d장" % (Ticket))
                elif((visit % 3) == 0) and visit < 16:
                    vip -= 1
                    print("축하 합니다. 연간회원권 구매 이벤트에 당첨되셨습니다. 연간 회원 할인 티켓을 발행합니다. 잔여 할인티켓 %d장" % (vip))
            else:
                print('"%d가 모자랍니다. 이력 하신 %d를 반환합니다."' % (3000 - money, money))
        elif pay == 2:
            money = int(input('사람수를 선택해주세요.'))
            print("%d원 결제 되었습니다. 티켓을 발행합니다." % (3000 * money - (3000 * money / 10)))
            visit = visit + 1
            if ((visit % 7) == 0 and visit < 22):
                Ticket -= 1
                print("축하합니다. 1주년 이벤트에 당첨되었습니다. 여기 무료 티켓을 발행합니다. 잔여 티켓 %d장" % (Ticket))
            elif ((visit % 3) == 0) and visit < 16:
                vip -= 1
                print("축하 합니다. 연간회원권 구매 이벤트에 당첨되셨습니다. 연간 회원 할인 티켓을 발행합니다. 잔여 할인티켓 %d장" % (vip))
    if 나이 >= 19 and 나이 <= 59:
        print("귀하는 [성인]등급이며 요금은[5000]원 입니다.")
        pay = int(input("요금 유형을 선택하세요.(1:현금, 2:공원 전용 신용 카드)"))
        if pay == 1:
            money = int(input('요금을 입력하세요:'))
            if money == 5000:
                print("감사합니다. 티켓을 발행합니다.")
                visit = visit + 1
                if((visit % 7) == 0 and visit < 22):
                    Ticket -= 1
                    print("축하합니다. 1주년 이벤트에 당첨되었습니다. 여기 무료 티켓을 발행합니다. 잔여 티켓 %d장" % (Ticket))
                elif((visit % 3) == 0) and visit < 16:
                    vip -= 1
                    print("축하 합니다. 연간회원권 구매 이벤트에 당첨되셨습니다. 연간 회원 할인 티켓을 발행합니다. 잔여 할인티켓 %d장" % (vip))
            elif money > 5000:
                print("감사합니다. 티켓을 발행하고 거스름돈 %d를 반환합니다." % (money - 5000))
                visit = visit + 1
                if((visit % 7) == 0 and visit < 22):
                    Ticket -= 1
                    print("축하합니다. 1주년 이벤트에 당첨되었습니다. 여기 무료 티켓을 발행합니다. 잔여 티켓 %d장" % (Ticket))
                elif((visit % 3) == 0) and visit < 16:
                    vip -= 1
                    print("축하 합니다. 연간회원권 구매 이벤트에 당첨되셨습니다. 연간 회원 할인 티켓을 발행합니다. 잔여 할인티켓 %d장" % (vip))
            else:
                print('"%d가 모자랍니다. 이력 하신 %d를 반환합니다."' % (5000 - money, money))
        elif pay == 2:
            money = int(input('사람수를 선택해주세요.'))
            print("%d원 결제 되었습니다. 티켓을 발행합니다." % (5000 * money - (5000 * money / 10)))
            visit = visit + 1
            if ((visit % 7) == 0 and visit < 22):
                Ticket -= 1
                print("축하합니다. 1주년 이벤트에 당첨되었습니다. 여기 무료 티켓을 발행합니다. 잔여 티켓 %d장" % (Ticket))
            elif ((visit % 3) == 0) and visit < 16:
                vip -= 1
                print("축하 합니다. 연간회원권 구매 이벤트에 당첨되셨습니다. 연간 회원 할인 티켓을 발행합니다. 잔여 할인티켓 %d장" % (vip))
    if 나이 >= 60 and 나이 <= 65:
        print("귀하는 [성인]등급이며 요금은[5000]원 입니다.")
        pay = int(input("요금 유형을 선택하세요.(1:현금, 2:공원 전용 신용 카드)"))
        if pay == 1:
            money = int(input('요금을 입력하세요:'))
            if money == 5000:
                print("감사합니다. 티켓을 발행합니다.")
                visit = visit + 1
                if((visit % 7) == 0 and visit < 22):
                    Ticket -= 1
                    print("축하합니다. 1주년 이벤트에 당첨되었습니다. 여기 무료 티켓을 발행합니다. 잔여 티켓 %d장" % (Ticket))
                elif((visit % 3) == 0) and visit < 16:
                    vip -= 1
                    print("축하 합니다. 연간회원권 구매 이벤트에 당첨되셨습니다. 연간 회원 할인 티켓을 발행합니다. 잔여 할인티켓 %d장" % (vip))
            elif money > 5000:
                print("감사합니다. 티켓을 발행하고 거스름돈 %d를 반환합니다." % (money - 5000))
                visit = visit + 1
                if((visit % 7) == 0 and visit < 22):
                    Ticket -= 1
                    print("축하합니다. 1주년 이벤트에 당첨되었습니다. 여기 무료 티켓을 발행합니다. 잔여 티켓 %d장" % (Ticket))
                elif((visit % 3) == 0) and visit < 16:
                    vip -= 1
                    print("축하 합니다. 연간회원권 구매 이벤트에 당첨되셨습니다. 연간 회원 할인 티켓을 발행합니다. 잔여 할인티켓 %d장" % (vip))
            else:
                print('"%d가 모자랍니다. 이력 하신 %d를 반환합니다."' % (5000 - money, money))
        elif pay == 2:
            money = int(input('사람수를 선택해주세요.'))
            print("%d원 결제 되었습니다. 티켓을 발행합니다." % ((money * 5000) - (5000 / money * 0.15)))
            visit = visit + 1
            if ((visit % 7) == 0 and visit < 22):
                Ticket -= 1
                print("축하합니다. 1주년 이벤트에 당첨되었습니다. 여기 무료 티켓을 발행합니다. 잔여 티켓 %d장" % (Ticket))
            elif ((visit % 3) == 0) and visit < 16:
                vip -= 1
                print("축하 합니다. 연간회원권 구매 이벤트에 당첨되셨습니다. 연간 회원 할인 티켓을 발행합니다. 잔여 할인티켓 %d장" % (vip))
    if 나이 >=0 and 나이<4:
        print("귀하는 [유아] 등급이며 요금은 무료 입니다.")
    elif 나이 >=66:
        print("귀하는 [노인]등급이며 요금은 무료 입니다.")