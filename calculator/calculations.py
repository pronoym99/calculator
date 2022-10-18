# calculator/calculations.py

"""Provide several sample math calculations.

This module allows the user to make mathematical calculations.

Examples:
    >>> from calculator import calculations
    >>> calculations.add(2, 4)
    6.0
    >>> calculations.multiply(2.0, 4.0)
    8.0
    >>> from calculator.calculations import divide
    >>> divide(4.0, 2)
    2.0

The module contains the following functions:

- `add(a, b)` - Returns the sum of two numbers.
- `subtract(a, b)` - Returns the difference of two numbers.
- `multiply(a, b)` - Returns the product of two numbers.
- `divide(a, b)` - Returns the quotient of two numbers.
"""

from typing import Union


def add(a, b):
  """Compute and return the sum of two numbers.

  Args:
      a (float): A number representing the first addend in the addition.
      b (float): A number representing the second addend in the addition.

  Returns:
    float: A number representing the arithmetic sum of `a` and `b`.

  Examples:
    >>> add(4.0, 2.0)
    6.0
    >>> add(4, 2)
    6.0

  """

  return float(a + b)


def subtract(a, b):
  """Compute and return the difference of two numbers.

  Args:
      a (float): A number representing the first number.
      b (float): A number representing the second number.

  Returns:
    float: A number representing the arithmetic difference of `a` and `b`.

  Examples:
    >>> subtract(4.0, 2.0)
    2.0
    >>> subtract(4, 2)
    2.0

  """
  return float(a - b)


def multiply(a, b):
  """Compute and return the product of two numbers.

  Args:
      a (float): A number representing the first number.
      b (float): A number representing the second number.

  Returns:
    float: A number representing the arithmetic product of `a` and `b`.

  Examples:
    >>> multiply(4.0, 2.0)
    8.0
    >>> multiply(4, 2)
    8.0

  """
  return float(a * b)


def divide(a, b):
  """Compute and return the ratio of two numbers.

  Args:
      a (float): A number representing the first number.
      b (float): A number representing the second number.

  Returns:
    float: A number representing the arithmetic ratio of `a` and `b`.

  Raises:
    ZeroDivisionError: When denominator is zero.

  Examples:
    >>> divide(4.0, 2.0)
    2.0
    >>> divide(4, 2)
    2.0

  """
  if b == 0:
    raise ZeroDivisionError("division by zero")
  return float(a / b)
