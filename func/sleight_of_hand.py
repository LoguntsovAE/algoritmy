
from collections import Counter


def result_counter(k, string_numbers):

    return sum(
        True for e, i in Counter(string_numbers).items() if i <= k * 2 and e != '.'
    )


if __name__ == '__main__':

    print('My algoritm', result_counter(
        int(input()),
        input() + input() + input() + input() )
    )
