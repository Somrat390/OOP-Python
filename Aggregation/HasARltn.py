class customer:
    def __init__(self,name,gender,adress):
        self.name = name
        self.gender = gender
        self.adress = adress
    def showAdress(self):
        print(self.adress.city,self.adress.state,self.adress.pin)

    def editAdress(self,new_name, new_city, new_pin, new_state):
        self.name = new_name
        self.adress.editAdress(new_city,new_pin,new_state)





class Adress:
    def __init__(self,city,state,pin):
        self.city = city
        self.state = state
        self.pin = pin
    def editAdress(self,new_city,new_pin,new_state):
        self.city = new_city
        self.state = new_state
        self.pin = new_pin


ad1 = Adress('Dhaka',"Ashulia", 1234)
c1 = customer("Somrat","male", ad1)
c1.showAdress()

c1.editAdress("Ankit","Jp", 4567, "Jp")
c1.showAdress()
