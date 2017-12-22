# A라는 디렉토리 하위에 있는 텍스트 파일(*.txt) 중에서
# LIFE IS TOO SHORT 라는 문자열을 포함하고 있는 파일들을
# 모두 찾을 수 있는 프로그램을 작성하시오.
# 단, 하위 디렉토리도 포함해서 검색해야 함.


import random

def printMatrix(_list):
    for row in _list:
        print ("   ".join(row))

def randomBomb():
    bomb=['*','.']
    return random.choice(bomb)

m = int(input("컬럼개수를 입력하세요.[100이하]:"))
n = int(input("열에 개수를 입력하세요.[0이상]:"))

n_matrix = []

for ndx in range(0,n):
    n_matrix.append(["*"] * m)


for ndx in range(0,n):
    for mdx in range(0,m):
            n_matrix[ndx][mdx]=randomBomb()

for ndx in range(0,n):
    for mdx in range(0,m):
            if n_matrix[ndx][mdx] != "*":
                bombCount = 0
                for x in range(-1,2):
                    for y in range(-1,2):
                        xindex = ndx + x
                        yindex = mdx + y
                        if xindex > -1 and yindex > -1 and xindex < m  and yindex < n:
                            if "*" == n_matrix[ndx + x][mdx + y]:
                                bombCount = bombCount + 1

                n_matrix[ndx][mdx]=str(bombCount)

printMatrix(n_matrix)