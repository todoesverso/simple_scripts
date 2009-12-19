#!/usr/bin/env python
# A palindromic number reads the same both ways. The largest palindrome made from
# the product of two 2-digit numbers is 9009 = 91 x 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.

def is_pal(n):
    index_start = 0
    index_end   = len(n) - 1

    while index_end > index_start:
        if n[index_start] != n[index_end]:
            return False

        index_start = index_start + 1
        index_end   = index_end - 1

    return True 

max = 0
n1 = 999
# Won't iterate n1 down to 100, I know the value
# will be found over n1 > 900
while n1 > 900:
    n2 = 999
    while n2 > n1:
        value = n1 * n2
        if is_pal(str(value)):
            if value > max:
                max = value
            break
        n2 -= 1 
    n1 -= 1

print max
