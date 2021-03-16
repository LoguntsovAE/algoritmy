#! /usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import timeit

import pytest

# Импорт файла с алгоритмом
from ..func.near_zero import near_zero


@pytest.mark.parametrize(
    'numbers, expected',
    (
            ([0, 1, 4, 9, 0], [0, 1, 2, 1, 0]),
            ([0, 7, 9, 4, 8, 20], [0, 1, 2, 3, 4, 5]),
            ([0, 1, 4, 9, 0], [0, 1, 2, 1, 0]),
            ([98, 0, 10, 77, 0, 59, 28, 0, 94], [1, 0, 1, 1, 0, 1, 1, 0, 1]),
            ([99, 0, 100, 72, 43, 49, 0, 51, 19, 61, 93, 31], [1, 0, 1, 2, 2, 1, 0, 1, 2, 3, 4, 5]),
            ([64, 68, 37, 11, 77, 80, 48, 82, 0], [8, 7, 6, 5, 4, 3, 2, 1, 0]),
            ([0, 3, 41, 0, 0, 0, 0, 0, 49, 0, 0, 56, 0, 88], [0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1]),
            ([0, 0, 20, 0, 0, 0, 0, 40, 0, 0, 65, 73, 77, 0, 79, 0, 82, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 2, 1, 0, 1, 0, 1, 0, 0, 0]),
            ([5, 8, 9, 12, 15, 26, 30, 0, 0, 55, 0, 0, 67, 0, 76, 80, 82, 0, 0, 98], [7, 6, 5, 4, 3, 2, 1, 0, 0, 1, 0, 0, 1, 0, 1, 2, 1, 0, 0, 1]),
            ([10, 13, 31, 35, 39, 0, 0, 59, 0, 66, 68, 73, 74, 0, 0, 0, 87, 89, 96, 99], [5, 4, 3, 2, 1, 0, 0, 1, 0, 1, 2, 2, 1, 0, 0, 0, 1, 2, 3, 4]),
            ([3, 15, 0, 22, 31, 32, 0, 41, 0, 0, 50, 0, 0, 66, 0, 76, 77, 82, 0, 89], [2, 1, 0, 1, 2, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 2, 1, 0, 1]),
            ([0, 152871953, 35758611, 0, 23446050, 761817124, 672461861, 39089193, 0, 0, 188187704, 70952507, 0, 940207165, 444534846, 414873160, 164274761, 858907213, 703483471, 385149009, 0, 951784545, 0, 0, 429548140, 437438577, 945148040, 847574158, 245872275, 686676631, 260948138, 220055723, 394760373, 608300732, 279782591, 507679937, 0, 437680330, 268329165, 0, 526207708, 383613661, 675427551, 1897698, 195749095, 614799594, 453061364, 447724793, 262574330, 142751994, 0, 982802179, 743490824, 761200905, 765521674, 589838606, 779130650, 489999132, 614469924, 534675750, 795652391, 532818235, 0, 7462720, 796842821, 987969359, 0, 820963159, 0, 639387490, 729833831, 725754736, 559672176, 265743221, 506640772, 0, 727270808, 849485724, 679340445, 857923486, 351773599, 231748526, 620691377, 753766836, 684745656, 522743742, 168625601, 821831113, 900417993, 894851534, 0, 553949137, 692702162, 0, 299571161, 94853602, 215074276, 62820842, 0, 404316147], [0, 1, 1, 0, 1, 2, 2, 1, 0, 0, 1, 1, 0, 1, 2, 3, 4, 3, 2, 1, 0, 1, 0, 0, 1, 2, 3, 4, 5, 6, 6, 5, 4, 3, 2, 1, 0, 1, 1, 0, 1, 2, 3, 4, 5, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 0, 1, 2, 1, 0, 1, 0, 1, 2, 3, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 7, 6, 5, 4, 3, 2, 1, 0, 1, 1, 0, 1, 2, 2, 1, 0, 1]),
            ([453711875, 549231112, 912076297, 728440337, 860232213, 322653209, 595801117, 131964447, 791407655, 609482791, 273008693, 254099001, 151722051, 529828428, 0, 390815834, 897204836, 424688243, 579298440, 478242441, 902418060, 691973261, 270165665, 895559842, 518829753, 823401147, 979741378, 312390349, 343285456, 985809106, 593765082, 71373021, 565784798, 285728478, 723175133, 486400741, 432401639, 685025521, 211914482, 473690361, 373750524, 862995200, 617452294, 165581579, 2755862, 493630230, 31744281, 976295195, 607670044, 71142175, 765716256, 538166053, 435577128, 675496237, 604298033, 151483194, 81099067, 454522683, 881482563, 464874309, 330614599, 717462344, 481418070, 0, 177763673, 120525148, 558441830, 958049644, 841846639, 428930419, 382281077, 977823099, 820120446, 405528454, 242160011, 816726924, 143926672, 160348052, 178267038, 792557476, 30897064, 294090152, 348437423, 366211509, 342114231, 340238782, 442921409, 7987654, 569753033, 521263055, 618353106, 344185810, 505109467, 904851934, 769808356, 443824105, 900135920, 42350064, 399316990, 0], [14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]),
            ([0], [0]),
    )
)
def test_nearest_zero(numbers, expected):
    # assert near_zero(len(numbers), numbers) == expected

    def func():
        near_zero(len(numbers), numbers)
    logging.info('Timeit: {}'.format(timeit.timeit(func, number=100000)))
