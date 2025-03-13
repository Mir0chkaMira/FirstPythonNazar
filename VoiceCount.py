#Робимо функцію
def vote():
    print('Voting System')

    count_of_1 = 0
    count_of_2 = 0
    count_of_3 = 0

    #Створюємо цикл
    while True:

        #Даємо користувачу можливість проголосувати
        voting = input('Vote for 1, 2, or 3 (or "stop" to end): ')

        #Перевіряємо відповідь користувача
        if voting == 'stop':
            break
        if voting == '1':
            count_of_1+=1
        elif voting == '2':
            count_of_2+=1
        elif voting == '3':
            count_of_3+=1
        else:
            print('Invalid vote!')

    #Виводимо на екран результат
    print('Results:')
    print('1: ', count_of_1)
    print('2: ', count_of_2)
    print('3: ', count_of_3)

#Викликаємо функцію
vote()