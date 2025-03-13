import random

class Astronaut:
    def __init__(self, name, spaceship):
        self.name = name
        self.oxygen = 100
        self.energy = 100
        self.inventory = []
        self.spaceship = spaceship

    def mine_resources(self, planet):
        if planet.resources:
            resource = random.choice(planet.resources)
            self.inventory.append(resource)
            print(f"{self.name} добув {resource} на {planet.name}.")
        else:
            print(f"На {planet.name} немає ресурсів для добування.")

    def upgrade_ship(self, resource):
        if resource in self.inventory:
            self.spaceship.add_upgrade(resource)
            self.inventory.remove(resource)
            print(f"Корабель {self.spaceship.name} покращено за допомогою {resource}!")
        else:
            print("У рюкзаку немає такого ресурсу!")

    def communicate_with_aliens(self, alien):
        if alien.attitude == "дружній":
            alien.trade(self)
        else:
            alien.negotiate(self)

    def explore(self, planet):
        print(f"{self.name} досліджує {planet.name}...")
        planet.discover_resources()
        if planet.aliens:
            alien = random.choice(planet.aliens)
            print(f"{self.name} зустрів {alien.species}!")
            self.communicate_with_aliens(alien)

    def survive_in_space(self):
        if self.oxygen <= 0 or self.energy <= 0:
            print("Критична ситуація! Потрібно терміново відновити запаси кисню та енергії!")
        else:
            print("Стан астронавта стабільний.")

class Spaceship:
    def __init__(self, name):
        self.name = name
        self.fuel = 100
        self.hull_strength = 100
        self.upgrades = []

    def travel(self, planet):
        if self.fuel >= 20:
            self.fuel -= 20
            print(f"Корабель {self.name} прибув на {planet.name}.")
        else:
            print("Недостатньо пального!")

    def repair(self):
        if "метал" in self.upgrades:
            self.hull_strength = 100
            print("Корабель відремонтовано!")
        else:
            print("Немає необхідних ресурсів для ремонту!")

    def refuel(self, amount):
        self.fuel += amount
        print(f"Запас пального поповнено на {amount}.")

    def add_upgrade(self, upgrade):
        self.upgrades.append(upgrade)
        print(f"Корабель отримав покращення: {upgrade}!")

class Planet:
    def __init__(self, name, resources, habitable, gravity, aliens=[]):
        self.name = name
        self.resources = resources
        self.habitable = habitable
        self.gravity = gravity
        self.aliens = aliens

    def discover_resources(self):
        print(f"На {self.name} доступні ресурси: {', '.join(self.resources) if self.resources else 'немає'}.")

    def hostile_aliens(self):
        return any(alien.attitude == "ворожий" for alien in self.aliens)

class Alien:
    def __init__(self, species, attitude, technology_level, trade_items=[]):
        self.species = species
        self.attitude = attitude
        self.technology_level = technology_level
        self.trade_items = trade_items

    def trade(self, astronaut):
        if self.trade_items:
            item = random.choice(self.trade_items)
            astronaut.inventory.append(item)
            print(f"{self.species} обміняли {item} з {astronaut.name}.")
        else:
            print(f"{self.species} не мають предметів для обміну.")

    def attack(self, astronaut):
        astronaut.energy -= 20
        print(f"{self.species} атакували {astronaut.name}! Енергія знизилася до {astronaut.energy}.")

    def negotiate(self, astronaut):
        success = random.choice([True, False])
        if success:
            print(f"{astronaut.name} вдалося домовитися з {self.species}!")
        else:
            print(f"{self.species} відмовилися від переговорів. Можлива атака!")

spaceship = Spaceship("БМВ2000")
astronaut = Astronaut("Назар", spaceship)
planet = Planet("Марс", ["залізо", "кристали"], True, 3.7, [Alien("Марсіанин", "дружній", 5, ["плазмовий генератор"])])

spaceship.travel(planet)
astronaut.explore(planet)
astronaut.mine_resources(planet)
astronaut.upgrade_ship("залізо")
astronaut.survive_in_space()
