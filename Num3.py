costs = [100, -40, -60, 200]

good = []
bad = []
money = 0

for cost in costs:
    if cost < 0:
        good.append(cost)
        money += cost
        print(f"Поповнення: {good}")
        print(f"Витрати: {bad}")
        print(f"Усього грошей: {money}")

    elif cost > 0:
        bad.append(cost)
        money += cost
        print(f"Поповнення: {good}")
        print(f"Витрати: {bad}")
        print(f"Усього грошей: {money}")

