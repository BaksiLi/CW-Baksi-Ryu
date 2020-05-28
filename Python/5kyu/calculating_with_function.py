#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Calculating with Functions
# https://www.codewars.com/kata/525f3eda17c7cd9f9e000b39

import operator as op

op_curried = lambda f: lambda y: lambda x: f(x, y)

plus = op_curried(op.add)
minus = op_curried(op.sub)
times = op_curried(op.mul)
divided_by = op_curried(op.floordiv)
id_ = lambda x: x

number = lambda x: lambda f=id_: f(x)
zero, one, two, three, four, five, six, seven, eight, nine = map(number, range(10))

# ------------------ #
# Test.describe('Basic Tests')
# Test.assert_equals(seven(times(five())), 35)
# Test.assert_equals(four(plus(nine())), 13)
# Test.assert_equals(eight(minus(three())), 5)
# Test.assert_equals(six(divided_by(two())), 3)

# Test.describe('Random Tests')
# from random import randint
# base=["zero","one","two","three","four","five","six","seven","eight","nine"]
# basef=[zero,one,two,three,four,five,six,seven,eight,nine]

# for _ in range(40):
#     a,b=randint(0,9),randint(0,9)
#     Test.it("Testing for %s(plus(%s()))" %(base[a],base[b]))
#     Test.assert_equals(basef[a](plus(basef[b]())), a+b)
#     a,b=randint(0,9),randint(0,9)
#     Test.it("Testing for %s(minus(%s()))" %(base[a],base[b]))
#     Test.assert_equals(basef[a](minus(basef[b]())), a-b)
#     a,b=randint(0,9),randint(0,9)
#     Test.it("Testing for %s(times(%s()))" %(base[a],base[b]))
#     Test.assert_equals(basef[a](times(basef[b]())), a*b)
#     a,b=randint(0,9),randint(1,9)
#     Test.it("Testing for %s(divided_by(%s()))" %(base[a],base[b]))
#     Test.assert_equals(basef[a](divided_by(basef[b]())), a//b)
