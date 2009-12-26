#!/usr/bin/env python
#
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a^(2) + b^(2) = c^(2)
#
# For example, 3^(2) + 4^(2) = 9 + 16 = 25 = 5^(2).
# 
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

# From simple math we see:
# a + b + sqrt(a^(2) + b^(2)) = 1000

for a in range(333):
    for b in range(a,999):
        c = ((a**2)+(b**2))**0.5
        if a+b+c == 1000:
            print a*b*c
            break


