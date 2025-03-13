#1-Змінні та базові операції
money = float(input("Усього грошей: "))
food = float(input("Витрати на їжу: "))
transport = float(input("Витрати на транспорт: "))

money_left = money - (food + transport)
print(f"Залишилося грошей: {money_left}")




#2-Умови
if money_left < 100:
    print("Грошей мало, час економити!")
else:
    print("Все добре, можна трохи витратити на себе.")




#3-Цикли
days = int(input("Скільки днів ви хочете вести облік витрат? "))

total_spents = 0

for day in range(1, days + 1):
    print(f"\nДень {day}:")
    food = float(input("Витрати на їжу: "))
    transport = float(input("Витрати на транспорт: "))
    other = float(input("Інші витрати: "))

    daily_spent = food + transport + other
    total_spents += daily_spent

    print(f"Витрати за день {day}: {daily_spent} грн")


print(f"\nЗагальні витрати за {days} днів: {total_spents} грн")




#4-Списки
days = int(input("Скільки днів ви хочете вести облік витрат? "))

total_expenses = 0
expenses_list = []

for day in range(1, days + 1):
    print(f"\nДень {day}:")
    food = float(input("Витрати на їжу: "))
    transport = float(input("Витрати на транспорт: "))
    other = float(input("Інші витрати: "))

    daily_expense = food + transport + other
    total_expenses += daily_expense
    expenses_list.append(daily_expense)

    print(f"Витрати за день {day}: {daily_expense} грн")

print(f"\nЗагальні витрати за {days} днів: {total_expenses} грн")

print("\nСписок витрат за кожен день:", expenses_list)




#5-Словники
days = int(input("Скільки днів ви хочете вести облік витрат? "))

total_expenses = 0
expenses_dict = {}

for day in range(1, days + 1):
    print(f"\nДень {day}:")
    food = float(input("Витрати на їжу: "))
    transport = float(input("Витрати на транспорт: "))
    other = float(input("Інші витрати: "))

    daily_expense = food + transport + other
    total_expenses += daily_expense
    expenses_dict[f"День {day}"] = daily_expense

    print(f"Витрати за день {day}: {daily_expense} грн")

print(f"\nЗагальні витрати за {days} днів: {total_expenses} грн")

print("\nВитрати по днях:")
for day, expense in expenses_dict.items():
    print(f"{day}: {expense} грн")




#6-Функції
def calculate_total_expenses(expenses_dict):
    return sum(expenses_dict.values())

def average_daily_expense(expenses_dict):
    if len(expenses_dict) == 0:
        return 0
    return sum(expenses_dict.values()) / len(expenses_dict)

days = int(input("Скільки днів ви хочете вести облік витрат? "))
expenses_dict = {}
for day in range(1, days + 1):
    print(f"\nДень {day}:")
    food = float(input("Витрати на їжу: "))
    transport = float(input("Витрати на транспорт: "))
    other = float(input("Інші витрати: "))

    daily_expense = food + transport + other
    expenses_dict[f"День {day}"] = daily_expense

    print(f"Витрати за день {day}: {daily_expense} грн")

total_expenses = calculate_total_expenses(expenses_dict)
average_expenses = average_daily_expense(expenses_dict)
print(f"\nЗагальні витрати за {days} днів: {total_expenses} грн")
print(f"Середні витрати на день: {average_expenses} грн")
print("\nВитрати по днях:")
for day, expense in expenses_dict.items():
    print(f"{day}: {expense} грн")



#7-Tkinter
import tkinter as tk
from tkinter import messagebox

expenses_dict = {}
day_counter = 1

def add_expense():
    global day_counter
    try:
        food = float(food_entry.get())
        transport = float(transport_entry.get())
        other = float(other_entry.get())

        total = food + transport + other
        expenses_dict[f"День {day_counter}"] = total
        day_counter += 1

        food_entry.delete(0, tk.END)
        transport_entry.delete(0, tk.END)
        other_entry.delete(0, tk.END)

        messagebox.showinfo("Успіх", "Витрати додано!")

    except ValueError:
        messagebox.showerror("Помилка", "Будь ласка, введіть коректні числа!")

