

class FourCal:
    def setdata(self, first, second):
        self.frist = first
        self.second = second
    def sum(self):
        result = self.frist + self.second
        return result
    def mul(self):
        result = self.frist * self.second
        return  result
    def sub(self):
        result = self.frist - self.second
        return result
    def div(self):
        result = self.frist / self.second
        return result

a=FourCal()
b=FourCal()
a.setdata(4,2)
b.setdata(3,7)
print(a.sum())
print(a.sub())
print(a.mul())
print(a.div())
print(b.sum())
print(b.sub())
print(b.mul())
print(b.div())

