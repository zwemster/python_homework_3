accuracy = int(input('До какого знака после запятой вывести число пи? '))
pi = 0
for i in range(0, 20):
    result = (1 / 16) ** i * ((4 / (8 * i + 1)) - (2 / (8 * i + 4)) - (1 / (8 * i + 5)) - (1 / (8 * i + 6)))
    pi += result
print(round(pi, accuracy))
