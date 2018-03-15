

class Restaurant :
    def __init__(self):
        self. restaurant_name = 'mins'
        self. cuisine_type    = 'steak'
    def describe_restaurant(self):
        print(" %s 식당이 오픈했습니다." %self.restaurant_name)
        print(" 주메뉴는 %s 입니다." %self.cuisine_type)


name2 = Restaurant()
name2.describe_restaurant()

name3 = Restaurant()
name3.describe_restaurant()

name4 = Restaurant()
name4.describe_restaurant()
