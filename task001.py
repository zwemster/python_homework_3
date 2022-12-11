dividers = []
count = 0
number = int(input('Введи число: '))
for i in range(2, number + 1):
    if number % i == 0:
        for j in range(2, i):
            if i % j == 0:
                count += 1
        if count == 0:
            dividers.append(i)
print(dividers)