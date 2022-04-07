available_parking = ["small", "big", "medium"]

class Cars:
    def __init__(self, carSize, owner):
        self.carSize =carSize
        self.owner = owner
    
    def park(self):
        for i in range(len(available_parking)):
            # print(available_parking) # works
            if available_parking[i] == self.carSize:
                # print(available_parking[i]) # works
                available_parking.remove(available_parking[i])
                # print(available_parking)
                print(f"{self.owner} just parked their {self.carSize} vehicle")
                return True
            
        if self.carSize != available_parking[i]:
            print(f"sorry there is no available parking for your {self.carSize} vehicle")
            return False

class Garage:
    def __init__(self, cars):
        self.cars = cars

park1 = Garage(Cars("large", "Johnny"))
park1.cars.park()