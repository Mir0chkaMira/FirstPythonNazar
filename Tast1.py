#Завдання 1
def text():
    print("\"Dont let the noise of others opinions drown out your own inner voice.\"Steve Jobs")

text()


#Завдання 2
def nums(num1=int(input("Введіть перше число: ")), num2=int(input("Введіть друге число: "))):
    for i in range(num1, num2):
        if i % 2 == 1:
            print (i)
    print(nums)

nums()


#Задвання 3
def line(weth=int(input("Ведіть довжину лінії: ")), lenth=input("Введіть тип лінії(верт\гориз): ".lower())):
    if lenth == "верт":
        print("|\n"*weth)
    elif lenth == "гориз":
        print("_"*weth)
    print(line)

line()


#Завдання 4
def fournums(num1, num2, num3, num4):
    maxnum = max(num1, num2, num3, num4)
    print(f"Найбільше число: {maxnum}")
    print(fournums)

fournums(7, 10, 3, 5)


#Завдання 5
def fer(num1=int(input("Введіть температуру у градусах: "))):
    feren = (num1 - 32)/1.8
    print("Цельсія у ференгейтах: ", feren)
    print(fer)

fer()


#Завдання 6
def hour(num1=int(input("Введіть години: "))):
    if num1 < 1 or num1 > 24:
        print("Це не дуже то й година")
    else:
        if num1 > 9 and num1 < 18:
            print("Цей час є робочим.")
        else:
            print("Цей час не є робочим.")
    print(hour)

hour()


#Завдання 7
def mint(num1=int(input("Введіть кількість хвилин: "))):
    if num1 > 0:
        hours = num1 / 60
        print("Годин з цих хвилин: ", hours)
    else:
        print("Ти як у минуле попав?")
    print(mint)

mint()


#Завдання 8
def sixnum(num1):

    if sum1 == sum2:
        print("Це число є щасливим.")
    else:
        print("Це число не є щасливим.")
    print(sixnum)




#Завдання 10
#def lists(num1=[5, 3, 4, 10]):