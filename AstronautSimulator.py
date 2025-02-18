from random import randint, choice


class Astronaut:
    def __init__(self, name):
        self.name = name

        self.oxygen = 100
        self.energy = 100
        self.inventory = []
        #self.spaceship = Spaceship()

    def mine_resources(self,planet):
        pass

    def ubgrade_ship(self, resources):
        pass
        #self.car = Auto(brands_of_car)

    def communicate_with_aliens(self, alien):
        pass

    def explore(self, planet):
        pass

    def survive_in_space(self):
        pass


class Spaceship:
    def __init__(self, name):
        self.name = name
        self.fuel = 100
        self.hull_strength = 100

    def travel(self,planet):
        self.gladness += 10
        self.home.mess += 5

    def repair(self):
        self.gladness -= 5
        self.home.mess = 0

    def refuel(self):
        self.car.strength += 100
        self.money -= 50

    def add_ubgrade(self, ubgrade):
        self.car.strength += 100
        self.money -= 50

    #def day_info(self, day):
        #print(f"Today the {day} of {self.name}'s life")
        #print(f"Money - {self.money}")
        #print(f"Satiety - {self.satiety}")
        #print(f"Gladness - {self.gladness}")
        #print(f"Food in home - {self.home.food}")
        #print(f"Mess in home - {self.home.mess}")
        #print(f"Car fuel - {self.car.fuel}")
        #print(f"Car strength - {self.car.strength}")
        #print("\n")


class Planet:
    def __init__(self, name):
        self.name = name
        self.habitable = False
        self.resources = []


    def travel(self, planet):
        self.gladness += 10
        self.home.mess += 5

    def repair(self):
        self.gladness -= 5
        self.home.mess = 0

    def refuel(self):
        self.car.strength += 100
        self.money -= 50

    def add_ubgrade(self, ubgrade):
        self.car.strength += 100
        self.money -= 50


class Auto:
    def __init__(self, brand_list):
        self.brand = choice(list(brand_list))
        self.fuel = brand_list[self.brand]["fuel"]
        self.strength = brand_list[self.brand]["strength"]
        self.consumption = brand_list[self.brand]["consumption"]

    def drive(self):
        if self.strength > 0 and self.fuel >= self.consumption:
            self.fuel -= self.consumption
            self.strength -= 1
            return True
        else:
            print("The car cannot move")
            return False


brands_of_car = {
    "BMW": {"fuel": 100, "strength": 100, "consumption": 6},
    "Lada": {"fuel": 50, "strength": 40, "consumption": 10},
    "Volvo": {"fuel": 70, "strength": 150, "consumption": 8},
    "Ferrari": {"fuel": 80, "strength": 120, "consumption": 14}

}


class House:

    def __init__(self):
        self.mess = 0
        self.food = 0


class Job:
    def __init__(self,job_list):
        self.job = choice(list(job_list))
        self.salary = job_list[self.job]["salary"]
        self.gladness_less = job_list[self.job]["gladness_less"]


job_list = {
    "Java developer": {"salary": 50, "gladness_less": 10},
    "Python developer": {"salary": 50, "gladness_less": 3},
    "C++ developer": {"salary": 45, "gladness_less": 35},
}


nazar = Astronaut("Nazar")

for day in range(1, 8):
    if nazar.live(day) == False:
        break