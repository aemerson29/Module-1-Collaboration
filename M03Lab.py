
#defualt calss
class Vehicle:
    def __init__(self, year, brand, module):
        self.year = year
        self.brand = brand
        self.module = module

#uses Vehicle class as a base
class Automobile(Vehicle):
    def __init__(self, year, brand, module, doors, roof):
        #adds the door and roof
        super().__init__(year, brand, module)
        self.doors = doors
        self.roof = roof
    #prints out all the data in a more readable form
    def Display_car(self):
        print("Year: ", self.year, "\nBrand: ", self.brand, "\nModule: ", self.module, "\nNumber of doors:", self.doors, "\nType of roof:", self.roof)


def create_car():
        year = str(input("What year was it made?"))
        brand = str(input("What brand is it?"))
        module = str(input("What module is it?"))
        doors = str(input("How many doors does it have?"))
        roof = str(input("What type of roof does it have?"))

        car = Automobile(year, brand, module, doors, roof)
        return car

car01 = create_car()

car01.Display_car()
