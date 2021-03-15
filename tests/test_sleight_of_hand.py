#! /usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

# Импорт файла с алгоритмом
from ..func.sleight_of_hand import result_counter


class TestResultCounter(unittest.TestCase):

    print('Тест алгоритма "sleight_of_hands" запущен')

    def test_data_generator(self):
        # Массив: к, строка цифр, правильный ответ
        test_data = (
            (3, "12312..22..22..2", 2),
            (4, "1111999911119911", 1),
            (4, "1111111111111111", 0),
            (4, "................", 0),
            (1, "1999543643681712", 7),
            (2, "1555.2564236595.", 6),
            (4, "2941.2873798.221", 7),
            (5, "55982666427.7645", 7),
            (3, "884443.922474.48", 6),
            (5, "2.1888644959.668", 7),
            (5, "9147.81153444142", 8),
            (5, "659.87.132868447", 9),
            (2, "878674574.398919", 8),
            (2, "3152396819185289", 7),
            (1, "229349124836745.", 7),
            (1, "2.892994894663..", 5),
            (3, "6.76541557377794", 7),
            (2, "8812978494667565", 8),
            (1, "8177532166338213", 5),
            (3, "5752681558577113", 7),
            (4, "4147.524..368581", 8),
        )

        for i in range(len(test_data)):

            # Получаем входные данные и правильный ответ из массива
            k = test_data[i][0]
            numbers = test_data[i][1]
            answer = test_data[i][2]

            # Получаем результат работы алгоритма
            # sleight_of_hand - название файла с алгоритмом
            # result_counter - название метода
            algoritm_answer = result_counter(k, numbers)

            error_mesage = ("При k = {} В строке: {}, правильный ответ = {}!!!"
                            "Но результат алгоритма = {}"
                            )
            self.assertEqual(
                algoritm_answer,
                answer,
                error_mesage.format(k, numbers, answer, algoritm_answer)
            )


if __name__ == "__main__":
    unittest.main()
