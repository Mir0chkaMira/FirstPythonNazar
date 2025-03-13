#Робимо функцію
def todo():
    print('To-Do List')

    #Створюємо порожній список
    tasks = []

    #Створюємо цикл
    while True:

         #Даємо користувачу можливість обрати
         action = input('Choose: "add", "done", "view", "exit":')

         #Перевіряємо вибір користувача
         if action == 'exit':
             break
         if action == 'add':
             task=input('Enter task:')
             tasks.append((task,False))
         elif action == 'done':
             number_of_task = int(input('Task number to mark done:'))
             tasks[number_of_task] = tasks[number_of_task][0],True
         elif action == 'view':
             print('Your tasks: ')

         for i,t in enumerate(tasks):
             print(i,t[0],'- Done' if t[1] else '- Not Done')

#Викликаємо функцію
todo()

