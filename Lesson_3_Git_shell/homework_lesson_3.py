def go_to_raising_a_number_to_a_power():
    i = 1
    for el in whole_numbers_list:
        if n >= i:
            number = int(input()) ** degree
            initial_list.append(number)
        else:
            print(initial_list)
            break
        i += 1


def go_to_filtration(*args, **kwargs):
    return list(filter(*args, **kwargs))


def filter_odd_num(in_num):
    return in_num % 2 == 0


def filter_even_num(in_num):
    return in_num % 2 != 0


def filter_prime_num():
    for j in whole_numbers_list:
        for num in range(2, j):
            return j % num == 0


if __name__ == "__main__":
    initial_list = []
    n = int(input())  # число целых чисел
    degree = int(input())  # степень в которую возводим числа
    whole_numbers = ['1', '2', '5', '10']  # список целых чисел
    whole_numbers_list = list(map(int, whole_numbers))

    go_to_raising_a_number_to_a_power()
    go_to_filtration(filter_odd_num, whole_numbers_list)
    go_to_filtration(filter_even_num, whole_numbers_list)
    go_to_filtration(filter_prime_num, whole_numbers_list)