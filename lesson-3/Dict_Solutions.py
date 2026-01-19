# DICTIONARY TASKS
# Initial data
d1 = {"name": "Gemini", "type": "AI", "version": 2.0}
d2 = {"company": "Google", "location": "Cloud"}

# 1. Get Value (with safety default)
val = d1.get("name", "Unknown")

# 2. Check Key
has_key = "name" in d1

# 3. Count Keys
num_keys = len(d1)

# 4. Get All Keys
keys_list = list(d1.keys())

# 5. Get All Values
vals_list = list(d1.values())

# 6. Merge Dictionaries
merged_dict = d1 | d2  # Python 3.9+ syntax

# 7. Remove Key (pop with default handles "missing key" safely)
d1.pop("version", None)

# 8. Clear Dictionary
empty_dict = {}

# 9. Check if Dictionary is Empty
is_dict_empty = not d1

# 10. Get Key-Value Pair (as a tuple)
item = ("name", d1["name"]) if "name" in d1 else None

# 11. Update Value
d1["version"] = 3.0

# 12. Count Value Occurrences
count_ai = list(d1.values()).count("AI")

# 13. Invert Dictionary (Keys become values, Values become keys)
inverted = {v: k for k, v in d1.items()}

# 14. Find Keys with Value
keys_with_val = [k for k, v in d1.items() if v == "AI"]

# 15. Create a Dictionary from Lists
k_list = ["a", "b", "c"]
v_list = [1, 2, 3]
zipped_dict = dict(zip(k_list, v_list))

# 16. Check for Nested Dictionaries
has_nested = any(isinstance(v, dict) for v in d1.values())

# 17. Get Nested Value
nested_data = {"user": {"id": 101}}
user_id = nested_data.get("user", {}).get("id")

# 18. Create Default Dictionary (Handy for counting)
from collections import defaultdict
def_dict = defaultdict(int) # Default value for any new key is 0

# 19. Count Unique Values
unique_val_count = len(set(d1.values()))

# 20. Sort Dictionary by Key
sorted_by_key = dict(sorted(d1.items()))

# 21. Sort Dictionary by Value
sorted_by_val = dict(sorted(d1.items(), key=lambda item: str(item[1])))

# 22. Filter by Value (e.g., keep values > 1)
scores = {"a": 1, "b": 2, "c": 3}
filtered = {k: v for k, v in scores.items() if v > 1}

# 23. Check for Common Keys
common_keys = d1.keys() & d2.keys()

# 24. Create Dictionary from Tuple
pairs = (("id", 1), ("status", "active"))
from_tuple = dict(pairs)

# 25. Get the First Key-Value Pair
first_pair = next(iter(d1.items()), None)