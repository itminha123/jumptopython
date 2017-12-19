

while True:
    try:
        number = int(input('숫자:'))
        for i in range(1,number+1) :
            print(('O'*(number-i))+('X'*i))
    except:
        print('꺼져')







