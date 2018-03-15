import urllib.request
from bs4 import BeautifulSoup
from pandas import DataFrame
import pprint

html = urllib.request.urlopen('http://movie.naver.com/movie/sdb/rank/rmovie.nhn')
soup = BeautifulSoup(html,'html.parser')
# print(soup)
# print(soup.prettify())

tags =  soup.findAll('div', attrs={'class':'tit3'})
changes =  soup.findAll('td', attrs={'class':'range ac'})
# changes =  soup.findAll('td')
# print(changes)
store_all = soup.find_all('img')
# print(store_all)
taste_all = []
for i in store_all[8:108]:
    i = str(i)
    taste_all.append(i.split()[1].split("=")[1])
    # result.append(i[1])
# print(taste_all)
# print(len(taste_all))
taste = []
for i in taste_all:
    if i[1:-1] == 'na' :
        taste.append("")
    elif i[1:-1] == 'up' :
        taste.append("+")
    elif i[1:-1] == 'down':
        taste.append('-')
# print(len(taste))

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
    up_down.append(movie_change)
# print(up_down)

taste_up_down = []
for i in range(len(taste)):
    taste_up_down.append([taste[i] + up_down[i]])

# print(taste_up_down)
# print(len(up_down))
# print(len(taste_up_down))
# print(len(name))
result = []
for i in range(len(name)):
    result.append([str(i+1)]+name[i]+taste_up_down[i])

print(result)
# movie_table = DataFrame(result,columns=('순위','영화명','변동폭'))
# movie_table.to_csv('movie.csv', encoding="cp949",mode='w',index=False)
#

# 과제
# 네이버 영화 랭킹 웹페이지를 분석하여 아래 형식으로 csv 파일을 생성하시오
# 순위 |      영화명       | 변동폭
#  1   |       1987        |   0
#  2   |  신과함께-죄와 벌 |  +1
#  3   |쥬만지: 새로운세계 |  -1.