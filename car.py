class Car:
    def __init__(self,price,speed,fuel,mileage):
        self.price=price
        self.speed=speed
        self.fuel=fuel
        self.mileage=mileage
        self.salesTax=15 if price>10000 else 12
    def display_all(self):
        return ("price:" + str(self.price), "speed:" + str(self.speed), "fuel:" + str(self.fuel), "mileage:" + str(self.mileage), "tax:" + str(self.salesTax))

Porsche=Car(80020,181,13,5)
Audi=Car(180000,202,15,80)
Acura=Car(220000,198,10,12)
Chevrolet=Car(90000,200,13,5)
Volvo=Car(1000,80,20,500000)
Delorean=Car(80000,181,13,5)

print (Porsche.display_all())
