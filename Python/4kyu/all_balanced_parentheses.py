#!/usr/bin/env python
# -*- coding: utf-8 -*-

# All Balanced Parentheses
# https://www.codewars.com/kata/5426d7a2c2c7784365000783/

# N=2*n being the length of the resulting string,
# so there are n*'(' and n*')'. For the i-th char to be
# '(', there should be more ')' than '(', and vice versa.


def balanced_parens(n: int) -> [str]:
    def next_paren(
        n: int, s: str = '', n_left: int = 0, n_right: int = 0
    ) -> str:
        if n_right < n:
            if n_left < n:
                next_paren(n, s + '(', n_left + 1, n_right)

            if n_left > n_right:
                next_paren(n, s + ')', n_left, n_right + 1)

        else:
            possibility.append(s)

    possibility = []
    next_paren(n)

    return possibility


def balanced_parens2(n: int) -> [str]:
    pass
