#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Evaluating prefix Polish notation
# https://www.codewars.com/kata/5e5b7f55c2e8ae0016f42339

import re

operators = dict(zip('+-*/',
                     (float.__add__,
                      float.__sub__,
                      float.__mul__,
                      float.__truediv__)))


def calculate(expr: str) -> float:
    """Evaluates prefix expression using stack.
    """
    global operators
    stack = []

    for atom in reversed(expr.split()):
        if atom in operators:
            stack.append(operators[atom](stack.pop(), stack.pop()))
        else:
            stack.append(float(atom))

    return stack.pop()


def calculate2(expr: str) -> float:
    """Evaluates prefix expression using regex parser.
    """
    global operators

    while ' ' in expr:
        expr = re.sub(r'([\+\-\*\/]) (-?\d[0-9\.\+\-]*) (-?\d[0-9\.\+\-]*)',
                      lambda m: str(operators[m.group(1)](float(m.group(2)),
                                                          float(m.group(3)))),
                      expr)

    return float(expr)
