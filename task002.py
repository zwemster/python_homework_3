from random import randint

list_size = int(input('Сколько чисел будет в списке? '))
rand_list = [randint(0, 10) for i in range(list_size)]
print(f'{rand_list} - исходный список')
sort_rand_list = sorted(rand_list)
uniq_rand_list = []
for i in sort_rand_list:
    if i not in uniq_rand_list:
        uniq_rand_list.append(i)
print(f'{uniq_rand_list} - список неповторяющихся элементов исходного списка')