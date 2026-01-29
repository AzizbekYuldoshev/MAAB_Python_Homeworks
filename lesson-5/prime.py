def is_prime(number):
    prime_status = True
    if number <= 1:
        return False
    if number == 2:
        return True
    for num in range(2, number//2 + 1):
        if number % num == 0:
            return False

# Task Details
# Define a function `is_prime(n)` which returns `True` if the given $n$ ($n$ > 0) is _prime number_, otherwise returns `False`.