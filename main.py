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
            
            if available_parking[i] != self.carSize:
                print(f"There is no room for your {self.carSize} vehicle")
                return False

        if len(available_parking) == 0:
            print(f"Sorry {self.owner}, the garage is full")
            return False

class Garage:
    def __init__(self, cars):
        self.cars = cars

park1 = Garage(Cars("small", "Robert")) # can park
park2 = Garage(Cars("small", "Steve"))# can park
park3 = Garage(Cars("medium", "Brian"))# can park
park4 = Garage(Cars("medium", "Brian"))# can't park, garage is full
park1.cars.park()
park2.cars.park()
park3.cars.park()
park4.cars.park()