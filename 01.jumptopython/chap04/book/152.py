
def say_myself(name,old,man=True):
#def say_myself(name,man=True,old):
#def say_myself(name,old,man):
    print('나의 이름은 %s입니다.'% name)
    print('나이는 %d살 입니다.'% old)
    if man:
        print('남자 입니다.')
    else:
        print('여자 입니다.')


say_myself("박응용",27)

say_myself("박응용",27 ,True)

say_myself('박응용',27 , False)

say_myself('박응용',True)