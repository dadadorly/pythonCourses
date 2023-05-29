def empty_list():
    emptyList = []
    print(f"Here a empty list {emptyList}")
    return emptyList

def four_element_list():
    fourElement = [1, 2, 3, 4]
    print(f"Here a four element list {fourElement}")
    return fourElement


def add_element(element):
    l = empty_list()
    l.append(element)
    print(f"Here a list with the element added {l}")
    return l

def pop_element(position):
    l = four_element_list()
    l.pop(position)
    print(f"Here the four element list minus the element at the position {position}\n{l}")

def create_set():
    nameSet = {"David", "Simon", "Thomas", "Patrick", "David"}
    print(nameSet)
    return nameSet

def add_element_set(element):
    nameSet = create_set()
    nameSet.add(element)
    print(nameSet)

def remove_element_set(element):
    nameSet = create_set()
    nameSet.remove(element)
    print(nameSet)

def create_tuple():
    tuple = (50, 3)
    print(tuple)

def diff_type_tuple():
    tuple = ("David", 20, "FR")
    print(tuple)
    return tuple

def unpack_tuple():
    tuple = diff_type_tuple()
    (name, age, nationality) = tuple
    print(name, age, nationality)

def add_element_tuple(element):
    tuple = diff_type_tuple()
    tuple_append = tuple + (element,)
    print(tuple_append)
    return tuple_append

def tuple2string():
    tuple = diff_type_tuple()
    s=''
    for element in tuple:
        s = s + str(element)
    print(s)
    return s

def forth_element_from_last():
    tuple = (1, 2, 3, 4, 5, 6)
    forth_from_last  = tuple[-4]
    print(tuple)
    print(forth_from_last)
    return forth_from_last

def tuple_is_immutable():
    # 14 - Show that a tuple is immutable with an example
    tuple = (1, 2, 3)
    tuple[0] = 4


def create_dict():
    my_dict = {"name": "David", "age": 20}
    print(my_dict)
    return my_dict

def add_pair_dict(key, value):
    my_dict = create_dict()
    my_dict[key] = value
    print(my_dict)

print("\n1 - Create an empty list using square brackets")
empty_list()
print("\n2 - Create a four-element list using square brackets")
four_element_list()
print("\n3 - Adding an element to a list using the append function")
add_element(5)
print("\n4 - Popping elements from a list using the pop function")
pop_element(3)
print("\n5 - Create a set")
create_set()
print("\n6 - Add elements to a set")
add_element_set("John")
print("\n7 - Remove elements from a set")
remove_element_set("Simon")
print("\n8 - Create a tuple")
create_tuple()
print("\n9 - Write a Python program to create a tuple with different data types")
diff_type_tuple()
print("\n10 - Write a Python program to unpack a tuple into several variables")
unpack_tuple()
print("\n11 - Write a Python program to add an item to a tuple")
add_element_tuple("164cm")
print("\n12 - Write a Python program to convert a tuple to a string")
tuple2string()
print("\n13 - Write a Python program to get the 4th element from the last element of a tuple")
forth_element_from_last()
print("\n14 - Show that a tuple is immutable with an example")
print("tuple = (1, 2, 3)\ntuple[0] = 4")
print("This will raise an error since tuples are immutable")
#tuple_is_immutable()
print("\n15 - Create a dictionary")
create_dict()
print("\n16 - Add a key-value pair to a dictionary")
add_pair_dict("nationality", "FR")