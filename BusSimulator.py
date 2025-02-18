class Human:

    def __init__(self, name):
        self.name = name


class Auto:

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.passengers = []

    def add_passenger(self,*args):
        for passenger in args:
            self.passengers.append(passenger)

    def print_passengers_name(self):
        if self.passengers != []:
            print(f"Names of {self.brand} {self.model} passenger")

            for passenger in self.passengers:
                print(passenger.name)

        else:
            print(f"There are no passengers ib {self.brand}  {self.model}")


nazar = Human("Nazar")
sasha = Human("Sasha")
andriy = Human("Andriy")
maks = Human("Maks")

car = Auto("BMW", "X5")

car.add_passenger(nazar, sasha, andriy, maks)

car.print_passengers_name()