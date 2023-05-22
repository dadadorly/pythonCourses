import calendar
def lcm():
    # Python Program to find the L.C.M. of two input number
    x = int(input("Type the first number : "))
    y = int(input("Type the second number : "))
    # choose the greater number
    if x > y:
        greater = x
    else:
        greater = y

    while 1:
        if (greater % x == 0) and (greater % y == 0):
            lcm = greater
            break
        greater += 1

    print("The L.C.M. is", lcm)


def hcf():
    # Python program to find H.C.F of two numbers
    x = int(input("Type the first number : "))
    y = int(input("Type the second number : "))
    # choose the smaller number
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller + 1):
        if (x % i == 0) and (y % i == 0):
            hcf = i

    print("The H.C.F. is", hcf)


def decimal_to_binary(decimal_num):
    binary_num = bin(decimal_num).replace("0b", "")
    return binary_num


def decimal_to_octal(decimal_num):
    octal_num = oct(decimal_num).replace("0o", "")
    return octal_num


def decimal_to_hexadecimal(decimal_num):
    hexadecimal_num = hex(decimal_num).replace("0x", "")
    return hexadecimal_num


def conversion():
    decimal_num = int(input("Enter a decimal number: "))

    binary_num = decimal_to_binary(decimal_num)
    octal_num = decimal_to_octal(decimal_num)
    hexadecimal_num = decimal_to_hexadecimal(decimal_num)

    print("Binary representation:", binary_num)
    print("Octal representation:", octal_num)
    print("Hexadecimal representation:", hexadecimal_num)


def find_ASCII_value():
    character = input("Enter a character: ")

    print("The ASCII value of", character, "is", ord(character))


def calculator():
    print("Choose two numbers to calculate.")
    num1 = int(input("Type the first number : "))
    num2 = int(input("Type the second number : "))

    operation = input("Choose the type operation you want (+,-,/,*) : ")
    match operation:
        case "+":
            print(f"{num1} + {num2}", end=' = ')
            print(f"{num1+num2}")
        case "-":
            print(f"{num1} - {num2}", end=' = ')
            print(f"{num1-num2}")
        case "*":
            print(f"{num1} * {num2}", end=' = ')
            print(f"{num1*num2}")
        case "/":
            print(f"{num1} / {num2}", end=' = ')
            print(f"{num1/num2}")


def cal():
    year = int(input("Choose a year : "))
    month = int(input("Choose a month : "))

    print(calendar.month(year, month))

def evenList():
    evenNumbers = []
    print("This will show the list of even number between two numbers.")
    start = int(input("Enter starting number : "))
    end = int(input("Enter last number : "))
    for num in range(start, end):
        if num % 2 == 0:
            evenNumbers.append(num)
    print(evenNumbers)

if __name__ == '__main__':
    choice = ''
    while choice != "stop":
        print()
        print("1. Python Program to Find LCM using function")
        print("2. Python Program to Find HCF using function")
        print("3. Python Program to Convert Decimal to Binary, Octal and Hexadecimal using function")
        print("4. Python Program To Find ASCII value of a character using function")
        print("5. Python Program to Make a Simple Calculator using function")
        print("6. Python Program to Display Calendar using function")
        print("7. Generate a  list of all the even numbers between 4 to 30 using function")

        choice = input("Type the exercise number ('q' to stop) : ")

        match choice:
            case "1":
                lcm()
                input("\nPress enter to continue ...")
            case "2":
                hcf()
                input("\nPress enter to continue ...")
            case "3":
                conversion()
                input("\nPress enter to continue ...")
            case "4":
                find_ASCII_value()
                input("\nPress enter to continue ...")
            case "5":
                calculator()
                input("\nPress enter to continue ...")
            case "6":
                cal()
                input("\nPress enter to continue ...")
            case "7":
                evenList()
                input("\nPress enter to continue ...")
            case "q":
                break
            case _:
                print("No exercises")
