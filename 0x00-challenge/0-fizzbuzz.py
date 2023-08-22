#!/usr/bin/python3
""" FizzBuzz """
import sys


def fizzbuzz(n):
    """
    The FizzBuzz function outputs a sequence of numbers from 1 to n,
    with each number separated by a space. However, there are certain conditions:

    If a number is a multiple of three, it is replaced with the word "Fizz".
    If a number is a multiple of five, it is replaced with the word "Buzz".
    If a number is a multiple of both three and five, it is replaced with the phrase "FizzBuzz".
    """
    if n < 1:
        return

    result = []
    for i in range(1, n + 1):
        if (i % 3) == 0 and (i % 5) == 0:
            result.append("FizzBuzz")
        elif (i % 3) == 0:
            result.append("Fizz")
        elif (i % 5) == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    print(" ".join(result))


if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print("Missing The first argument 'Number' ")
        print("How to run it: ./0-fizzbuzz.py <number>")
        print("Example: ./0-fizzbuzz.py 89")
        sys.exit(1)
    else:
        number = int(sys.argv[1])
        fizzbuzz(number)
