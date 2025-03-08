# Prog01: Create a program that ask user to input 2 numbers. Print the bigger number.
def prog1():
    user_input1 = float(input("Enter 1st number: "))
    user_input2 = float(input("Enter 2nd number: "))
    if user_input1 > user_input2:
        print(f"{user_input1} is the bigger number")
    else:
        print(f"{user_input2} is the bigger number")

# Prog02: Create a program that ask user to input 2 numbers. Print "Equal" when the numbers are the same.
def prog2():
    user_input1 = float(input("Enter 1st number: "))
    user_input2 = float(input("Enter 2nd number: "))
    if user_input1 == user_input2:
        print(f"{user_input1} and {user_input2} are equal")
    else:
        print(f"{user_input1} and {user_input2} are not equal")

# Prog03: Create a program that ask user to input 2 numbers. Print the sum of the two numbers.
def prog3():
    user_input1 = float(input("Enter 1st number: "))
    user_input2 = float(input("Enter 2nd number: "))
    print(f"{user_input1 + user_input2} is the sum of {user_input1} and {user_input2}")

# Prog04: Create a program that ask user to input 2 numbers. Print the product of the two numbers.
def prog4():
    user_input1 = float(input("Enter 1st number: "))
    user_input2 = float(input("Enter 2nd number: "))
    print(f"{user_input1 * user_input2} is the product of {user_input1} and {user_input2}")

# Prog05: Create a program that ask user to input 2 numbers. Print the quotient of the two numbers with the
# decimal point.
def prog5():
    user_input1 = float(input("Enter 1st number: "))
    user_input2 = float(input("Enter 2nd number: "))
    print(f"{user_input1 / user_input2} is the quotient of {user_input1} and {user_input2}")

# Prog06: Create a program that ask user to input 2 numbers. Print the result when the first number is
# raised to the second number.
def prog6():
    user_input1 = float(input("Enter 1st number: "))
    user_input2 = float(input("En`ter 2nd number: "))
    print(f"{user_input1 ** user_input2} is the result of {user_input1} raised to {user_input2}")

# Prog07: Create a program that ask user to input 10 numbers. Print the sum of all the numbers.
def prog7():
    total = 0
    for i in range(10):
        num = float(input(f"Enter #{i+1}: "))
        total += num
    print(f"The sum of the 10 numbers is {total}")

# Prog08: Create a program that ask user to input 10 numbers. Print how many are odd numbers.
def prog8():
    odd_num = 0
    for i in range(10):
        num = float(input(f"Enter #{i+1}: "))
        if num % 2 != 0:
            odd_num += 1
    print(f"The sum of the odd numbers is {odd_num}")

# Prog09: Create a program that print all the even numbers starting from 0 to 100. (Use for loop)
def prog9():
    for num in range(0,101,2):
        print(num)

# Prog10: Create a program that print all the numbers starting from 0 to 100 except numbers ending in zero.
def prog10():
    for num in range(101):
        if num % 10 != 0:
            print(num)

def main():
    while True:
        print("\nChoose a program to run:")
        print("1 - Find the bigger number")
        print("2 - Check if numbers are equal")
        print("3 - Find the sum of the two numbers")
        print("4 - Find product of the two numbers")
        print("5 - Find the quotient with the decimal point")
        print("6 - Find the result of first number raised to the second number")
        print("7 - Find the sum of all 10 numbers")
        print("8 - Print how many odd numbers from 10 numbers")
        print("9 - Print all the even numbers starting from 0 to 100")
        print("10 - Print all the numbers starting from 0 to 100 except numbers ending in 0")
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