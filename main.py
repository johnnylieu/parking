available_parking = ["small", "big", "medium"]

class Cars:
    def __init__(self, carSize, owner):
        self.carSize =carSize
        self.owner = owner
    
    def park(self):
        for i in range(len(available_parking)):
            # print(available_parking) # works
            if available_parking[i] == self.carSize:
                print(available_parking[i])
                available_parking.remove(available_parking[i])
                print(available_parking)
                return True

class Garage:
    def __init__(self, cars):
        self.cars = cars

park1 = Garage(Cars("big", "Johnny"))
park1.cars.park()