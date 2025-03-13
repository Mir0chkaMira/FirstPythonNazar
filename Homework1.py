#Завдання 1
def text():
    print("\"Don't compare yourself with anyone in this world…\nif you do so, you are insulting yourself.\"\nBill Gates" )

text()

#Завдання 2
def numbers(num1=int(input("Введіть перше число: ")), num2=int(input("Введіть друге число: "))):
    for i in range(num1, num2):
        if i % 2 == 0:
            print(i)

numbers()

#Завдання 3
#def squere(length=int(input("Введіть довжину сторони: ")), symb=int(input("Введіть символ: ")), fill=input("Заповнений або ні: ").lower()):
def square(length, symbol, filled):
    for i in range(length):
        for j in range(length):
            if filled or i == 0 or j == 0 or i == length - 1 or j == length - 1:
                print(symbol, end=' ')
            else:
                print(' ', end=' ')
        print()
    return

square(6, '%', True)

#Завдання 4
def fournums(num1, num2, num3, num4):
    maxnum = min(num1, num2, num3, num4)
    print(f"Найменше число: {maxnum}")
    print(fournums)

fournums(4, 13, 8, 1)

#Завдання 5
def mul(start, end):
   multiply = 1
   if end < start:
       center = start
       center2 = end
       end = center
       start = center2

   for num in range(start, end + 1):
        multiply *= num
        print(multiply)
   return multiply

mul(2, 14)

#Завдяння 6
def numlen(num1=int(input("Введіть число:"))):
    lenum = len(str(num1))
    print(lenum)

numlen()

#Завдяння 7
def pol():

    a = input("Введіть число - паліндром: ")

    if a == a[::-1]:
        while True:
             print("Введений рядок є паліндромом")
             return
    else:
        print("Введений рядок не є паліндромом")

pol()