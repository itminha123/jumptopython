news_list= [
        {
            "link": "http://aaa.com",
            "name": "이명박",
            "shares": {
                "count": 2
            }
        },
        {
            "link": "http://bbb.com",
            "name": "노무현",
            "shares": {
                "count": 28
            }
        },
        {
            "link": "http:ccc.com",
            "name": "박근혜",
            "shares": {
                "count": 12
            }
        }
]
sorted_list = sorted(news_list, key=lambda k: k['shares']['count'],reverse=True)
print(sorted_list)