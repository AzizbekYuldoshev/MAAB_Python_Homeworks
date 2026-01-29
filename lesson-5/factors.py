def find_factors(number):
    number = int(number)
    for num in range(1, number+1):
        if number % num == 0:
            print(f"{num} is a factor of {number}")

find_factors(input("Enter a number: "))

# A factor of a positive integer n is any positive integer less than or equal to n that divides n with no remainder.
# For example, 3 is a factor of 12 because 12 divided by 3 is 4, with no remainder. 
# However, 5 is not a factor of 12 because 5 goes into 12 twice with a remainder of 2.
# Write a script factors.py that asks the user to input a positive integer and then prints out the factors of that number. 
# Here’s a sample run of the program with output:

# Enter a positive integer: 12
# 1 is a factor of 12
# 2 is a factor of 12
# 3 is a factor of 12
# 4 is a factor of 12
# 6 is a factor of 12
# 12 is a factor of 12