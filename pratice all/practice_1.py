
price = {'유아':'무료', '어린이':10, '성인': 15}
while 1:
    print("cgv 극장에 오신걸 환영합니다.")
    age = int(input("나이를 입력하세요:\n[종료]=0"))
    if age < 3 and age >0 :
        print("무료 입니다.")
        type = '유아'
    elif age >= 3 and age < 15:
        print("10$ 입니다.")
        type = '어린이'
    elif age >= 15 :
        print("15$입니다.")
        type = '성인'
    if age >= 3 :
        money = int(input("금액을 넣어주세요:"))
        if money == price[type] :
            print("감사합니다. cgv에 오신걸 환영합니다.")
        elif money < price[type] :
            print("%d 가 모자랍니다." %(price[type]-money))
        elif money > price[type] :
            print("감사합니다. cgv에 오신걸 환영합니다.\n거스름돈 %d를 반환합니다." %(money-price[type]))

    if age == 0 :
        break
