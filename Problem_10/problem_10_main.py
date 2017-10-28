import itertools

# Author John Nilsson, 2017-10-28

#
# Question 10:
#
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

# primes = [2]
# for i in range(2, 100001):
#     if all((i+1) % count for count in range(2, i)):
#         primes.append(i+1)
#
# print(primes)

def erat2():
    D = {}
    yield 2
    for q in itertools.islice(itertools.count(3), 0, None, 2):
        p = D.pop(q, None)
        if p is None:
            D[q*q] = q
            yield q
        else:
            x = p + q
            while x in D or not (x&1):
                x += p
            D[x] = p

def get_primes_erat(n):
  return list(itertools.takewhile(lambda p: p<n, erat2()))

print(sum(get_primes_erat(2000000)))