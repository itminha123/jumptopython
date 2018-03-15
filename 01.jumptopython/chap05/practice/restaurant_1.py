

class Restaurant :
    def __init__(self):
        self. restaurant_name = 'mins'
        self. cuisine_type    = 'strak'
    def describe_restaurant(self):
        print(" %s 식당이 오픈했습니다." %self.restaurant_name)
        print(" 주메뉴는 %s 입니다." %self.cuisine_type)


name2 = Restaurant()
name2.describe_restaurant()

b = str(result2)

f = open("고객서빙현황.txt", 'r')
f = open("고객서빙현황.txt", 'a')
f.write('%s\n' % b)
f.close()