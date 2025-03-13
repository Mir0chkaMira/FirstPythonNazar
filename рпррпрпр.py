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