# HOMEWORK
# 1. Return uncommon elements of lists. Order of elements does not matter.
list1 = [1, 2, 3, 4]
list2 = [3, 5, 6, 7, 2]
unique_list = list(set(list1) ^ set(list2))


# 2. Print the square of each number which is less than `n` on a separate line.
n = int(input("Enter a number: "))
for number in range(1, n):
    print(number ** 2)

# 3. `txt` nomli string saqlovchi o'zgaruvchi berilgan. 
# `txt`dagi har uchinchi belgidan keyin pastgi chiziqcha (underscore) qo'yilsin. 
# Agar belgi unli harf yoki orqasidan ostki chiziqcha qo'yilgan harf bo'lsa, 
# ostki chiziqcha keyingi harfdan keyin qo'yilsin. 
# Agar belgi satrdagi oxirgi belgi bo'lsa chiziqcha qo'yilmasin.

txt = input("Enter your text: ")  #"abcabcdabcdeabcdefabcdefg"
vowels = "aeiou"
used_hosts = set()  # This is memory of letters already used with '_'
result = ""
counter = 0

for i in range(len(txt)):
    char = txt[i].lower()
    result += txt[i]
    counter += 1
    
    if counter >= 3:
        if i != len(txt) - 1 and char not in vowels and char not in used_hosts:
            result += "_"
            used_hosts.add(char)
            counter = 0 
        else:
            pass

print(f"Result: {result}")

# **4. Number Guessing Game**
# Create a simple number guessing game.
# - The computer randomly selects a number between 1 and 100. 
# - If the guess is high, print "Too high!". 
# - If the guess is low, print "Too low!". 
# - If they guess correctly, print "You guessed it right!" and exit the loop.
# - The player has 10 attempts to guess it. If the player can not find the correct number in 10 attempts, print "You lost. Want to play again? ".
# - If the player types one of 'Y', 'YES', 'y', 'yes', 'ok' then start the game from the beginning.

import random
secret_number = random.randint(1, 100)
attempts_remained = 10
while attempts_remained:
    user_guess = int(input("Guess a number: "))
    attempts_remained -= 1
    if user_guess == secret_number:
        print("You guessed it right!")
        break
    elif attempts_remained == 0:
        play_again = input(f"You lost. The secret number was {secret_number}. Want to play again? ").lower()
        if play_again in ['y', 'yes', 'ok']:
            attempts_remained = 10
            secret_number = random.randint(1, 100)
    elif user_guess > secret_number:
        print("Too high!")
    else:
        print("Too low!")

# **5. Password Checker**
# Task: Create a simple password checker.
# - Ask the user to enter a password. 
# - If the password is shorter than 8 characters, print "Password is too short." 
# - If the password doesn’t contain at least one uppercase letter, print "Password must contain an uppercase letter.". 
# - If the password meets both criteria, print "Password is strong."

password = input("Enter your password: ")
if len(password) < 8:
    print("Password is too short.")
else:
    for char in password:
        if char.isupper():
            print("Password is strong.")
            break
    else:
        print("Password must contain an uppercase letter.")

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

# Bonus Challenge
# Task: Create a simple text-based Rock, Paper, Scissors game where the player plays against the computer.
# - The computer randomly chooses `rock`, `paper`, or `scissors` using `random.choice()`.
# - The player enters their choice.
# - Display the winner and keep track of scores for the player and the computer.
# - First to 5 points wins the match.

comp_score = 0
user_score = 0
while (comp_score != 5) and (user_score != 5):
    comp_choice = random.choice(("rock", "paper", "scissors"))
    user_choice = input("Choose (rock, paper, scissors) ")
    if (comp_choice == "rock" and user_choice == "paper") or \
    (comp_choice == "paper" and user_choice == "scissors") or \
    (comp_choice == "scissors" and user_choice == "rock"):
        print("Computer lost with", comp_choice)
        user_score += 1
    elif (user_choice == "rock" and comp_choice == "paper") or \
    (user_choice == "paper" and comp_choice == "scissors") or \
    (user_choice == "scissors" and comp_choice == "rock"):
        print("Computer won with", comp_choice)
        comp_score += 1
    else:
        print("It is draw. Both of you chose", user_choice)
    print(f"Current scores: computer is {comp_score} and you are {user_score}", end="\n\n")

if comp_score == 5:
    print("Computer won in this game")
else:
    print("You won in this game")
