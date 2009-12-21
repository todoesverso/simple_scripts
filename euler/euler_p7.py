#!/usr/bin/env python
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that
# the 6^(th) prime is 13.
#
# What is the 10001^(st) prime number?

# I know that the 26th prime number is 101
# and all prime numbers are odd
number = 103 
count  = 26

def is_prime(n):
    '''check if n is prime'''

    n = abs(int(n))

    if not n & 1:
        return False

    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

while True:
    if is_prime(number):
        count += 1
        if count == 10001:
            print number
            break
    number += 2
