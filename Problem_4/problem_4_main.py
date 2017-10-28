# Author: John Nilsson, 2017-10-28

# Question (Problem 4)

# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is
# 9009 = 91 × 99. Find the largest palindrome made from the product of two 3-digit numbers.


# --- Solution ---

class Palindrom(object):

    # Initializing class
    def __init__(self, number):
        self.n = number

    # Reversing integer
    def reverse_int(self):
        return int(str(self.n)[::-1])

    # Return delta between numbers
    def delta_int(self):
        n_rev = self.reverse_int()
        return self.n - n_rev

palins = []
for i in range(999):
    for j in range(999):
        product = i * j
        if Palindrom(product).delta_int() == 0:
            palins.append(product)

largest_palin = max(palins)
print(largest_palin)



