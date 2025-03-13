menu = {}

while True:
    dish = input("Введіть назву страви (або 'стоп' для завершення): ")
    if dish.lower() == "стоп":
        break
    price = float(input(f"Введіть ціну для страви '{dish}': "))
    menu[dish] = price


print("\nМеню:")
for dish, price in menu.items():
    print(f"{dish}: {price} грн")

total_sum = 0

while True:
    order = input("Додайте страву до замовлення: ")
    if order.lower() == "стоп":
        break
    if order in menu:
        total_sum += menu[order]
    else:
        print("Цієї страви немає в меню.")

print(f"\nЗагальна сума замовлення: {total_sum} грн")
