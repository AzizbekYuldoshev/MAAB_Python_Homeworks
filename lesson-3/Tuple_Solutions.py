# TUPLE TASKS

# 1. **Count Occurrences**: Given a tuple and an element, find how many times the element appears in the tuple.
fruits = ("apple", "banana", "apple", "cherry", 'peach',"apple")
apple_count = fruits.count("apple")

# 2. **Max Element**: From a given tuple, determine the largest element.
numbers = (1, 2, 3, 4, 5, 6, 7, 12, 8, 9, 10)
max_element = max(numbers)

# 3. **Min Element**: From a given tuple, determine the smallest element.
numbers = (1, 2, 3, 4, 5, 6, 7, 12, 8, 9, 10)
min_element = min(numbers)

# 4. **Check Element**: Given a tuple and an element, check if the element is present in the tuple.
fruits = ("apple", "banana", "apple", "cherry", 'peach',"apple")
pear_exist = "pear" in fruits

# 5. **First Element**: Access the first element of a tuple, considering what to return if the tuple is empty.
fruits = ("apple", "banana", "apple", "cherry", 'peach',"apple")
first_element = fruits[0] if fruits else "The tuple is empty"

# 6. **Last Element**: Access the last element of a tuple, considering what to return if the tuple is empty.
fruits = ("apple", "banana", "apple", "cherry", 'peach',"apple")
first_element = fruits[-1] if fruits else "The tuple is empty"

# 7. **Tuple Length**: Determine the number of elements in the tuple.
fruits = ("apple", "banana", "apple", "cherry", 'peach',"apple")
tuple_length = len(fruits)

# 8. **Slice Tuple**: Create a new tuple that contains only the first three elements of the original tuple.
fruits = ("apple", "banana", "apple", "cherry", 'peach',"apple")
first_3_fruits = fruits[:3]

# 9. **Concatenate Tuples**: Given two tuples, create a new tuple that combines both.
tuple1 = (1, 2, 3, 4)
tuple2 = (5, 6, 7, 8)
tuple_concat = tuple1 + tuple2

# 10. **Check if Tuple is Empty**: Determine if a tuple has any elements.
fruits = ("apple", "banana", "apple", "cherry", 'peach',"apple")
tuple_not_empty = bool(fruits)

# 11. **Get All Indices of Element**: Given a tuple and an element, find all the indices of that element in the tuple.
fruits = ("apple", "banana", "apple", "cherry", 'peach',"apple")
element = "apple"
all_indices = set([fruits.index("apple", i) for i in range(len(fruits))])

# 12. **Find Second Largest**: From a given tuple, find the second largest element.
numbers = (10, 1, 12, 3, 4, 5, 6, 7, 12, 8, 9, 10)
numbers_sorted = sorted(list(set(numbers)))
second_largest = numbers_sorted[-2]

# 13. **Find Second Smallest**: From a given tuple, find the second smallest element.
numbers = (10, 1, 12, 1, 3, 4, 5, 6, 7, 12, 8, 9, 10)
numbers_sorted = sorted(list(set(numbers)))
second_smallest = numbers_sorted[1]

# 14. **Create a Single Element Tuple**: Create a tuple that contains a single specified element.
single_element_tuple = (1,)

# 15. **Convert List to Tuple**: Given a list, create a tuple containing the same elements.
numbers_list = [10, 1, 12, 3, 4, 5, 6, 7, 12, 8, 9, 10]
numbers_tuple = tuple(numbers_list)

# 16. **Check if Tuple is Sorted**: Determine if the tuple is sorted in ascending order and return a boolean.
numbers = (10, 1, 12, 1, 3, 4, 5, 6, 7, 12, 8, 9, 10)
is_sorted = (numbers == tuple(sorted(numbers)))

# 17. **Find Maximum of Subtuple**: Given a tuple, find the maximum element of a specified subtuple.
numbers = (10, 1, 0, 2, 3, 4, 5, 6, 7, 12, 8, 9, 10)
max_1st_half = max(numbers[:(len(numbers)//2)])

# 18. **Find Minimum of Subtuple**: Given a tuple, find the minimum element of a specified subtuple.
numbers = (10, 1, 0, 2, 3, 4, 5, 6, 7, 12, 8, 9, 10)
min_1st_half = min(numbers[(len(numbers)//2):])

# 19. **Remove Element by Value**: Given a tuple and an element, create a new tuple that removes the first occurrence of that element.
numbers = (10, 1, 0, 2, 3, 4, 5, 6, 7, 12, 8, 9, 10)
new_tuple = numbers[1:]

# 20. **Create Nested Tuple**: Create a new tuple that contains subtuples, where each subtuple contains specified elements from the original tuple.
numbers = (10, 1, 0, 2, 3, 4, 5, 6, 7, 12, 8, 9, 10)
step = 2
nested = tuple([numbers[i:i+step] for i in range(0,len(numbers),step)])

# 21. **Repeat Elements**: Given a tuple and a number, create a new tuple where each element is repeated that number of times.
mytuple = ("apple", True, "777")
repeat = 2
new_tuple = mytuple * 2

# 22. **Create Range Tuple**: Create a tuple of numbers in a specified range (e.g., from 1 to 10).
range_tuple = tuple(range(10))

# 23. **Reverse Tuple**: Create a new tuple that contains the elements of the original tuple in reverse order.
numbers = (10, 1, 12, 1, 3, 4, 5, 6, 7, 12, 8, 9)
reverse_numbers = numbers[::-1]

# 24. **Check Palindrome**: Given a tuple, check if the tuple is a palindrome (reads the same forwards and backwards).
numbers = (10, 1, 12, 1, 3, 4, 5, 6, 7, 12, 8, 9)
is_palindrome = (numbers == numbers[::-1])

# 25. **Get Unique Elements**: Given a tuple, create a new tuple that contains only the unique elements while maintaining the original order.
numbers = (10, 1, 12, 1, 3, 4, 5, 6, 7, 12, 8, 9, 10, 6)
unique_numbers = tuple(set(numbers))
