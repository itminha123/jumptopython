import urllib.request
from bs4 import BeautifulSoup
from pandas import DataFrame

html = urllib.request.urlopen('http://movie.naver.com/movie/sdb/rank/rmovie.nhn')
soup = BeautifulSoup(html,'html.parser')

tags =  soup.findAll('div', attrs={'class':'tit3'})
changes =  soup.findAll('td', attrs={'class':'range ac'})
store_all = soup.find_all('img')

taste_all = []
for i in store_all[8:108]:
    i = str(i)
    print(i.split()[1].split("=")[1])
    taste_all.append(i.split()[1].split("=")[1])

taste = []
for i in taste_all:
    if i[1:-1] == 'na' :
        taste.append("")
    elif i[1:-1] == 'up' :
        taste.append("+")
    elif i[1:-1] == 'down':
        taste.append('-')

name = []
for tag in tags:
    tag = list(tag.strings)
    movie_name = tag[1]
    name.append([movie_name])

up_down = []
for change in changes:
    change = list(change.strings)
    movie_change = change[0]
    up_down.append(movie_change)

taste_up_down = []
for i in range(len(taste)):
    taste_up_down.append([taste[i] + up_down[i]])

result = []
for i in range(len(name)):
    result.append([str(i+1)]+name[i]+taste_up_down[i])

print(result)
# movie_table = DataFrame(result,columns=('순위','영화명','변동폭'))
# movie_table.to_csv('movie.csv', encoding="cp949",mode='w',index=False)

