from Phone import Phone

class Feature(Phone):
    # Constructor Overloading
    def  __init__(self,price,brand,camera,os, ram):
        print("Inside SmartPhone constructor")
        super().__init__(price, brand, camera)
        self.os = os
        self.ram = ram
        print("Inside SmartPhone constructor")

s = Feature(2000,'Samsung',13,"Android", 2)
