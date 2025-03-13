#Частина 1
#Завдання 1
try:

    name = input("Введіть ваше ім'я: ")
    age = int(input("Введіть ваш вік: "))
    if age < 0 or age > 120:
        raise ValueError("Ваш вік не може бути таким.")

except ValueError as e:
    print(f"Помилка: {e}")

else:
    print(f"Привіт, {name}! Твій вік — {age}")



#Завдання 2
def function(name = input("Введіть ваше ім'я: "),age = int(input("Введіть ваш вік: "))):
    try:
        if age < 0 or age > 120:
            raise ValueError("Ваш вік не може бути таким.")

    except ValueError as e:
        print(f"Помилка: {e}")

    else:
        print(f"Привіт, {name}! Твій вік — {age}")

    return function

function()



#Завдання 3
numbers = []

try:

    user_input = input("Введіть додатні числа через пробіл: ")
    numbers_str = user_input.split()
    numbers = []
    for x in numbers_str:
        numbers.append(float(x))

    try:
        for num in numbers:
            if num < 0:
                raise ValueError("Знайдено від'ємне значення у списку.")
        result = sum(numbers)
        print(f"Сума всіх чисел у списку: {result}")

    except ValueError as e:
        print(f"Помилка: {e}")

except ValueError:
    print("Помилка: Всі введені значення повинні бути числами.")



#Завдання 4
def sum_positive_numbers(numbers):

   try:
       for num in numbers:
           if num < 0:
               raise ValueError("Знайдено від'ємне значення у списку.")
       return sum(numbers)
   except ValueError as e:
       return f"Помилка: {e}"

try:

    user_input = input("Введіть додатні числа через пробіл: ")
    numbers_str = user_input.split()
    numbers = []
    for x in numbers_str:
        numbers.append(float(x))
    result = sum_positive_numbers(numbers)
    print(f"Сума всіх чисел у списку: {result}")

except ValueError:

   print("Помилка: Всі введені значення повинні бути числами.")