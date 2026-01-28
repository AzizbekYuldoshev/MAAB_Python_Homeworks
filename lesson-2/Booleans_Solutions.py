# BOOLEAN DATA TYPE QUESTIONS: 

# 1. Write a program that accepts a username and password and checks if both are not empty.
username = input("Enter your username: ")
password = input("Enter your password: ")
if username and password:
    print("Both fields are filled!")

# 2. Create a program that checks if two numbers are equal and outputs a message if they are.
num1 = float(input("Enter 1st number: "))
num2 = float(input("Enter 2nd number: "))

if num1 == num2:
    print("Two numbers are equal")
else:
    print("Two numbers are not equal")

# 3. Write a program that checks if a number is positive and even.
num = float(input("Enter a number: "))
if num > 0 and num % 2 == 0:
    print("Number is positive and even.")

# 4. Write a program that takes three numbers and checks if all of them are different.
num1 = input("Enter 1st number: ")
num2 = input("Enter 2nd number: ")
num3 = input("Enter 3rd number: ")
print(num1 == num2 == num3)

# 5. Create a program that accepts two strings and checks if they have the same length.
str1 = input("Enter 1st string: ")
str2 = input("Enter 2nd string: ")
print("The same length" if len(str1)==len(str2) else "Not the same length")

# 6. Create a program that accepts a number and checks if it’s divisible by both 3 and 5.
num = int(input("Enter your number: "))
if num % 3 == 0 and num % 5 == 0:
    print(f"{num} is divisible by both 3 and 5")
else:
    print(f"{num} isn't divisible by both 3 and 5")

# 7. Write a program that checks if the sum of two numbers is greater than 50.
num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))
sum = num1 + num2
print(f"The sum {sum} is greater than 50" if sum > 50 else f"The sum {sum} is not greater than 50")

# 8. Create a program that checks if a given number is between 10 and 20 (inclusive)
num = int(input("Enter your number: "))
print(f"{num} is between 10 and 20" if 20 >= num >= 10 else f"{num} is not between 10 and 20")