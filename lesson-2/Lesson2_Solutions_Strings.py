# STRING QUESTIONS:

# 1. Create a program to ask name and year of birth from user and tell them their age.  
import datetime as d
name = input("What is your name? ")
year = int(input("Enter your birth year: "))
print(f"You are {name}, and you are {2026 - year} years old.")

# 2. Extract car names from this text:
txt = 'LMaasleitbtui'
car1 = txt[1:3] + txt[5] + txt[7] + txt[9] + txt[11]
car2 = txt[0] + txt[3:5] + txt[6] + txt[8]*2 + txt[-1]
print(f"{car1=}\n{car2=}")

# 3. Write a Python program to:
#    - Take a string input from the user.
#    - Print the length of the string.
#    - Convert the string to uppercase and lowercase.
user_str = input("Enter a string: ")
str_len = len(user_str)
str_upper = user_str.upper()
str_lower = user_str.lower()
print(f"The length of your string is {str_len}. Upper case is {str_upper} and lower case is {str_lower}")

# 4. Write a Python program to check if a given string is `palindrome` or not.
user_str = input("Enter a string: ")
if user_str == user_str[::-1]:
    print(f"{user_str} is palindrome")
else:
    print(f"{user_str} is not palindrome")

# 5. Write a program that counts the number of vowels and consonants in a given string.
vowels = ["a", "e", "i", "o", "u"]
consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
vowel_count = 0
consonant_count = 0
user_str = input("Enter a string: ").lower()
for letter in user_str:
    if letter in vowels:
        vowel_count += 1
    elif letter in consonants:
        consonant_count +=1
print(f"{user_str} has {vowel_count} vowels and {consonant_count} consonants")


# 6. Write a Python program to check if one string contains another.
str1 = input("Enter a string: ")
str2 = input("Enter another string: ")
print(str2 in str1)

# 7. Ask the user to input a sentence and a word to replace. Replace that word with another word provided by the user.  
# Example:  
#    - Input sentence: "I love apples."  
#    - Replace: "apples"  
#    - With: "oranges"  
#    - Output: "I love oranges."
sentence = input("Enter a sentence: ")
old_value = input("What word would you like to be replaced? ")
new_value = input("Tell me the new replacement: ")
updated_sentence = sentence.replace(old_value, new_value)
print(updated_sentence)

# 8. Write a program that asks the user for a string and prints the first and last characters of the string.
user_str = input("Enter a string: ")
print(f"The first character is {user_str[0]}, and the last character is {user_str[-1]}")

# 9. Ask the user for a string and print the reversed version of it.
print(input("Enter a string: ")[::-1])

# 10. Write a program that asks the user for a sentence and prints the number of words in it.
sentence = input("Enter your sentence: ")
words = sentence.split()
print("Your sentence has {} words".format(len(words)))  

# 11. Write a program to check if a string contains any digits.  
user_str = input("Enter a string: ")
has_digit = any(char.isdigit() for char in user_str)

# 12. Write a program that takes a list of words and joins them into a single string, separated by a character (e.g., `-` or `,`).  
words = input("Enter your word list: ").split()
single_Str = "-".join(words)
print(single_Str)

# 13. Ask the user for a string and remove all spaces from it.  
print(input("Enter a string: ").strip())

# 14. Write a program to ask for two strings and check if they are equal or not. 
str1 = input("Enter a string: ")
str2 = input("Enter another string: ")
print(str2 == str1)

# 15. Ask the user for a sentence and create an acronym from the first letters of each word.  
#     Example:  
#     - Input: "World Health Organization"  
#     - Output: "WHO"  
sentence = input("Enter your sentence: ").split()
acronym = ""
for word in sentence:
    acronym += word[0].upper()
print(acronym)

# 16. Write a program that asks the user for a string and a character, then removes all occurrences of that character from the string.  
user_str = input("Enter your string: ")
character = input("Enter the character to remove: ")
updated_str = user_str.replace(character, "")
print(updated_str)

# 17. Ask the user for a string and replace all the vowels with a symbol (e.g., `*`).  
user_str = input("Enter string: ")
for v in "aeiouAEIOU":
    user_str = user_str.replace(v, "*")

# 18. Write a program that checks if a string starts with one word and ends with another.  
#     Example:  
#     - Input: "Python is fun!"  
#     - Starts with: "Python"  
#     - Ends with: "fun!"  
sentence = input("Enter your sentence: ").split()
if (sentence[0] != sentence[-1]) and len(sentence) > 2:
    print(f'Your sentence starts with "{sentence[0]}" and ends with "{sentence[-1]}"')
else:
    print("Your a string doesn't start with one word and end with another")