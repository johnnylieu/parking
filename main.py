available_parking = ["small", "big", "medium"]

class Cars:
    def __init__(self, carSize, owner):
        self.carSize =carSize
        self.owner = owner
    
    def park(self):
        for i in range(len(available_parking)):
            print(available_parking[i])

class Garage:
    def __init__(self, cars):
        self.cars = cars

park1 = Garage(Cars("big", "Johnny"))
park1.cars.park()