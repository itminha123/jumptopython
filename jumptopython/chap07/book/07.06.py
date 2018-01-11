import urllib.request

from  bs4 import  BeautifulSoup
from pandas import DataFrame

html = urllib.request.urlopen('http://movie.naver.com/movie/sdb/rank/rmovie.nhn')
soup = BeautifulSoup(html,'html.parser')

# print(soup)
# print(soup.prettify())

tags = soup.find_all('div',attrs={"class":"tit3"},)
change = soup.find_all('td',attrs={"class":"range ac"})
# up_do = soup.find_all('td',attrs="alt")

# print(up_down)
# print(tags)
# print(change)
rank = []

i=1
result = []
for tag in tags:
    tr_tag = list(tag.strings)
    movie_name=tr_tag[1]
    result.append([i]+[movie_name])
    i += 1

# number = []
for movie_number in change:
    movie_number = list(movie_number)
    movie_change = movie_number[0]
    result.append([movie_change])

movie_table = DataFrame(result, columns=('순위','영화명'))
movie_table.to_csv("movie.csv",encoding='cp949',mode='w',index=False)







