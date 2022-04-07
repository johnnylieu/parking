available_parking = ["small", "big", "medium"]

class Cars:
    def __init__(self, carSize, owner):
        self.carSize =carSize
        self.owner = owner
    
    def park(self):
        for i in range(len(available_parking)):
            # print(f"available_parking: {available_parking}") # works
            # print(f"i: {i}")
            
            if self.carSize != "small" and self.carSize != "medium" and self.carSize != "big":
                # print(f"i: {i}")
                # print(f"available_parking[i]: {available_parking[i]}")
                # print(f"available: {available_parking[i]}")
                print(f"There is no room for your {self.carSize} vehicle")
                return False

            if self.carSize != "small" or self.carSize != "big" or self.carSize != "medium":
                # print(available_parking[i]) # works
                available_parking.remove(available_parking[i])
                # print(available_parking)
                print(f"{self.owner} just parked their {self.carSize} vehicle")
                return True

        if len(available_parking) == 0:
            print(f"Sorry {self.owner}, the garage is full")
            return False

class Garage:
    def __init__(self, cars):
        self.cars = cars


if __name__=="__main__":
    park1 = Garage(Cars("small", "Robert")) # can park
    park2 = Garage(Cars("small", "Steve"))# can park
    park3 = Garage(Cars("medium", "Brian"))# can park
    park4 = Garage(Cars("medium", "Scott"))# can't park, garage is full
    park5 = Garage(Cars("large", "Johnny"))# can't park, garage is full

    park5.cars.park()
    park1.cars.park()
    park2.cars.park()
    park3.cars.park()
    park4.cars.park()