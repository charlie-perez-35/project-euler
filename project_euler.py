# 1. If we list all the natural numbers below 10 that are multiples of 3 or 5,
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

x = 0
for a in range (1,1000):
    if a % 3 == 0 or a % 5 == 0:
        x += a

print("Euler 1 answer: Sum = " + str(x) + "\n")

# x = 233168

# 2. By considering the terms in the Fibonacci sequence whose values do not exceed 
# four million, find the sum of the even-valued terms.

b = [0, 1]
c = 1
while b[c] < 4000000:
    d = b[c-1] + b[c]
    b.append(d)
    c += 1

e = 0
for each in b:
    if each < 4000000 and each % 2 == 0:
        e += each

print("Euler 2 answer: Sum = " + str(e) + "\n")

# e = 4613732

# 3. What is the largest prime factor of the number 600851475143?

# can't.