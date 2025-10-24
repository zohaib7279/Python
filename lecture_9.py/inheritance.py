class Car:
    @staticmethod
    def start():
        print("Car is started")

    @staticmethod
    def stop():
        print("Car is stop")
class ToyotaCar(Car):
    def __init__(self , name):
        self.name = name
car1 = ToyotaCar("Corrolla")
car2 = ToyotaCar("City")
print(car1.start())