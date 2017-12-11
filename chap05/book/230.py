try:
    number = int(input('양수를 입력하세요'))
    if(number < 0):
        print('양수를 입력하세요')
        raise NotImplementedError
    # f=open('나없는파일','r')
    # 4/0
    print('hello world')
except FileNotFoundError as e:
    print('없는 파일을 열었습니다.')
    print('시스템 에러 메세지:'+str(e))
except ZeroDivisionError:
    print('0으로 나누었습니다.')
# except :
#     print('에러가 발생했습니다.')
except NotImplementedError:
    print('음수를 입력했네요')
else:
    print('Thank You!!')
finally:
    print('See ya later')

print('프로그램 정상 종료')
