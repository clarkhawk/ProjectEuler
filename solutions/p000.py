#   SPDX-License-identifier: MIT
#   Problem Euler, problem 0 (introductory problem, values randomised per visitor)
#   https://projecteuler.net/register
#
#   Approach:the k-th square is odd iff k is odd. Sum the squares of the
#   odd integers up to n with the closed form m(2m-1)(2m+1)/3, m = ceil(n/2).
#   A brute-force version is kept to cross-check the formula.