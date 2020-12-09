
initial_list = []
n = int(input())  # число целых чисел
degree = int(input())  # степень в которую возводим числа
whole_numbers = ['1', '2', '5', '10']  # список целых чисел
whole_numbers_list = list(map(int, whole_numbers))


def go_to_raising_a_number_to_a_power():
    i = 1
    while True:
        if n >= i:
            number = int(input()) ** degree
            initial_list.append(number)
        else:
            print(initial_list)
            break
        i += 1


def filter_odd_num(in_num):
    return in_num % 2 == 0


def filter_even_num(in_num):
    return in_num % 2 != 0


def filter_prime_num():
    for j in whole_numbers_list:
        for num in range(2, j):
            return j % num == 0


go_to_raising_a_number_to_a_power()
print(list(filter(filter_odd_num, whole_numbers_list)))
print(list(filter(filter_even_num, whole_numbers_list)))
print(list(filter(filter_prime_num, whole_numbers_list)))