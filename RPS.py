#Підключаємо бібліотеку
import random

#Робимо функцію
def rps():
    print('welcome to rps game')
    user_score_count = 0
    computer_score_count = 0

    #Створюємо цикл
    while True:
        print('choose: 1-rock 2-paper 3-scissors')
        user = input('your choice:')

        #Вибір гравця
        if user not in ['1','2','3']:
            print('invalid choice try again')
            continue
        computer = random.choice(['1','2','3'])

        print('computer:',computer)

        #Перевірка вибору гравця
        if user == computer:
           print('draw')
        elif (user == '1' and computer == '3') or (user == '2' and computer == '1') or (user == '3' and computer == '2'):
            print('you win')
            user_score_count+=1
        else:
         print('you lose')
         computer_score_count+=1

        #Кількість балів та пропонування грати знову
        print('score: you:',user_score_count,'comp:',computer_score_count)
        print('play again? y/n')
        again = input()

        if again!='y':
         print('final score: you:',user_score_count,'comp:',computer_score_count)
         print('bye!')
         break

#Викликаємо функцію
rps()
