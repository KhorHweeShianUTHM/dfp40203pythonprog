class Car:
    def __init__(self, make, model, price, inventory):
        self.__make = make # properties
        self.__model = model
        self.__price = price
        self.__inventory = inventory

#define Setters and Getters
    def get_make(self): # getter
        return self.__make
    def set_make(self, make):#setter
        self.__make = make

    def get_model(self):
        return self.__model
    def set_model(self, model):
        self.__model = model

    def get_price(self):
        return self.__price
    def set_price(self, price):
        self.__price = price

    def get_inventory(self):
        return self.__inventory
    def set_inventory(self, inventory):
        self.__inventory = inventory

    make = property(get_make, set_make)
    model = property(get_model, set_model)
    price = property(get_price, set_price)
    inventory = property(get_inventory, set_inventory)

    def display(self):
        print("{0} {1} - price:{2:.2f}, inventory:{3:d}".format(self.make, 
                                                                self.model, 
                                                                self.price, 
                                                                self.inventory))

    def sellCar(self, quantity):
        self.__inventory = self.__inventory - quantity


class Sedan(Car):
    def __init__(self, make, model, price, inventory, doors, seats):
        super(Sedan, self).__init__(make, model, price, inventory)
        self.__doors = doors
        self.__seats = seats

    def get_doors(self):
        return self.__doors
    def set_doors(self, doors):
        self.__doors = doors

    def get_seats(self):
        return self.__seats
    def set_seats(self, seats):
        self.__seats = seats

    doors = property(get_doors, set_doors)
    seats = property(get_seats, set_seats)

    def display(self):
        print("This sedan has {0} doors and {1} seats".format(self.doors, self.seats))
        

car1 = Car("Chevy", "Volt", 15000.00, 10)
sedan1 = Sedan("Ford", "Focus", 10000, 10, 4, 5)


car1.display()
sedan1.display()

car1.sellCar(3)
car1.display()

sedan1.doors = 3
sedan1.display()


def __eq__(self, other):
    if (self.price == other.price):
        return True

def __gt__(self, other):
    if (self.price > other.price):
        return True

def __lt__(self, other):
    if (self.price < other.price):
        return True
            

class Car:
    def factory(type):
        class Sedan(Car):
            def display(self):
                print("This is a new sedan")

        class Sports(Car):
            def display(self):
                print("This is a sports car")

        if (type == "Sedan"):
            return Sedan()

        if (type == "Sports"):
            return Sports()