#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Sudoku Solution Validator
# https://www.codewars.com/kata/529bf0e9bdf7657179000008/


def valid_solution(board):
    blocks = [[board[i][j] for i in range(k, k+3) for j in range(k, k+3)]
              for k in range(0, 9, 3)]
    return all(map(lambda xs: sum(xs) == 45,
                   board +  # x-axis
                   list(map(list, zip(*board))) +  # y-axis
                   blocks  # blocks
                   ))


def valid_solution2(board):
    sum_to_45 = lambda xs: sum(xs) == 45
    return (
        all(board[i][j] != 0 for i in range(9)
            for j in range(9)) and  # no zeros
        all([sum_to_45(board[i]) for i in range(9)]) and  # x-axis
        all([sum_to_45([board[i][j] for i in range(9)])
             for j in range(9)]) and  # y-axis
        all([sum_to_45([
                board[i][j] for i in range(k, k + 3) for j in range(k, k + 3)
            ]) for k in range(0, 9, 3)])  # blocks
    )
# You know what, fuck readability ;)
