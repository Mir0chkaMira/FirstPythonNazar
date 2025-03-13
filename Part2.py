#Частина 2
#Завдання 1
a = input("Введіть арифметичний вираз (число операція число): ")

print(eval(a))

#Завдання 2
num_list = [1, 0, -6, 12, -13, 0, 2, 7, 8, -5, 0]

count1 = 0
count2 = 0
count3 = 0

min_num = min(num_list)
max_num = max(num_list)
print("Максимальне число: ", max_num)
print("Мінімальне число: ", min_num)

for num in num_list:
    if num < 0:
        count1 += 1
    elif num > 0:
        count2 += 1
    elif num == 0:
        count3 += 1

print("Кількість від'ємних чисел: ", count1)
print("Кількість додатніх чисел: ", count2)
print("Кількість нулів: ", count3)
