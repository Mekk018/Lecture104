class Customer:
    name = ""
    lastname = ""
    age = 0

    def addCart(self):
        print("Added product to",self.name,self.lastname,"'s cart")

customer1 = Customer()
customer1.name = "Siwakorn"
customer1.lastname = "Siriphan"
customer1.addCart()

custom2 = Customer()
custom2.name = "Rujira"
custom2.lastname = "Siriphan"
custom2.addCart()

custom3 = Customer()
custom3.name = "Nuttawat"
custom3.lastname = "Siriphan"
custom3.addCart()

custom4 = Customer()
custom4.name = "Srimork"
custom4.lastname = "Satun"
custom4.addCart()