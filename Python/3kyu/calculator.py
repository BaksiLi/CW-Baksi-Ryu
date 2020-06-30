#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Calculator
# https://www.codewars.com/kata/5235c913397cbf2508000048/

import re

operators = dict(zip('+-*/',
                     (float.__add__,
                      float.__sub__,
                      float.__mul__,
                      float.__truediv__)))


def calculate(expr: str) -> float:
    """Evluates infix expression.
    """
    global operators

    try:
        return float(expr)

    except ValueError:
        # Brackets
        while '(' in expr:
            expr = re.sub(
                r'\((-?\d[\d\.]*)( ([\+\-\*\/]) (-?\d[\d\.]*))+\)',
                lambda m: str(calculate(m.group(0).strip('()'))), expr
            )

        # */
        while ' * ' in expr or ' / ' in expr:
            expr = re.sub(r'(-?\d[\d\.]*) ([\*\/]) (-?\d[\d\.]*)',
                          lambda m: str(operators[m.group(2)](float(m.group(1)),
                                                              float(m.group(3)))),
                          expr)

        # +-, left-to-right
        subexpr = re.match(r'(-?\d[\d\.]*) ([\+\-]) (-?\d[\d\.]*)+', expr)
        if subexpr:
            expr = expr.replace(
                subexpr.group(0),
                str(
                    operators[subexpr.group(2)](
                        float(subexpr.group(1)), float(subexpr.group(3))
                    )
                )
            )

        return calculate(expr)


class Calculator():
    def evaluate(self, expr):
        return calculate(expr)
