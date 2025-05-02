class Phone:
    def __init__(self,price,brand,camera):
        print("Insie Phone Constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("Buying a Phone")
    def show(self):
        print(self.__price)

