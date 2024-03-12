#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
ldigit = abs(number) % 10
result = (f"The string Last digit of {number} is {last_digit} "
          f"and is greater than 5" if last_digit > 5 else
          f"The string Last digit of {number} is {last_digit} "
          f"and is 0" if last_digit == 0 else
          f"The string Last digit of {number} is {last_digit} "
          f"and is less than 6 and not 0")

print(result)
