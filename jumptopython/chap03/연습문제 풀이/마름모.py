
x=0
while True:
    n=int(input("사용자 입력:"))
    for i in range(1,n+1):
        if i % 2 == 1:
            print(' ' * n/2+1-i,end='' )
            print('*' + 2 )
        elif n >= x+2 :
            print("홀수를 입력하세요.")
        else:
            n = 0
            print("마름모 연습프로그램을 이용해 주셔서 감사합니다.")
            break

