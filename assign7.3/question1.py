# Exercise 7.3. The mathematician Srinivasa Ramanujan found an infinite series that can be used to
# generate a numerical approximation of 1/π:
# √
# 2 2 ∞ ( 4k ) ! ( 1103 + 26390k )
# 1
# =
# π
# 9801 k ∑
# ( k! ) 4 396 4k
# = 0
# Write a function called estimate_pi that uses this formula to compute and return an estimate of
# π. It should use a while loop to compute terms of the summation until the last term is smaller than
# 1e-15 (which is Python notation for 10 − 15 ). You can check the result by comparing it to math.pi .
# Solution: http: // thinkpython2. com/ code/ pi. py .

import math

def factorial(n):
    if n == 0:
        return 1
    else:
        recurse = factorial(n-1)
        result = n * recurse
        return result

def estimate_pi():
    total = 0
    k = 0
    factor = 2 * math.sqrt(2) / 9801
    while True:
        num = factorial(4*k) * (1103 + 26390*k)
        den = factorial(k)**4 * 396**(4*k)
        total += num / den
        term = factor * num/den
        if abs(term) < 1e-15:
            break
        k += 1
    return 1 / (factor * total)

print(estimate_pi())

# output
# python3 assign7.3/question1.py
# 3.141592653589793
