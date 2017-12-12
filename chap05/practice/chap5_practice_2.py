

while True:
    program = input('프로그래밍이 왜 좋으세요? (종료 입력시 프로그램 종료):')
    if program == '종료' :
        break
    name = input('성함을 입력해주세요:')
    f = open('poll.txt','a')
    f.write(name+'  ')
    # f.close()
    # f = open('poll.txt','a')
    f.write(program +'\n')
    f.close()




