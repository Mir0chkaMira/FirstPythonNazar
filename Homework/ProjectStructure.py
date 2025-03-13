#1-Змінні та базові операції
money = float(input("Усього грошей: "))
dinner_cost = float(input("Витрачено на обід: "))
transport_cost = float(input("Треба на транспорт: "))

money_left = money - (dinner_cost + transport_cost)
print(f"Залишилося грошей: {money_left}")


#2-Умови
if money_left < 100:
    print("Грошей мало, час економити!")
else:
    print("Все добре, можна трохи витратити на себе.")


#3-Цикли
