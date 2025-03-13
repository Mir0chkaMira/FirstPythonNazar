#Робимо функію
def avarage_grade_calculator():
    print('Average Grade Calculator')

    #Створюємо порожній список
    grades = []

    #Створюємо цикл
    while True:

        #Даємо користувачу можливість увести варіант або зупинити
        grade = input('Enter grade (or "stop"):')

        #Перевіряємо вибір користувача
        if grade == 'stop':
            break

        grades.append(float(grade))

        avarage_grade = float(sum(grades)/len(grades))

        print('Average grade:',avarage_grade)

        #Перевіряємо наскільки велике число
        if avarage_grade >= 90:
            print('Excellent')
        elif avarage_grade >= 75:
            print('Good')
        else:
            print('Needs Improvement')

#Викликаємо функцію
avarage_grade_calculator()