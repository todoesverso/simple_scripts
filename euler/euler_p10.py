#!/usr/bin/env python
#
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.

number = 600851475143

def is_prime(n):
    '''check if n is prime'''

    n = abs(int(n))

    if n < 2:
        return False

    if n == 2: 
        return True  
  
    if not n & 1: 
        return False

    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False

    return True

sum = 0

for i in range(2000000):
    if is_prime(i):
        sum += i

print sum