def show_results():
    if not expenses_dict:
        messagebox.showwarning("Попередження", "Немає збережених витрат!")
        return

    total_expenses = sum(expenses_dict.values())
    average_expenses = total_expenses / len(expenses_dict)

    result_text = "\n".join([f"{day}: {expense} грн" for day, expense in expenses_dict.items()])
    result_text += f"\n\nЗагальні витрати: {total_expenses} грн"
    result_text += f"\nСередні витрати на день: {average_expenses} грн"

    messagebox.showinfo("Результати", result_text)

root = tk.Tk()
root.title("Облік витрат")
root.geometry("300x200")

tk.Label(root, text="Витрати на їжу:").grid(row=0, column=0)
food_entry = tk.Entry(root)
food_entry.grid(row=0, column=1)

tk.Label(root, text="Витрати на транспорт:").grid(row=1, column=0)
transport_entry = tk.Entry(root)
transport_entry.grid(row=1, column=1)

tk.Label(root, text="Інші витрати:").grid(row=2, column=0)
other_entry = tk.Entry(root)
other_entry.grid(row=2, column=1)

add_button = tk.Button(root, text="Додати день", command=add_expense)
add_button.grid(row=3, column=0, pady=10)

result_button = tk.Button(root, text="Показати результати", command=show_results)
result_button.grid(row=3, column=1, pady=10)

root.mainloop()




#8-Регулярні вирази
import tkinter as tk
from tkinter import messagebox
import re

expenses_dict = {}
day_counter = 1

def is_valid_number(value):
    login_pattern = re.compile(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")
    return re.match(login_pattern, value) is not None

def add_expense():
    global day_counter
    food = food_entry.get()
    transport = transport_entry.get()
    other = other_entry.get()

    if not (is_valid_number(food) and is_valid_number(transport) and is_valid_number(other)):
        messagebox.showerror("Помилка", "Будь ласка, введіть коректні числа!")
        return

    food = float(food)
    transport = float(transport)
    other = float(other)

    total = food + transport + other
    expenses_dict[f"День {day_counter}"] = total
    day_counter += 1

    food_entry.delete(0, tk.END)
    transport_entry.delete(0, tk.END)
    other_entry.delete(0, tk.END)

    messagebox.showinfo("Успіх", "Витрати додано!")

def show_results():
    if not expenses_dict:
        messagebox.showwarning("Попередження", "Немає збережених витрат!")
        return

    total_expenses = sum(expenses_dict.values())
    average_expenses = total_expenses / len(expenses_dict)

    result_text = "\n".join([f"{day}: {expense} грн" for day, expense in expenses_dict.items()])
    result_text += f"\n\nЗагальні витрати: {total_expenses} грн"
    result_text += f"\nСередні витрати на день: {average_expenses:.2f} грн"

    messagebox.showinfo("Результати", result_text)

root = tk.Tk()
root.title("Облік витрат")
root.geometry("300x200")

tk.Label(root, text="Витрати на їжу:").grid(row=0, column=0, sticky="w")
food_entry = tk.Entry(root)
food_entry.grid(row=0, column=1)

tk.Label(root, text="Витрати на транспорт:").grid(row=1, column=0, sticky="w")
transport_entry = tk.Entry(root)
transport_entry.grid(row=1, column=1)

tk.Label(root, text="Інші витрати:").grid(row=2, column=0, sticky="w")
other_entry = tk.Entry(root)
other_entry.grid(row=2, column=1)

add_button = tk.Button(root, text="Додати день", command=add_expense)
add_button.grid(row=3, column=0, pady=10)

result_button = tk.Button(root, text="Показати результати", command=show_results)
result_button.grid(row=3, column=1, pady=10)

root.mainloop()
