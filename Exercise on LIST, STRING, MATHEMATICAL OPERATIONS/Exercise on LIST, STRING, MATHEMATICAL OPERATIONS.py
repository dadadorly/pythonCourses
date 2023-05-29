from collections import Counter
#1. Multiply all the items in a list:
def multiply_list(items):
    result = 1
    for item in items:
        result *= item
    return result

my_list = [2, 3, 4, 5]
print("1. Multiply all the items in a list:")
print(multiply_list(my_list))

#2. Sum all the items in a list:
def sum_list(items):
    result = 0
    for item in items:
        result += item
    return result

my_list = [1, 2, 3, 4, 5]
print("2. Sum all the items in a list:")
print(sum_list(my_list))

#3. Get the largest number from a list:
def find_largest_number(items):
    return max(items)

my_list = [10, 5, 8, 20, 3]
print("3. Get the largest number from a list:")
print(find_largest_number(my_list))

#4. Get the smallest number from a list:
def find_smallest_number(items):
    return min(items)

my_list = [10, 5, 8, 20, 3]
print("4. Get the smallest number from a list:")
print(find_smallest_number(my_list))

#5. Count the number of strings where the string length is 2 or more and the first and last character are the same from a given list of strings:
def count_strings(items):
    count = 0
    for string in items:
        if len(string) >= 2 and string[0] == string[-1]:
            count += 1
    return count

my_list = ['abc', 'xyz', 'aba', '1221']
print("5. Count the number of strings where the string length is 2 or more and the first and last character are the same from a given list of strings:")
print(count_strings(my_list))

#6. Get a list sorted in increasing order by the last element in each tuple from a given list of non-empty tuples:
def sort_tuples(items):
    return sorted(items, key=lambda x: x[-1])

my_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
print("6. Get a list sorted in increasing order by the last element in each tuple from a given list of non-empty tuples:")
print(sort_tuples(my_list))

#7. Remove duplicates from a list:
def remove_duplicates(items):
    return list(set(items))

my_list = [1, 2, 3, 2, 4, 3, 5]
print("7. Remove duplicates from a list:")
print(remove_duplicates(my_list))

#8. Copy a list:
def copy_list(items):
    return list(items)

my_list = [1, 2, 3, 4, 5]
copied_list = copy_list(my_list)
print("8. Copy a list:")
print(copied_list)

#9. Print a specified list after removing the 0th, 4th, and 5th elements:
def remove_elements(items):
    del items[5]
    del items[4]
    del items[0]
    return items

my_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
print("9. Print a specified list after removing the 0th, 4th, and 5th elements:")
print(remove_elements(my_list))

#10. Append a list to the second list:
def append_lists(list1, list2):
    list2.extend(list1)
    return list2

my_list1 = [1, 2, 3]
my_list2 = [4, 5, 6]
print("10. Append a list to the second list:")
print(append_lists(my_list1, my_list2))

#11. Write a Python program to get the frequency of the elements in a list:
def get_frequency(items):
    return dict(Counter(items))

my_list = [1, 2, 3, 2, 1, 3, 2, 1, 4]
print("11. Write a Python program to get the frequency of the elements in a list:")
print(get_frequency(my_list))

#12. Write a Python program to remove all the duplicated tuples from the given list:
def remove_duplicate_tuples(items):
    return list(set(items))

my_list = [(1, 2), (3, 4), (1, 2), (5, 6), (3, 4)]
print("12. Write a Python program to remove all the duplicated tuples from the given list:")
print(remove_duplicate_tuples(my_list))

#13. Write a Python program to find Tuples with positive elements in List of tuples:
def find_positive_tuples(items):
    return [t for t in items if all(i > 0 for i in t)]

my_list = [(4, 5, 9), (-3, 2, 3), (-3, 5, 6), (4, -6)]
print("13. Write a Python program to find Tuples with positive elements in List of tuples:")
print(find_positive_tuples(my_list))

#14. Write a Python program to Remove tuples having duplicate first value from given list of tuples:
def remove_duplicates_first_value(items):
    seen = set()
    result = []
    for item in items:
        if item[0] not in seen:
            seen.add(item[0])
            result.append(item)
    return result

my_list = [(12.121, 'Tuple1'), (12.121, 'Tuple2'), (12.121, 'Tuple3'), (923232.2323, 'Tuple4')]
print("14. Write a Python program to Remove tuples having duplicate first value from given list of tuples:")
print(remove_duplicates_first_value(my_list))

#15. Write a Python script to sort (ascending and descending) a dictionary by value:
def sort_dictionary_by_value(dictionary, reverse=False):
    return dict(sorted(dictionary.items(), key=lambda x: x[1], reverse=reverse))

my_dict = {'a': 10, 'b': 30, 'c': 20}
print("15. Write a Python script to sort (ascending and descending) a dictionary by value:")
print(sort_dictionary_by_value(my_dict))  # Ascending order
print(sort_dictionary_by_value(my_dict, reverse=True))  # Descending order

#16. Write a Python script to add a key to a dictionary:
def add_key_to_dictionary(dictionary, key, value):
    dictionary[key] = value
    return dictionary

my_dict = {0: 10, 1: 20}
print("16. Write a Python script to add a key to a dictionary:")
print(add_key_to_dictionary(my_dict, 2, 30))

#17. Write a Python script to concatenate following dictionaries to create a new one:
def concatenate_dictionaries(*dicts):
    result = {}
    for d in dicts:
        result.update(d)
    return result

dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
print("17. Write a Python script to concatenate following dictionaries to create a new one:")
print(concatenate_dictionaries(dic1, dic2, dic3))

