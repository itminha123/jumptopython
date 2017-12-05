

def input_ingredient():
    sandwich_list = []
    while 1:
        sandwich=input("안녕하세요. 원하는 재료를 입력하세요.")
        if sandwich == "종료" :
            return sandwich_list
        else:
            sandwich_list.append(sandwich)


def make_sandwiches(sandwich_list)  :
    print("샌드위치를 만들겠습니다.")
    for make in sandwich_list :
        print("%s를 추가합니다."% make )


while 1 :
    order = int(input("안녕하세요. 저희 가게에 방문해 주셔서 감사합니다.\n1. 주문\n2. 종료\n입력:"))
    if order == 2:
        break
    elif order == 1:
        sandwich_list =  input_ingredient()
        make_sandwiches(sandwich_list)
        print("여기 주문하신 샌드위치 만들었습니다.")
    else:
        print("숫자만 입력하세요.")

