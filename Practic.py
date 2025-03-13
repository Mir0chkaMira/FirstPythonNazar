temperatures = [15,18,20,17,19,22,26,12,15,20]

a = ""
day = 1

for temp in temperatures:
    if temp > 15:
        a = "хороша погода"
    elif temp <= 15:
        a = "прохолодно"

    print(f"{day}. {temp} - {a}")
    day += 1

arfm = sum(temperatures)/len(temperatures)
print(f"Середнє арифметичне тижня: {arfm}")