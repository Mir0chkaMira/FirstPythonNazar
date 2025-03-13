#Робимо функію
def shopping_calculator():
    print('Shopping Calculator')

    #Створюємо порожній список
    list_of_products = []

    #Створюємо цикл
    while True:

        #Даємо користувачу можливість увести варіант або зупинити
        product_name = input('Enter product name or "done":')

        #Перевіряємо вибір користувача
        if product_name == 'done':
         break

        cost_of_product = float(input('Enter price:'))

        list_of_products.append((product_name, cost_of_product))

        total_price = 0

        print('Your products:')

        #Рахуємо та виводимо на екран повну ціну
        for i in list_of_products:
            print(i[0],' - ',i[1])

            total_price+=i[1]

            print('Total:',total_price)

#Викликаємо функцію
shopping_calculator()

