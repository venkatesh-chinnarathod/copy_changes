def add(a, b):
	"""Return the sum of two values."""
	return a + b


def subtract(a, b):
	"""Return the difference of two values."""
	return a - b


def multiply(a, b):
	"""Return the product of two values."""
	return a * b


def divide(a, b):
	"""Divide a by b, raising an error if b is zero."""
	if b == 0:
		raise ValueError("Cannot divide by zero")
	return a / b


def is_even(number):
	"""Return whether an integer is even."""
	return number % 2 == 0


def greet(name):
	"""Return a greeting for the given name."""
	return f"Hello, {name}!"
