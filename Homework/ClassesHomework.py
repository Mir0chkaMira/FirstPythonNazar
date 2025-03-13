from random import randint

class Employer:

    def __init__(self, name):
        self.name = name
        self.money = 1000
        self.energy = 50
        self.motivation = 50
        self.alive = True

    def work(self):
        print("Час працювати")
        self.money += 500
        self.motivation -= 6
        self.energy -= 5

    def invest(self):
        print("Треба інвестувати")
        self.money -= 150
        live_cube = randint(1, 2)

        if live_cube == 1:
            self.money += 600

        elif live_cube == 2:
            self.money -= 400

    def relax(self):
        print("Час відпочити")
        self.motivation += 5
        self.energy += 5

    def network(self):
        print("Час нетворкінгу")
        self.motivation += 4

    def is_alive(self):
        if self.money < -0.5:
            print("Я збанкрутував")
            self.alive = False

        elif self.motivation <= 0:
            print("В мене дипресія")
            self.alive = False

        elif self.energy <= 0:
            print("Я втомився")
            self.alive = False

        elif self.money >= 50000:
            print("Став богатієм")
            self.alive = False

    def end_of_day(self):
        print(f"Мотивації = {self.motivation}")
        print(f"Грошей = {self.money}")
        print(f"Енергії = {self.energy}")

    def live(self, day):
        print(f"День: {day} - студент: {self.name}")

        live_cube = randint(1, 4)

        if live_cube == 1:
            self.work()

        elif live_cube == 2:
            self.invest()

        elif live_cube == 3:
            self.relax()

        elif live_cube == 4:
            self.network()

        self.end_of_day()
        self.is_alive()


nazar = Employer("Nazar")

for day in range(365):

    if nazar.alive == False:
        break

    nazar.live(day)