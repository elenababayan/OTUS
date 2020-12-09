
initial_list = []
n = int(input())  # число целых чисел
degree = int(input())  # степень в которую возводим числа
whole_numbers = []  # список целых чисел


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


def go_to_creating_different_lists():
    for j in range(len(whole_numbers)):
        if whole_numbers[j] % 2 == 0:
            print(whole_numbers[j])
        else:
            continue

    for j in range(len(whole_numbers)):
        if whole_numbers[j] % 2 != 0:
            print(whole_numbers[j])
        else:
            continue

    for j in range(len(whole_numbers)):
        for num in range(2, j):
            if whole_numbers[j] % num != 0:
                print(whole_numbers[j])
            else:
                continue