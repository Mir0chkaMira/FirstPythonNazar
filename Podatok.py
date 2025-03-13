#Робимо функцію
def total_salary():
    print('Salary Tax Calculator')

    #Даємо користувачу можливість увести варіант
    salary = float(input('Enter gross salary:'))

    #Перевіряємо наскільки велике число
    if salary < 20000:
        tax = 0.18
    else:
        tax = 0.22

    #Підраховуємо ітогову ціну
    net_salary = salary - salary * tax

    print('Net salary:', net_salary)

#Викликаємо функцію
total_salary()
