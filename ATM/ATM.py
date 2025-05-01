class Atm:
    def __init__(self):
        self.__pin = ''
        self.__balance = 0
        self.menu()

    def getbalance(self):
        return self.__balance
    def setbalance(self,new_balance):
        if type(new_balance) == int:
            self.__balance = new_balance
        else:
            print("Invalid Balance")

    def menu(self):
        while True:
            user_input = input("""
            Hi How can i help you
            1.Press 1 to create pin
            2.Press 2 to change pin
            3.Press 3 to check balance
            4.Press 4 to withdraw
            5.Press 5 to deposit money
            6.Anything else to exit
            """)
            if user_input == '1':
                self.createpin()
            elif user_input == '2':
                self.changepin()
            elif user_input == "3":
                self.checkbalance()
            elif user_input == "4":
                self.withdrawbalnce()
            elif user_input == "5":
                self.depositbalance()
            else:
                print("Good Bye ")
                exit()

    def createpin(self):
        user_pin = input("Enter your Pin : ")
        self.__pin = user_pin

        print("Pin created successfully")

    def changepin(self):
       for i in range(3,0,-1):
           old_pin = input("Enter Your Old Pin ")
           if self.__pin == old_pin:
               new_pin = input("Enter Your New Pin")
               self.__pin = new_pin
               return
           else:
               print(f"You Enter Wrong Pin , You have left {i - 1} attempt")
       print("Too many Wrong Attempt. Existing for security purpose")
       exit()

    def checkbalance(self):
        for i in range(3, 0, -1):
            pin = input("Enter Your Pin: ")
            if self.__pin == pin:
                print(f"Your Balance is {self.__balance}")
                return
            else:
                print("You Enter Wrong Pin! Try Again")
        print("Too many Wrong Attempt. Existing for security purpose")
        exit()


    def depositbalance(self):
        for i in range(3, 0, -1):
            pin = input("Enter Your Pin: ")
            if self.__pin == pin:
                balance = int(input("Enter Your Balance"))
                self.__balance += balance
                print("Deposit Successfully")
                return
            else:
                print("You Enter Wrong Pin! Try Again")
        print("Too many Wrong Attempt. Existing for security purpose")
        exit()


    def withdrawbalnce(self):
        for i in range(3, 0, -1):
            pin = input("Enter Your Pin: ")
            if self.__pin == pin:
                balance = int(input("Enter Withdraw Amount"))
                if self.__balance >= balance:
                    self.__balance -= balance
                    print(f"Your Balance now {self.__balance} tk")
                else:
                    print(f"You dont have sufficient money.You can withdraw {self.__balance} money")
                return
            else:
                print("You Enter Wrong Pin! Try Again")
        print("Too many Wrong Attempt. Existing for security purpose")
        exit()



obj = Atm()
obj.getbalance()
