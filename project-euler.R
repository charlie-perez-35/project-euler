# New R file

library(tidyverse)

# 1. If we list all the natural numbers below 10 that are multiples of 3 or 5,
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

x = 0
for (a in 1:1000) {
  if (a %% 3 == 0 || a %% 5 == 0) {
  x = x+a
  }
}
cat("Euler 1 answer: Sum = " , x, "\n")

# 2. By considering the terms in the Fibonacci sequence whose values do not exceed 
# four million, find the sum of the even-valued terms.

b <- list(0, 1)
index <- 1
while (b[index] < 4000000) {
  index2 <- index + 1
  d <- as.numeric(b[index]) + as.numeric(b[index2])
  b <- c(d, index2+1)
  index = index+1
}
cat(b)
# problem seems to be with concatenating to list
e = 0
for each in b:
  if each < 4000000 and each % 2 == 0:
  e += each

print("Euler 2 answer: Sum = " + str(e) + "\n")

# e = 4613732