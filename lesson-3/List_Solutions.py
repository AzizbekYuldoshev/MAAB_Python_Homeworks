# LIST TASKS

# 1. **Count Occurrences**: Given a list and an element, find how many times the element appears in the list.
mylist = ["apple", "peach", "apple", "pear"]
apple_count = mylist.count("apple")

# 2. **Sum of Elements**: Given a list of numbers, calculate the total of all the elements.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
total = sum(numbers)

# 3. **Max Element**: From a given list, determine the largest element.
mylist = [1, 2, 3, 4.5]
max_item_numeric = max(mylist)

this_list = ["Hello", "Apple", "Melon"]
max_item_string = max(this_list)

# 4. **Min Element**: From a given list, determine the smallest element.
mylist = [1, 2, 3, 4.5]
min_item_numeric = min(mylist)

this_list = ["Hello", "Apple", "Melon"]
min_item_string = min(this_list)

# 5. **Check Element**: Given a list and an element, check if the element is present in the list.
mylist = ["apple", "peach", "apple", "pear"]
exist_status = "apple" in mylist

# 6. **First Element**: Access the first element of a list, considering what to return if the list is empty.
mylist = []
if mylist:
    result = mylist[0]
else:
    result = "This list is empty"

# 7. **Last Element**: Access the last element of a list, considering what to return if the list is empty.
mylist = ["Hello", "World"]
if mylist:
    result = mylist[-1]
else:
    result = "This list is empty"

# 8. **Slice List**: Create a new list that contains only the first three elements of the original list.
fruits = ["apple", "peach", "apple", "pear", "melon", "watermelon"]
cheap_fruits = fruits[:3]

# 9. **Reverse List**: Create a new list that contains the elements of the original list in reverse order.
fruits_reverse2 = fruits[::-1]

# 10. **Sort List**: Create a new list that contains the elements of the original list in sorted order.
fruits_sorted =  sorted(fruits)

# 11. **Remove Duplicates**: Given a list, create a new list that contains only unique elements from the original list.
fruits_uniqe = list(set(fruits))

# 12. **Insert Element**: Given a list and an element, insert the element at a specified index.
fruits = ["apple", "peach", "apple", "pear", "melon", "watermelon"]
fruits.insert(3, "pineapple")

# 13. **Index of Element**: Given a list and an element, find the index of the first occurrence of the element.
apple_index_1st = fruits.index("apple")
apple_index_2nd = fruits.index("apple", fruits.index("apple")+1)

# 14. **Check for Empty List**: Determine if a list is empty and return a boolean.
my_list = [1]
status = bool(my_list)

# 15. **Count Even Numbers**: Given a list of integers, count how many of them are even.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_nums = [num for num in numbers if num % 2 == 0]
evens = len(even_nums)

# 16. **Count Odd Numbers**: Given a list of integers, count how many of them are odd.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
odd_nums = [num for num in numbers if num % 2 == 1]
odds = len(odd_nums)

# 17. **Concatenate Lists**: Given two lists, create a new list that combines both lists.
letters = ["a", "b", "c"]
numbers = [1, 2, 3]
mixed = letters + numbers

# 18. **Find Sublist**: Given a list and a sublist, check if the sublist exists within the list.
mix = ['a', 'b', 'c', 1, 2, 3]
numbers = [1, 2, "a"]
issublist = True
for item in numbers:
    if item in mix:
        pass
    else:
        issublist = False
        break

# 19. **Replace Element**: Given a list, replace the first occurrence of a specified element with another element.
mix = ['a', 'b', 'c', 1, 2, 3]
mix[mix.index("a")] = "A"

# 20. **Find Second Largest**: From a given list, find the second largest element.
numbers = [21, 12, 324, 1, 242, 43, 124, 235]
second_largest = sorted(list(set(numbers)), reverse=True)[1]

# 21. **Find Second Smallest**: From a given list, find the second smallest element.
numbers = [21, 12, 324, 1, 242, 43, 124, 235]
second_smallest = sorted(list(set(numbers)))[1]

# 22. **Filter Even Numbers**: Given a list of integers, create a new list that contains only the even numbers.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_nums = [num for num in numbers if num % 2 == 0]

