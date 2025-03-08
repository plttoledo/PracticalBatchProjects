# Prog01: Create a program that ask user to input 2 numbers. Print the smaller number.
def prog1():
    user_input1 = float(input("Enter the 1st number: "))
    user_input2 = float(input("Enter the 2nd number: "))

    if user_input1 < user_input2:
        print(f"{user_input1} is the smaller number.")
    else:
        print(f"{user_input2} is the smaller number.")

# Prog02: Create a program that ask user to input 2 numbers. Print "Not Equal" when the numbers are not the same.
def prog2():
    user_input1 = float(input("Enter the 1st number: "))
    user_input2 = float(input("Enter the 2nd number: "))

    if user_input1 != user_input2:
        print(f"The two numbers are not equal.")
    else:
        print(f"The two numbers are even")

# Prog03: Create a program that ask user to input 2 numbers. Print the difference of the two numbers.
def prog3():
    user_input1 = float(input("Enter the 1st number: "))
    user_input2 = float(input("Enter the 2nd number: "))

    print(f"{user_input1 - user_input2} is the difference of the two numbers.")

# Prog04: Create a program that ask user to input 2 numbers. Print the quotient of the two numbers without the decimal
# point.
def prog4():
    user_input1 = int(input("Enter the 1st number: "))
    user_input2 = int(input("Enter the 2nd number: "))

    print(f"{user_input1 // user_input2} is the quotient without decimal points.")

# Prog05: Create a program that ask user to input 2 numbers. Print the remainder when the first number is divided by
# the second number.
def prog5():
    user_input1 = int(input("Enter the 1st number: "))
    user_input2 = int(input("Enter the 2nd number: "))

    print(f"{user_input1 % user_input2} is the remainder of the two numbers.")

# Prog06: Create a program that ask user to input 10 numbers. Print the result of the first number
# minus all of the remaining numbers.
def prog6():
    num = [float(input(f"Enter #{i+1}: ")) for i in range(10)]
    print(f"{num[0] - sum(num[1:])} is the result of the first number minus the remaining numbers.")

# Prog07: Create a program that ask user to input 10 numbers. Print how many are even numbers.
def prog7():
    even_num = 0
    for i in range(10):
        num = int(input(f"Enter #{i+1}: "))
        if num % 2 == 0:
            even_num += 1
    print(f"There are {even_num} even numbers.")

# Prog08: Create a program that print all the odd numbers starting from 0 to 100. (Use while loop)
def prog8():
    num = 1
    while num < 100:
        print(num)
        num += 2

# Prog09: Create a program that print all the numbers starting from 0 to 100 except numbers ending in zero or
# ending five.
def prog9():
    for num in range(101):
        if num % 10 != 0 and num % 5 != 0:
            print(num)

# Prog10: Create a program that ask user to input 2 numbers. Print all the numbers between the two numbers.
def prog10():
    user_input1 = int(input("Enter the 1st number: "))
    user_input2 = int(input("Enter the 2nd number: "))

    if user_input1 > user_input2:
        print("The first input should be greater than the second input.")
    else:
        for num in range(user_input1 + 1, user_input2):
            print(num)

def main():
    while True:
        print("\nChoose a program to run:")
        print("1 - Find the smaller number")
        print("2 - Check if numbers are not equal")
        print("3 - Find the difference between two numbers")
        print("4 - Find quotient without decimal points")
        print("5 - Find remainder of division")
        print("6 - Subtract remaining numbers from the first")
        print("7 - Count even numbers")
        print("8 - Print odd numbers from 0 to 100")
        print("9 - Print numbers from 0-100 except those ending in 0 or 5")
        print("10 - Print numbers between two inputs")
        print("0 - Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            prog1()
        elif choice == "2":
            prog2()
        elif choice == "3":
            prog3()
        elif choice == "4":
            prog4()
        elif choice == "5":
            prog5()
        elif choice == "6":
            prog6()
        elif choice == "7":
            prog7()
        elif choice == "8":
            prog8()
        elif choice == "9":
            prog9()
        elif choice == "10":
            prog10()
        elif choice == "0":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number from 0 to 10.")

if __name__ == "__main__":
    main()