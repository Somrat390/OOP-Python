from Phone import Phone

class SmartPhone(Phone):
    def check(self):
        print(self.__price)
    def buy(self): #Mthod overriding
        print("Buying a SmartPhone")
        super().buy()

s1 = SmartPhone(2000,"APPLE", 13)
s1.buy()
s1.show()
s1.check()