# HOMEWORK
# 1. Return uncommon elements of lists. Order of elements does not matter.
list1 = [1, 2, 3, 4]
list2 = [3, 5, 6, 7, 2]
unique_list = list(set(list1).symmetric_difference(set(list2)))
print(unique_list)

# 2. Print the square of each number which is less than `n` on a separate line.
# n = int(input("Enter a number: "))
# for number in range(1, n):
#     print(number ** 2)

# 3. `txt` nomli string saqlovchi o'zgaruvchi berilgan. 
# `txt`dagi har uchinchi belgidan keyin pastgi chiziqcha (underscore) qo'yilsin. 
# Agar belgi unli harf yoki orqasidan ostki chiziqcha qo'yilgan harf bo'lsa, 
# ostki chiziqcha keyingi harfdan keyin qo'yilsin. 
# Agar belgi satrdagi oxirgi belgi bo'lsa chiziqcha qo'yilmasin.

# txt = input("Enter your text: ")
# txt_list = []
# underscore_index = 2
# for i in range(len(txt)):
#     txt_list.append(txt[i])
#     if i == underscore_index:
#         if (txt[i].lower() in "aeiou") or (i == len(txt) - 1):
#             underscore_index += 1
#         elif (txt[i] + "_") in ("".join(txt_list)):
#             underscore_index += 1
#         else:
#             txt_list.append("_")
#             underscore_index += 3

# result = "".join(txt_list)
# print(result)

# **4. Number Guessing Game**
# Create a simple number guessing game.
# - The computer randomly selects a number between 1 and 100. 
# - If the guess is high, print "Too high!". 
# - If the guess is low, print "Too low!". 
# - If they guess correctly, print "You guessed it right!" and exit the loop.
# - The player has 10 attempts to guess it. If the player can not find the correct number in 10 attempts, print "You lost. Want to play again? ".
# - If the player types one of 'Y', 'YES', 'y', 'yes', 'ok' then start the game from the beginning.

# import random
# secret_number = random.randint(1, 100)
# attempts_remained = 10
# while attempts_remained:
#     user_guess = int(input("Guess a number: "))
#     attempts_remained -= 1
#     if user_guess == secret_number:
#         print("You guessed it right!")
#         break
#     elif attempts_remained == 0:
#         play_again = input("You lost. Want to play again? ").lower()
#         if play_again in ['y', 'yes', 'ok']:
#             attempts_remained = 10
#     elif user_guess > secret_number:
#         print("Too high!")
#     else:
#         print("Too low!")

# **5. Password Checker**
# Task: Create a simple password checker.
# - Ask the user to enter a password. 
# - If the password is shorter than 8 characters, print "Password is too short." 
# - If the password doesn’t contain at least one uppercase letter, print "Password must contain an uppercase letter.". 
# - If the password meets both criteria, print "Password is strong."

# password = input("Enter your password: ")
# if len(password) < 8:
#     print("Password is too short.")
# else:
#     for char in password:
#         if (char == char.upper()) and (char not in "1234567890!@#$%^&*():; "):
#             print(char)
#             print("Password is strong.")
#             break
#     else:
#         print("Password must contain an uppercase letter.")

# **6. Prime Numbers**
# Task: Write a Python program that prints all prime numbers between 1 and 100.

for number in range(2, 101):
    if number in [2, 3, 5, 7]:
        print(number)
    else:
        if (number % 2 == 0) or (number % 3 == 0) or (number % 5 == 0) or (number % 7 == 0):
            continue
        else:
            print(number)

# ### Bonus Challenge
# Task: Create a simple text-based Rock, Paper, Scissors game where the player plays against the computer.
# - The computer randomly chooses `rock`, `paper`, or `scissors` using `random.choice()`.
# - The player enters their choice.
# - Display the winner and keep track of scores for the player and the computer.
# - First to 5 points wins the match.