#!/usr/bin/env python
# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?

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


# As I saw that most of the result fall in the 1% of the number
# just reduce a litlle bit the calculations 
i = number/10000000
i = abs(int(i))

while 1:
    i = i - 2
    val = number % i
    if is_prime(i) and val == 0:
        break

print ("The result is %(res)s")% {'res': i}
