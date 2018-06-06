class Bike:
    def __init__(self,price1,max_speed1):
        self.price=price1
        self.max_speed=max_speed1
        self.miles=0
    def displayInfo(self):
        print(self.price, self.max_speed, self.miles)
    def ride(self):
        print("Riding")
        self.miles+=10
    def reverse(self):
        print("Reversing")
        self.miles-=5

trek=Bike(300,17)
huffy=Bike(300,17)
leopard=Bike(300,17)

trek.ride()
trek.ride()
trek.ride()
trek.reverse()
trek.displayInfo()

huffy.ride()
huffy.ride()
huffy.reverse()
huffy.reverse()
huffy.displayInfo()

leopard.reverse()
leopard.reverse()
leopard.reverse()
leopard.displayInfo()





