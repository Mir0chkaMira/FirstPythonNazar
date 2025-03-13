num_list = input("Введіть цілі числа через пробіл: ").split()

max_value = max(num_list)
min_value = min(num_list)
max_index = num_list.index(max_value)
min_index = num_list.index(min_value)

print(f"Найбільше значення: {max_value}, його індекс: {max_index}")
print(f"Найменше значення: {min_value}, його індекс: {min_index}")

