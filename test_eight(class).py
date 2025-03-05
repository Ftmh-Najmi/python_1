# گالری خودرو

class Car:
    cars_number = 0

    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.status = False
        Car.cars_number +=1


    def start(self):
        if self.status == False:
            self.status = True
            print(f'{self.name} is starting!')
        else:
            print('Car is on ,dont start again!!!')

    def off(self):
        if self.status == True:
            self.status = False
            print(f'{self.name} is off now!')
        else:
            print('Car is off ,start first!!!')

#print(Car.cars_number)

car1 = Car('Benz' , 20000)
car2 = Car('Toyota' , 13000)
car3 = Car('Porsche' , 12000)
car4 = Car('Ferrari' , 15000)
car5 = Car('Audi' , 11000)

print(Car.cars_number)

car1.off()

car2.start()

car2.start()

car2.off()