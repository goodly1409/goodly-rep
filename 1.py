class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.probeg = 0

    def show_probeg(self):
        print("This car has " + str(self.probeg) + " miles on it")

    def update_probeg(self, values):
        self.probeg == values


my_new_car = Car('audi', 'a4', 2016)
my_new_car.show_probeg()

my_new_car.update_probeg(20)
my_new_car.show_probeg()

my_new_car.update_probeg(3)
my_new_car.show_probeg()
