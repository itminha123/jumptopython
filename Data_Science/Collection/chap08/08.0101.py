import  urllib.request
import json

app_id= ""
app_secret = ""

def get_jtbc_news_page_ID():
    page_name = "jtbcnews"
    access_token = app_id + "|" + app_secret

    base = "https://graph.facebook.com/v2.8"
    node = "/" + page_name
    parameters = "/?access_token = %s" % access_token

    url = base +node +parameters

    req = urllib.request.Request(url)
    print("The request url for jtbc news ID: "+url)

    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            data = json.loads(response.read().decode('utf-8'))
            page_id = data['id']
            print("%s Facebook Numer ic ID: %s" %(page_name,page_id))
    except Exception as e:
        print(e)

    return  page_id

page_id = get_jtbc_news_page_ID()
from_date = "2018-01-24"
to_date = "2018-01-25"
num_statuses = "10"
access_token = app_id + "|" + app_secret

base = "http://graph.facebook.com/v2.8"
node = "/%s/posts"%page_id
fields = "/?fields= id,message,link,name,type,shares,reactions,"+\
    "created_time,comments.limit(0).summary(ture)"+\
    ".limit(0).summary(ture)"
duration = "&since=%s&until=%s"%(num_statuses,access_token)
parameters = "&limit"