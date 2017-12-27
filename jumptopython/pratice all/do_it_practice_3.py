
def getTotalpage(m,n):
    if (m % n) > 0:
        page = m / n + 1
        # print('게시물 총 건수: %d, 한 페이지에 보여줄 게시물 수: %d, 총 페이지수: %d'%(m,n,page))
    elif (m % n) == 0:
        page = m / n
    print('게시물 총 건수: %d, 한 페이지에 보여줄 게시물 수: %d, 총 페이지수: %d'%(m,n,page))

# while True:
f = open('condition.txt', 'r')
lines = f.readlines()
for line in lines:
    result = line.split()
    m = result[0]
    n = result[1]
    try:
        m = int(m)
        n = int(n)
        getTotalpage(m,n)
    except:
        pass
    # else:
    #     getTotalpage(m,n)

    # else:
    #     continue

