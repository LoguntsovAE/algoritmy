def near_zero(lenght, numbers):
    zero_spisok = []
    answer = []
    previous_index = -1
    for index in range(len(numbers)):
        if int(numbers[index]) == 0:
            zero_spisok.append(index)
    print('zero_spisok:', zero_spisok)
    # ФОрмируем первые числа ответа
    answer.append(list(range(1, 3))[::-1])
    # Ставим флаг
    answer.append('flag')

    # ФОрмируем промежуточные числа ответа
    for zero in zero_spisok:
        print('list(range(1, zero - 1))', list(range(1, zero - 1)))
        if zero % 2 == 1:
            print('[zero % 2 + 1]:', [zero % 2 + 1])
        else:
            print('Условие не выполнелось')
        print('list(range(1, zero - 1)', list(range(1, zero - 1)))
        a = list(range(1, zero - 1)) + [zero % 2 + 1] if zero % 2 == 1 else [] + list(range(1, zero - 1)) [::-1]
        answer.append(a)
        
    print('answer:', answer)
    return zero_spisok


if __name__ == '__main__':
    lenght = 5 # int(input())
    numbers = '3 15 0 22 31 32 0 41 0 0 50 0 0 66 0 76 77 82 0 89'.split()
    print(near_zero(lenght, numbers))
    print('right: 2 1 0 1 2 1 0 1 0 0 1 0 0 1 0 1 2 1 0 1')

# def near_zero(lenght, numbers):
#     new_arr = [0] * lenght

#     if numbers[0] != 0:
#         new_arr[0] = lenght

#     for i in range(1, lenght):
#         if numbers[i] == 0:
#             new_arr[i] = 0
#         else:
#             new_arr[i] = new_arr[i-1] + 1
#     for i in range(lenght-2, -1, -1):
#         if numbers[i] == 0:
#             new_arr[i] = 0
#         else:
#             new_arr[i] = min(new_arr[i], new_arr[i+1]+1)
#     return new_arr