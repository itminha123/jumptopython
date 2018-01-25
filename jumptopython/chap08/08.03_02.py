from pprint import pprint
i= {
    "description": "'썰전' 유시민이 <b>이명박</b> 전 대통령의 입장 발표에 대해 분석했다. 25일 오후 방송될 종합편성채널 JTBC '썰전'에서는 <b>이명박</b> 전 대통령의 입장 발표와 MB정부 국정원 특수 활동비 상납 의혹 등에 대해 이야기를 나눈다.... ",
    "org_link": "http://enews24.tving.com/news/article.asp?nsID=1275674",
    "pData": "2018-01-25 14:59:00",
    "title": "'썰전' 유시민, MB 입장 발표문에 &quot;전직 대통령으로서 정치적으로만 대응&quot;"
}

if '&quot;' in i['description'] or i['org_link'] or i['org_link'] or i["title"]:
    pprint(i["title"].replace("&quot;","\'"))
