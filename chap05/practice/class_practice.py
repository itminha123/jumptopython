
class Calculator:
    def __init__(self, numberlist):
        self.numberlist = numberlist
    def sum(self):
        result = 0
        for i in self.numberlist:
            result = i+result
        return result
    def avr(self):
        total = self.sum()
        result = total / len(self.numberlist)
        return result

if __name__ == "__main__":
    cal1 = Calculator([1,2,3,4,5])
    print(cal1.sum())
    print(cal1.avr())

    cal2 = Calculator([6,7,8,9,10])
    print(cal2.sum())
    print(cal2.avr())

