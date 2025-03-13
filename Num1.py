books = ["абетка", "казки", "енеїда", "лісова пісня"]

a = input("Введіть назву книги для пошуку: ").lower()

for book in books:
    if book == a:
        print("Така книга є.")
        break
if book != a:
    print("Такої книги немає")
