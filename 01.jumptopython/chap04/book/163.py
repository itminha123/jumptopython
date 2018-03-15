

f= open("D:/python/01.jumptopython/chap04/book/새파일.txt", 'r')
line = f.readline()
print(line)
f.close()

f= open("D:/python/01.jumptopython/chap04/book/새파일.txt",'r')
while 1:
    line=f.readline()
    if not line:break
    print(line, end='')
f.close()

