spending = [30, 0, 4302, 10, 0, 5324, 0, 300, 2341, 678]

spd0 = 0
spd1000 = 0

for spend in spending:
    if spend == 0:
        spd0 += 1
    if spend >= 1000:
        spd1000 += 1

sum = sum(spending)

print(f"Кількість днів з витратами 0: {spd0}")
print(f"Кількість днів з витратами 1000 та більше: {spd1000}")
print(f"Сума витрат: {sum}")