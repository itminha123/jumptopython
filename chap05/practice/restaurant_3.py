

class Restaurant :
    number_served = 0
    def __init__(self):
        self.restaurant_name = 'mins'
        self.cuisine_type    = 'strak'
    def describe_restaurant(self):
        print(" %s 식당이 오픈했습니다." %self.restaurant_name)
        print(" 주메뉴는 %s 입니다." %self.cuisine_type)
    def set_number_served(self, number):
        self.number_served = number
        print(self.number_served)
    def increment_number_served(self,increment_number):
        self.number_served = self.number_served + increment_number
        print(self.number_served)


name2 = Restaurant()
name2.describe_restaurant()
name2.increment_number_served(50)
name2.increment_number_served(90)


# number2 = Restaurant()
# number2.set_number_served(5)

# number3 = Restaurant()
# number3.increment_number_served(30)



