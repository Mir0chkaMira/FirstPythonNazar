#Частина 1
#Завдання 1

a = input("Введіть речення - паліндром: ")

a = a.replace(" ","")
a = a.upper()

if a == a[::-1]:
 print("Введений рядок є паліндромом")
else:
 print("Введений рядок не є паліндромом")

#Завдання 2
text = input("Введіть текст: ")
reserved_words = input("Введіть список зарезервованих слів (через кому): ").split(',')

for word in reserved_words:
   text = text.replace(word, word.title())
print(text)

#Завдання 3
text = input("Введіть текст: ")

num_sentences = text.count('.') + text.count('!') + text.count('?')
print(f"Кількість речень у тексті: {num_sentences}")
