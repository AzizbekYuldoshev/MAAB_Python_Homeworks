# SET TASKS
import random

# Initial data for sets
s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}

# 1. Union of Sets
union_set = s1 | s2  # Or s1.union(s2)

# 2. Intersection of Sets
inter_set = s1 & s2  # Or s1.intersection(s2)

# 3. Difference of Sets (s1 minus s2)
diff_set = s1 - s2   # Or s1.difference(s2)

# 4. Check Subset
is_subset = s1.issubset(s2) # or {4, 5} <= s2

# 5. Check Element
exists = 3 in s1

# 6. Set Length
size = len(s1)

# 7. Convert List to Set
mylist = [1, 2, 2, 3]
new_set = set(mylist)

# 8. Remove Element (discard is safer as it doesn't error if element is missing)
s1.discard(10) 

# 9. Clear Set
empty_set = set() # Always use set(), {} creates a dictionary!

# 10. Check if Set is Empty
is_empty = not s1

# 11. Symmetric Difference (In one or the other, but NOT both)
sym_diff = s1 ^ s2

# 12. Add Element
s1.add(10)

# 13. Pop Element (Removes and returns an arbitrary item)
popped = s1.pop() if s1 else None

# 14. Find Maximum
max_val = max(s1) if s1 else None

# 15. Find Minimum
min_val = min(s1) if s1 else None

# 16. Filter Even Numbers
evens = {x for x in s1 if x % 2 == 0}

# 17. Filter Odd Numbers
odds = {x for x in s1 if x % 2 != 0}

# 18. Create a Set of a Range
range_set = set(range(1, 11))

# 19. Merge and Deduplicate two lists
l1, l2 = [1, 2], [2, 3]
merged_set = set(l1 + l2)

# 20. Check Disjoint Sets (True if they have NO common elements)
are_disjoint = s1.isdisjoint(s2)

# 21. Remove Duplicates from a List (preserving order is not guaranteed)
unique_list = list(set(mylist))

# 22. Count Unique Elements
unique_count = len(set(mylist))

# 23. Generate Random Set (5 random ints between 1 and 100)
random_set = set(random.sample(range(1, 101), 5))