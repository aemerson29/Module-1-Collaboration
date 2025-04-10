#Alan Emerson
#create-a-car
#4/6/2025
#creates a Vehicle super class just to make a Automobile class (part of the assignment) with a built in Display function to
#show it in a more readable form. Includes a create_car function to create one easier (includes car01 as a test)




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

#creates a car
def create_car():
        #first gathers all data needed
        year = str(input("What year was it made?"))
        brand = str(input("What brand is it?"))
        module = str(input("What module is it?"))
        doors = str(input("How many doors does it have?"))
        roof = str(input("What type of roof does it have?"))

        #then creates an Automobile using the data collected
        car = Automobile(year, brand, module, doors, roof)
        #returns newly created Automobile
        return car

#test run
car01 = create_car()
car01.Display_car()