

while True:
    program = input('프로그래밍이 왜 좋으세요? (종료 입력시 프로그램 종료):')
    if program == '종료' :
        break
    name = input('성함을 입력해주세요:')
    try:
        f = open('poll.txt','r')
        f = open('poll.txt', 'a')
        f.write(name + '  ')
        f.write(program + '\n')
        f.close()
    except:
        file_select=int(input('poll.txt 파일이 없습니다. 아래중 선택하세요.\n1. 종료 \n2. 변경된 파일경로입력'))
        if file_select == 1 :
            break
        elif file_select == 2:
            file_location = input('변경된 파일 경로를 입력하세요:')
            f = open(file_location + '\\poll.txt','a')
            f.write('[' + name +'] ')
            f.write(program +'\n')
            f.close()