# 23. **Filter Odd Numbers**: Given a list of integers, create a new list that contains only the odd numbers.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
odd_nums = [num for num in numbers if num % 2 == 1]

# 24. **List Length**: Determine the number of elements in the list.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
numbers_length = len(numbers)

# 25. **Create a Copy**: Create a new list that is a copy of the original list.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
num_copy1 = numbers.copy()
num_copy2 = numbers[:]
num_copy3 = list(numbers)

# 26. **Get Middle Element**: Given a list, find the middle element. If the list has an even number of elements, return the two middle elements.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
numbers_length = len(numbers)
middle_num_index = round(numbers_length/2)
if numbers_length % 2 == 0:
    print(numbers[middle_num_index], numbers[middle_num_index +1])
else:
    print(numbers[middle_num_index])

# 27. **Find Maximum of Sublist**: Given a list, find the maximum element of a specified sublist.
temps = [18, 19, 21, 20, 22, 28, 27]
# Find max of the weekend (index 5 to the end)
weekend_max = max(temps[5:]) 

# 28. **Find Minimum of Sublist**: Given a list, find the minimum element of a specified sublist.
# Find min of the first three days (index 0 to 3)
early_week_min = min(temps[:3])

# 29. **Remove Element by Index**: Given a list and an index, remove the element at that index if it exists.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
deleted_num = numbers.pop(0)  #first item deleted
deleted_num2 = numbers.pop()  #last item deleted
del numbers[3]  #item with third index deleted

# 30. **Check if List is Sorted**: Determine if the list is sorted in ascending order and return a boolean.
original_list = [12, 3, 1254, 33, 1324, 5, 65, 76]
sorted_list = sorted(original_list)
isthesame = original_list == sorted_list

# 31. **Repeat Elements**: Given a list and a number, create a new list where each element is repeated that number of times.
my_list = ["a", "b", "c"]
replicate_amount = 3
new_list = my_list * replicate_amount
new_list.sort()

# 32. **Merge and Sort**: Given two lists, create a new sorted list that merges both lists.
list1 = ["d", "e", "f"]
list2 = ["a", "b", "c"]
new_list = list1 + list2
new_list.sort()

# 33. **Find All Indices**: Given a list and an element, find all the indices of that element in the list.
mylist = ["apple", "banana", "apple", "cherry", "apple", "date"]
element = "apple"
all_indices = [i for i, fruit in enumerate(mylist) if fruit == element]

# 34. **Rotate List**: Given a list, create a new list that is a rotated version of the original list (shift elements to the right).
mylist = [1, 2, 3, 4, 5]
rotated = mylist[-1:] + mylist[:-1]

# 35. **Create Range List**: Create a list of numbers in a specified range (e.g., from 1 to 10).
range_list_10 = [number for number in range(1,11)]

# 36. **Sum of Positive Numbers**: Given a list of numbers, calculate the sum of all positive numbers.
numbers = [1, -2, 3, -4, -5, 6, 7, -8]
positive_num_sum = sum([number for number in numbers if number > 0])

# 37. **Sum of Negative Numbers**: Given a list of numbers, calculate the sum of all negative numbers.
numbers = [1, -2, 3, -4, -5, 6, 7, -8]
negative_num_sum = sum([number for number in numbers if number < 0])

# 38. **Check Palindrome**: Given a list, check if the list is a palindrome (reads the same forwards and backwards).
fruits = ["apple", "peach", "apple", "pear", "melon", "watermelon"]
ispalindrome = (fruits == fruits[::-1])

# 39. **Create Nested List**: Create a new list that contains sublists, where each sublist contains a specified number of elements from the original list.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
size = 3
nested = [numbers[i : i + size] for i in range(0, len(numbers), size)]

# 40. **Get Unique Elements in Order**: Given a list, create a new list that contains unique elements while maintaining the original order.
fruits = ["apple", "peach", "apple", "pear", "melon", "watermelon"]
unique_fruits = []
for fruit in fruits:
    if fruit not in unique_fruits:
        unique_fruits.append(fruit)
