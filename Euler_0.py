"""
A number is a perfect square, or a square number, if it is the square of a positive integer.
For example, 25 is a square number because 5 * 5 = 25; it is also an odd square.

The first 5 square numbers are: 1, 4, 9, 16, 25, and the sum of the odd squares is 35.

Among the first 560 thousand square numbers, what is the sum of all the odd squares?
"""

import math

if __name__ == "__main__":
    n = 560000
    sum_of_odd_squares = 0

    for i in range(1, n + 1):
        square = i * i
        if square % 2 != 0:  # Check if the square is odd
            sum_of_odd_squares += square

    print(sum_of_odd_squares)