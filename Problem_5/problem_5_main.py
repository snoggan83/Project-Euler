# Author: John Nilsson, 2017-10-28

# Question 5:
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

# Initializing
count = 20
while not all(not count % integer for integer in range(1, 21)):
    count += 20
