#!/usr/bin/env python
# 2520 is the smallest number that can be divided by each of the numbers from 1
# to 10 without any remainder.
#
# What is the smallest number that is evenly divisible by all of the numbers from
# 1 to 20?

def iter(x):
    for i in range(1,20):
        if x%i == 0:
           continue 
        else:
            return False
    return True

# Condition 1: X/20 = n20
# Condition 2: X/19 = n19
# Minimun X would be 20 for the first condition therefore
# 20/20 = n20 = 1 
# But now I have a new condition 
# Condition 3: n20/19 = int
# Therefore n20 = 19. So from the first contition we see that
# X/20 = n20 and n20 must be at least 19 so 
# X = 20 * n20 = 380. This contition will be always true
# so we cant start the iteration assuming that 
# X = 380
# This will be true for the first two contitions, and as it 
# will be always true we can iterate X by an increment of 380

val = 380

while True:
    if iter(val):
       break 
    else:
       val += 380

print val
