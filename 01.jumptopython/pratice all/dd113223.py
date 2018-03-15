

# print(str(12).split())
#
# for i in range(1,10):
#     print(i, ':',str(i))

while True:
    # try:
        number = int(input('숫자입력해'))
        # star = 1
        blank = int((number - 1) / 2)
        if number % 2 == 0:
            print('홀수입력해')
        for i in range(1, number + 1):
            if i % 2 == 0:
                print(' ' * blank,end='')
                print('*'*i)
                blank -= -1



    # except:
    #     print('아아 ')