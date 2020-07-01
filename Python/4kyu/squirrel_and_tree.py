#!/usr/bin/env python
# -*- coding: utf-8 -*-

# One Line Task: Squirrel And Tree
# https://www.codewars.com/kata/59016379ee5456d8cc00000f/

# Cartesian coordinate
# $x = r \times cos(\theta) = (S / 2 \pi) * cos(2\pi \times T/t)$
# we are interested in the arc length, so integrate sqrt of x y z over T
# and times H/h, so we have $\sqrt{S^2+h^2}\frac{H}{h}$
# $ = H\sqrt{\frac{S^2}{h^2}+1} = H * \|j+S/H\|$

squirrel=lambda h,H,S:round(H*abs(1j+S/h),4)
