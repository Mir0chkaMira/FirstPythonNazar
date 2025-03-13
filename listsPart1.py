from random import *
import time

word_list = ["Камень", "Ножиці", "Бумага", "Ящірка", "Спок"]

bot_score = 0
player_score = 0

user_choise = ""


print("Гра КаменьНожиціБумага\n")

while True:
    user_choise = input("Оберіть предмет (К,Н,Б,Я,С): ").upper()
    bot_choice = choice(word_list)

    print(f"Ваш вибір - {user_choise} : {bot_choice} - вибір бота")
    print("Та переможцем є....\n")
    time.sleep(1)
    if user_choise == bot_choice[0]:
        print("Нечія >:)")
    elif user_choise == "К" and bot_choice == "Бумага":
        print("Бот!")
        bot_score += 1
    elif user_choise == "К" and bot_choice == "Ножиці":
        print("Ви!")
        bot_score += 1
    elif user_choise == "Н" and bot_choice == "Камень":
        print("Бот!")
        bot_score += 1
    elif user_choise == "Н" and bot_choice == "Бумага":
        print("Ви!")
        bot_score += 1
    elif user_choise == "Б" and bot_choice == "Ножиці":
        print("Бот!")
        bot_score += 1
    elif user_choise == "Б" and bot_choice == "Камень":
        print("Ви!")
        bot_score += 1
    elif user_choise == "Я" and bot_choice == "Ножиці":
        print("Ви!")
        bot_score += 1
    elif user_choise == "Я" and bot_choice == "Камень":
        print("Ви!")
        bot_score += 1
    elif user_choise == "Я" and bot_choice == "Бумага":
        print("Бот!")
        bot_score += 1
    elif user_choise == "Я" and bot_choice == "Спок":
        print("Бот!")
        bot_score += 1
    elif user_choise == "С" and bot_choice == "Ножиці":
        print("Бот!")
        bot_score += 1
    elif user_choise == "С" and bot_choice == "Камень":
        print("Бот!")
        bot_score += 1
    elif user_choise == "С" and bot_choice == "Бумага":
        print("Бот!")
        bot_score += 1
    elif user_choise == "С" and bot_choice == "Ящірка":
        print("Ви!")
        bot_score += 1

    if bot_score == 5:
        print("Бот переміг >:)")

        yes_or_no = input("Чи ви хочете продовжити грати? Т/Н : ").upper()

        if yes_or_no == "Т":
            player_score = 0
            bot_score = 0
            continue
        else:
            print("Було гарно з вами пограти! :>")
            break

    if player_score == 5:

        print("Ви перемогли! :D")

        yes_or_no = input("Чи ви хочете продовжити грати? Т/Н : ").upper()

        if yes_or_no == "Т":
            player_score = 0
            bot_score = 0
            continue
        else:
            print("Було гарно з вами пограти! :>")
            break