class Sweets:
    def __init__(self,name,type,duration):
        self.name = name
        self.type = type
        self.duration = duration

    def information(self):
        print(f"Хто їв: {self.name}. Тип цукерок: {self.type}. "
              f"Кількість: {self.duration}")

    def how_many_sweets(self):
        return self.duration>40

who_ate_sweets = Sweets("Назар","шоколадні",45)
who_ate_sweets.information()
print(who_ate_sweets.how_many_sweets())