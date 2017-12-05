



def input_ingredient():
    while 1:
        make_sandwiches =str(input("안녕하세요. 원하시는 재료를 입력하세요:"))
        if make_sandwiches == "종료":
            break

            for i in make_sandwiches:
                print("%s를 출력하겠습니다."% make_sandwiches)
                if make_sandwiches == "종료":
                    break


while 1 :
    order = int(input("안녕하세요. 저희 가게에 방문해 주셔서 감사합니다.\n1. 주문\n2. 종료\n입력:"))
    if order == 2:
        break

