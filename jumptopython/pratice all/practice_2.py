
n=0
while 1:
    name = input("안녕하세요. 이름을 입력하세요.")
    n = n+1
    if n == 1 :
        print("Hi %s!! You are %dst person com here!"%(name,n))
    elif n == 2 :
        print("Hi %s!! You are %dnd person com here!"%(name,n))
    elif n == 3 :
        print("Hi %s!! You are %drd person com here!"%(name,n))
    elif n > 3 and n < 11:
        print("Hi %s!! You are %dth person com here!"%(name,n))
    else:
        print("Sorry %s. The event is closed because You are %dth person come here."%(name,n))

