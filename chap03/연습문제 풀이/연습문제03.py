
while True:
    나이=int(input("나이를 입력하세요."))
    if 나이 >=0 and 나이<4:
        print("귀하는 [유아] 등급이며 요금은 무료 입니다.")
    elif 나이 >=4 and 나이 <=13:
        print("귀하는 [어린이]등급이며 요금은[2000]원 입니다.")
        money = int(input('요금을 입력하세요:'))
        if money == 2000:
            print("감사합니다. 티켓을 발행합니다.")
        elif money > 2000:
            print("감사합니다. 티켓을 발행하고 거스름돈 %d를 반환합니다." % (money - 2000))
        else:
            print('"%d가 모자랍니다. 이력 하신 %d를 반환합니다."' %(2000-money,money))
    elif 나이 >=14 and 나이 <=18:
        print("귀하는 [청소년]등급이며 요금은[3000]원 입니다.")
        money = int(input('요금을 입력하세요:'))
        if money == 3000:
            print("감사합니다. 티켓을 발행합니다.")
        elif money > 3000:
            print("감사합니다. 티켓을 발행하고 거스름돈 %d를 반환합니다." % (money - 3000))
        else:
            print('"%d가 모자랍니다. 이력 하신 %d를 반환합니다."' %(3000-money,money))
    elif 나이 >=19 and 나이 <=65:
        print("귀하는 [성인]등급이며 요금은[5000]원 입니다.")
        money = int(input('요금을 입력하세요:'))
        if money == 5000:
            print("감사합니다. 티켓을 발행합니다.")
        elif money > 5000:
            print("감사합니다. 티켓을 발행하고 거스름돈 %d를 반환합니다." % (money - 5000))
        else:
            print('"%d가 모자랍니다. 이력 하신 %d를 반환합니다."' % (5000 - money, money))

    elif 나이 >=66:
        print("귀하는 [노인]등급이며 요금은 무료 입니다.")