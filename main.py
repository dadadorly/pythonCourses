# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import math
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hei, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def exo1(n1, n2):
    print("1. Write a Python program to add 2 numbers.")
    print(f'\tThe 2 parameters are n1 = {n1} and n2 = {n2}')
    result = int(n1) + int(n2)
    print(f'\tThe sum of the 2 numbers is : {result}')

def exo2():
    print("2. Write a Python program to add 2 numbers using user input.")
    a = input("\tType the first number : ")
    b = input("\tType the second number : ")

    #print(f'The value of a is : {a}', end = '')
    result = int(a) +int(b)
    print(f'\tThe sum of the 2 numbers is  : {result}')

def exo3(n):
    print("3. Write a Python Program to calculate the square root")
    print(f'\tThe squareroot of {n} is : {math.sqrt(n)}')

def exo4(s1, s2):
    print("4. Write a python program to concatenate 2 strings")
    cat = s1+s2
    print(f'\tThe concat of {s1} and {s2} give {cat}')

def exo5():
    print("5. Write a Python Program to find the area of triangle")
    a = 5
    b = 6
    c = 7

    # Uncomment below to take inputs from the user
    # a = float(input('Enter first side: '))
    # b = float(input('Enter second side: '))
    # c = float(input('Enter third side: '))

    # calculate the semi-perimeter
    s = (a + b + c) / 2

    # calculate the area
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    print('\tThe area of the triangle is %0.2f' % area)

def exo6():
    print("6. Write a Python Program to convert kilometres to miles")
    # Taking kilometers input from the user
    kilometers = float(input("\tEnter value in kilometers: "))

    # conversion factor
    conv_fac = 0.621371

    # calculate miles
    miles = kilometers * conv_fac
    print('\t%0.2f kilometers is equal to %0.2f miles' % (kilometers, miles))
def exo7():
    print("7. Write a Python program to swap two variables")
    x = 10
    y = 20
    print(f'\tValue of x:{x} and value of y:{y}')
    temp = x
    x = y
    y = temp
    print("\tValues after the swap :", end=' ')
    print(f'Value of x:{x} and value of y:{y}')

def exo8():
    print("8. Write a Python program to print() with end Parameter and without end parameter")
    print(f'\tGood Morning', end='!')
    print("It is rainy today")

def exo9():
    # Python Program to convert temperature in celsius to fahrenheit
    print("9. Write a Python program to convert Celsius to Fahrenheit")
    # change this value for a different result
    celsius = 100

    # calculate fahrenheit
    fahrenheit = (celsius * 1.8) + 32
    print('\t%0.1f degree Celsius is equal to %0.1f degree Fahrenheit' % (celsius, fahrenheit))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #print_hi('David')
    exo1(3, 4)
    print()
    exo2()
    print()
    exo3(36)
    print()
    exo4("David", "LUU")
    print()
    exo5()
    print()
    exo6()
    print()
    exo7()
    print()
    exo8()
    print()
    exo9()
    print()


