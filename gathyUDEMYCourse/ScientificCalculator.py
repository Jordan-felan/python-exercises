import math
# SCIENTIFIC CALCULATOR

while True:
    print("\nChoose the math operation.\n\n0 - Addidtion\n1 - Subtraction\n2 - Multiplication\n3 - Division\n4 - Modulo\n5 - Raising to a power\n6 - Square Root\n7 - Logarithm\n8 - Sine\n9 - Cosine\n10 - Tangent\n")

    oper = input("\nYour option from the menu: ")

    # addition
    if oper == "0":
        val1 = float(input("\nFirst value: "))
        val2 = float(input("\nSecond value: "))

        print("\nThe result is: " + str(val1 + val2) + "\n")

        # going back to the main menu or exiting the program
        back = input('\nGo back to the main menu? (y/n) ')
        if back == "y":
            continue
        else:
            break

    # subtraction
    elif oper == "1":
        val1 = float(input("\nFirst value: "))
        val2 = float(input("\nSecond value: "))

        print("\nThe result is: " + str(val1 - val2) + "\n")

        # going back to the main menu or exiting the program
        back = input('\nGo back to the main menu? (y/n) ')
        if back == "y":
            continue
        else:
            break

    # multiplication
    elif oper == "2":
        val1 = float(input("\nFirst value: "))
        val2 = float(input("\nSecond value: "))

        print("\nThe result is: " + str(val1 * val2) + "\n")

        # going back to the main menu or exiting the programv
        back = input('\nGo back to the main menu? (y/n) ')
        if back == "y":
            continue
        else:
            break

    # division
    elif oper == "3":
        val1 = float(input("\nFirst value: "))
        val2 = float(input("\nSecond value: "))

        print("\nThe result is: " + str(val1 / val2) + "\n")

        # going back to the main menu or exiting the program
        back = input('\nGo back to the main menu? (y/n) ')
        if back == "y":
            continue
        else:
            break

    # Modulo
    elif oper == "4":
        val1 = float(input("\nFirst value: "))
        val2 = float(input("\nSecond value: "))

        print("\nThe result is: " + str(val1 % val2) + "\n")

        # going back to the main menu or exiting the program
        back = input('\nGo back to the main menu? (y/n) ')
        if back == "y":
            continue
        else:
            break

    # raising to a power
    elif oper == "5":
        val1 = float(input("\nFirst value: "))
        val2 = float(input("\nSecond value: "))

        print("\nThe result is: " + str(math.pow(val1, val2)) + "\n")

        # going back to the main menu or exiting the program
        back = input('\nGo back to the main menu? (y/n) ')
        if back == "y":
            continue
        else:
            break

    # square root
    elif oper == "6":
        val1 = float(input("\nEnter value for extracting square root: "))

        print("\nThe result is: " + str(math.sqrt(val1)) + "\n")

        # going back to the main menu or exiting the program
        back = input('\nGo back to the main menu? (y/n) ')
        if back == "y":
            continue
        else:
            break

    # logarithm
    elif oper == "7":
        val1 = float(input("\nEnter value for calculating the logarithm to base 2: "))

        print("\nThe result is: " + str(math.log(val1,2)) + "\n")

        # going back to the main menu or exiting the program
        back = input('\nGo back to the main menu? (y/n) ')
        if back == "y":
            continue
        else:
            break

    # sine
    elif oper == "8":
        val1 = float(input("\nEnter value (in degrees) for calculating the sine: "))

        print("\nThe result is: " + str(math.sin(math.radians(val1))) + "\n")

        # going back to the main menu or exiting the program
        back = input('\nGo back to the main menu? (y/n) ')
        if back == "y":
            continue
        else:
            break

    # cosine
    elif oper == "9":
        val1 = float(input("\nEnter value (in degrees) for calculating the cosine: "))

        print("\nThe result is: " + str(math.cos(math.radians(val1))) + "\n")

        # going back to the main menu or exiting the program
        back = input('\nGo back to the main menu? (y/n) ')
        if back == "y":
            continue
        else:
            break

    # tangent
    elif oper == "10":
        val1 = float(input("\nEnter value (in degrees) for calculating the tangent: "))

        print("\nThe result is: " + str(math.tan(math.radians(val1))) + "\n")

        # going back to the main menu or exiting the program
        back = input('\nGo back to the main menu? (y/n) ')
        if back == "y":
            continue
        else:
            break

    else:
        print("\nInvalid option!\n")
        continue