#18. Write a Python script to merge two Python dictionaries:
def merge_dictionaries(dict1, dict2):
    merged_dict = dict1.copy()
    merged_dict.update(dict2)
    return merged_dict

dict1 = {1: 10, 2: 20}
dict2 = {3: 30, 4: 40}
print("18. Write a Python script to merge two Python dictionaries:")
print(merge_dictionaries(dict1, dict2))

#19. Write a Python program to sum all the items in a dictionary:
def sum_dictionary_items(dictionary):
    return sum(dictionary.values())

my_dict = {'a': 100, 'b': 200, 'c': 300}
print("19. Write a Python program to sum all the items in a dictionary:")
print(sum_dictionary_items(my_dict))

#20. Write a Python program to multiply all the items in a dictionary:
def multiply_dictionary_items(dictionary):
    result = 1
    for value in dictionary.values():
        result *= value
    return result

my_dict = {'a': 2, 'b': 3, 'c': 4}
print("20. Write a Python program to multiply all the items in a dictionary:")
print(multiply_dictionary_items(my_dict))

#21. Write a Python program to remove a key from a dictionary:
def remove_key_from_dictionary(dictionary, key):
    dictionary.pop(key, None)
    return dictionary

my_dict = {'a': 100, 'b': 200, 'c': 300}
print("21. Write a Python program to remove a key from a dictionary:")
print(remove_key_from_dictionary(my_dict, 'b'))

#22. Write a Python program to map two lists into a dictionary:
def map_lists_to_dictionary(keys, values):
    return dict(zip(keys, values))

keys = ['a', 'b', 'c']
values = [1, 2, 3]
print("22. Write a Python program to map two lists into a dictionary:")
print(map_lists_to_dictionary(keys, values))

#23. Write a Python program to get the maximum and minimum value in a dictionary:
def get_min_max_values(dictionary):
    values = dictionary.values()
    return min(values), max(values)

my_dict = {'a': 10, 'b': 20, 'c': 5}
print("23. Write a Python program to get the maximum and minimum value in a dictionary:")
print(get_min_max_values(my_dict))

#24. Write a Python program to remove duplicates from Dictionary:
def remove_duplicates_from_dictionary(dictionary):
    return {k: v for k, v in set(dictionary.items())}

my_dict = {'a': 10, 'b': 20, 'c': 10}
print("24. Write a Python program to remove duplicates from Dictionary:")
print(remove_duplicates_from_dictionary(my_dict))

#25. Write a Python program to combine two dictionary adding values for common keys:
from collections import Counter

def combine_dictionaries(dict1, dict2):
    result = Counter(dict1) + Counter(dict2)
    return dict(result)

d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}
print("25. Write a Python program to combine two dictionary adding values for common keys:")
print(combine_dictionaries(d1, d2))

#26. Write a Python program to print all unique values in a dictionary:
def print_unique_values(dictionary):
    unique_values = set(dictionary.values())
    for value in unique_values:
        print(value)

my_dict = {'a': 10, 'b': 20, 'c': 10, 'd': 30}
print("26. Write a Python program to print all unique values in a dictionary:")
print_unique_values(my_dict)

#27. Write a Python program to count number of items in a dictionary value that is a list:
def count_items_in_list_values(dictionary):
    count = 0
    for value in dictionary.values():
        if isinstance(value, list):
            count += len(value)
    return count

my_dict = {'a': [1, 2, 3], 'b': 10, 'c': [4, 5]}
print("27. Write a Python program to count number of items in a dictionary value that is a list:")
print(count_items_in_list_values(my_dict))

#28. Write a Python program to create a tuple:
my_tuple = (1, 2, 3)
print("28. Write a Python program to create a tuple:")
print(my_tuple)

#29. Write a Python program to create a tuple with different data types:
my_tuple = (1, 'a', True, 3.14)
print("29. Write a Python program to create a tuple with different data types:")
print(my_tuple)

#30. Write a Python program to create a tuple with numbers and print one item:
my_tuple = (10, 20, 30)
print("30. Write a Python program to create a tuple with numbers and print one item:")
print(my_tuple[1])

#31. Write a Python program to add an item in a tuple:
def add_item_to_tuple(tuple, item):
    new_tuple = tuple + (item,)
    return new_tuple

my_tuple = (1, 2, 3)
print("31. Write a Python program to add an item in a tuple:")
print(add_item_to_tuple(my_tuple, 4))

#32. Write a Python program to get the 4th element and 4th element from last of a tuple:
def get_elements_from_tuple(tuple):
    return tuple[3], tuple[-4]

my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print("32. Write a Python program to get the 4th element and 4th element from last of a tuple:")
print(get_elements_from_tuple(my_tuple))

#33. Write a Python program to find the repeated items of a tuple:
def find_repeated_items(my_tuple):
    repeated_items = []
    for item in my_tuple:
        if my_tuple.count(item) > 1 and item not in repeated_items:
            repeated_items.append(item)
    return tuple(repeated_items)

my_tuple = (1, 2, 3, 2, 4, 5, 2, 6, 7, 2)
repeated_items = find_repeated_items(my_tuple)
print("33. Write a Python program to find the repeated items of a tuple:")
print(repeated_items)

#34. Write a Python program to find the length of a tuple:
my_tuple = (1, 2, 3, 4, 5)
print("34. Write a Python program to find the length of a tuple:")
print(len(my_tuple))

#35. Write a Python program to replace last value of tuples in a list:
def replace_last_value(tuples_list, new_value):
    new_list = []
    for t in tuples_list:
        new_list.append(t[:-1] + (new_value,))
    return new_list

my_list = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
new_value = 100
print("35. Write a Python program to replace last value of tuples in a list:")
print(replace_last_value(my_list, new_value))


