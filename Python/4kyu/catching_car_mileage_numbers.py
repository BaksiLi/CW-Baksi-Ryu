#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Catching Car Mileage Numbers
# https://www.codewars.com/kata/52c4dd683bfd3b434c000292/

import re


def any_cond(n: int, awesome_phrases: list) -> [bool]:
    n_str = str(n)

    all_zeros = any(re.findall(r'^\d0+$', n_str))
    all_same = set(n_str[1:]) == set('0')
    matched_phrases = any(
        re.findall(r'|'.join([str(s) for s in awesome_phrases]), n_str)
    )
    palidronme = n_str == n_str[::-1]
    increment = n_str in '1234567890'
    decrement = n_str in '9876543210'

    cond_list = [
        all_zeros, all_same, matched_phrases, palidronme, decrement, increment
    ]

    return any(cond_list)


def is_interesting(n: int, awesome_phrases: list) -> bool:
    for n, r in zip(range(n, n + 3), (2, 1, 1)):
        if n >= 100 and any_cond(n, awesome_phrases):
            return r
    return 0
