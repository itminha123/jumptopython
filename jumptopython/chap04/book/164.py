

f= open("D:/python/jumptopython/chap04/book/새파일.txt", 'r')
lines = f.readline()
for line in lines:
    print(line)
f.close()

f= open("D:/python/jumptopython/chap04/book/새파일.txt", 'r')
data = f.read()
print(data)
f.close()

f= open("D:/python/jumptopython/chap04/book/새파일.txt", 'a')
for i in range(11,20):
    data="%d번째 줄입니다.\n" % i
    f.write(data)
f.close()
