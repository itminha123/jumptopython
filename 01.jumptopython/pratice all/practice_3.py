
def multiples(num):
    if num % 10 == 0:
        print('10의 배수가 입니다.')
        # return True
    else:
        print('10의 배수가 아닙니다.')
        # return False
    # return num

while True:
    input_number = int(input("양수를 입력하세요(종료-1):"))
    if input_number == -1 :
        break
    multiples(input_number)
    # elif multiples(input_number) ==True:
        # print("10의 배수 입니다.")
    # elif multiples(input_number) ==False:
        # print("10의 배수가 아닙니다.")



