
while True:
    나이=int(input("나이를 입력하세요."))
    if 나이 >=0 and 나이<4:
        print("귀하는 [유아] 등급이며 요금은 무료 입니다.")
    elif 나이 >=4 and 나이 <=13:
        print("귀하는 [어린이]등급이며 요금은[2000]원 입니다.")
    elif 나이 >=14 and 나이 <=18:
        print("귀하는 [청소년]등급이며 요금은[3000]원 입니다.")
    elif 나이 >=19 and 나이 <=65:
        print("귀하는 [성인]등급이며 요금은[5000]원 입니다.")
    elif 나이 >=66:
        print("귀하는 [노인]등급이며 요금은 무료 입니다.")
