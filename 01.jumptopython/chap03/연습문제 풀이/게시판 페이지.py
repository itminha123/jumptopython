


while True:
    m = int(input("게시물(m)의 수 : "))
    n = int(input("페이지당 게시물(n)의 수 : "))
    if (m % n) > 0:
        page = m / n + 1
    elif (m % n) == 0:
        page = m / n
    print("m =", m, " n =", n, " page = %d" %(page))