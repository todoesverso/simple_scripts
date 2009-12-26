#!/usr/bin/env python
# 2^(15) = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#
# What is the sum of the digits of the number 2^(1000)?

number = 2**1000
# Convert to string to make it iterable
str_num = str(number)
sum = 0 

for i in str_num:
    sum += int(i)

print sum 

