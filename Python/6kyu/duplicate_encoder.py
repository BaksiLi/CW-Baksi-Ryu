#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Duplicate Encoder
# https://www.codewars.com/kata/54b42f9314d9229fd6000d9c

def duplicate_encode(word: str) -> str:
    word = word.lower()
    return ''.join(['(' if word.count(c) == 1 else ')' for c in word])
