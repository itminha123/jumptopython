

class Restaurant :
    number_served = 0
    def __init__(self):
        self.restaurant_name = 'mins'
        self.cuisine_type    = 'korean_food'
    def describe_restaurant(self):
        print(" %s 식당이 오픈했습니다." %self.restaurant_name)
        print(" %s 전문점 입니다." %self.cuisine_type)
    def set_number_served(self, number):
        self.number_served = number
        print(self.number_served)
    def increment_number_served(self,increment_number):
        self.number_served = self.number_served + increment_number
        print(self.number_served)

        f=open("고객서빙현황.txt","r")
        line = f.readlines()
        f = open("고객서빙현황.txt",'a')
        f.write('\n')
        f.write(str(self.number_served+int(line[-1])))
        f.close()

name2 = Restaurant()
name2.describe_restaurant()
name2.increment_number_served(40)
name2.increment_number_served(30)


class Korean_Restaurant(Restaurant):
    restaurant_name = 'different'
    cuisine_type = 'Korean_food'
    def describe_restaurant(self):
        print(" %s 식당이 오픈했습니다." %self.restaurant_name)
        print(" %s 전문점 입니다." %self.cuisine_type)
        print(" 주메뉴는 %s 입니다.")
    def set_number_served(self, number):
        self.number_served = number
        print(self.number_served)
    def increment_number_served(self,increment_number):
        self.number_served = self.number_served + increment_number
        print(self.number_served)










