#Робимо функцію
def test_results():

    print("Test Results System")

    #Створюємо змінні до подальшого використування
    total = 0
    students_that_passed = 0
    students_that_failed = 0

    #Створюємо цикл
    while True:

        #Даємо користувачу можливість обрати
        results = input("Enter 'pass' for students_that_passed, 'fail' for students_that_failed, or 'end' to stop:")

        #Перевіряємо вибір користувача
        if results == "end":
            break
        if results == "pass":
            students_that_passed+=1
            total+=1
        elif results == "fail":
            students_that_failed+=1
            total+=1
        else:
            print("Invalid input, try again!")

    #Виводимо на екрані результати
    print("Total Students:",total)
    print("Passed Students:",students_that_passed)
    print("Failed Students:",students_that_failed)
    print("Pass Percentage:",students_that_passed/total*100 if total>0 else 0)

#Викликаємо функцію
test_results()