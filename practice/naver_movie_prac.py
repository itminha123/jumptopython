import urllib.request
from bs4 import BeautifulSoup
from pandas import DataFrame

html = urllib.request.urlopen('http://movie.naver.com/movie/sdb/rank/rmovie.nhn')
soup = BeautifulSoup(html,'html.parser')
# print(soup)
# print(soup.prettify())

tags =  soup.findAll('div', attrs={'class':'tit3'})
changes =  soup.findAll('td', attrs={'class':'range ac'})

name = []
for tag in tags:
    tag = list(tag.strings)
    movie_name = tag[1]
    name.append([movie_name])
# print(name)

up_down = []
for change in changes:
    change = list(change.strings)
    movie_change = change[0]
    up_down.append([movie_change])
# print(up_down)

result = []
for i in range(len(name)):
    result.append([str(i+1)]+name[i]+up_down[i])

# print(result)
movie_table = DataFrame(result,columns=('순위','영화명','변동폭'))
movie_table.to_csv('movie.csv', encoding="cp949",mode='w',index=True)


# 과제
# 네이버 영화 랭킹 웹페이지를 분석하여 아래 형식으로 csv 파일을 생성하시오
# 순위 |      영화명       | 변동폭
#  1   |       1987        |   0
#  2   |  신과함께-죄와 벌 |  +1
#  3   |쥬만지: 새로운세계 |  -1.