# NUMBER DATA TYPE QUESTIONS:

# 1. Create a program that takes a float number as input and rounds it to 2 decimal places.
user_num = round(float(input("Enter a float number: ")), 2)

# 2. Write a Python program that asks for three numbers and outputs the largest and smallest.
numbers = []
for i in range(3):
    numbers.append(int(input("Enter a number: ")))
print(f"{max(numbers)=}\n{min(numbers)=}")

# 3. Create a program that converts kilometers to meters and centimeters.
km = float(input("Enter kilometers: "))
m = km * 1000
cm = m * 10

print(f"It's {m} meters or {cm} cantimeters")

# 4. Write a program that takes two numbers and prints out the result of integer division and theremainder.
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

division, remainder = divmod(num1, num2)
print(f"{division=} and {remainder=}")

# 5. Make a program that converts a given Celsius temperature to Fahrenheit.
degree_c = float(input("Enter Celsius temperature: "))
degree_f = degree_c * 1.8 + 32
print(f"{degree_f=}")

# 6. Create a program that accepts a number and returns the last digit of that number.
num = input("Enter a number: ")
print("Your last digit is", num[-1])

# 7. Create a program that takes a number and checks if it’s even or not.
num = int(input("Enter a number: "))
if num % 2 == 0:
    print(f"{num} is an even number")
else:
    print(f"{num} is an odd number")