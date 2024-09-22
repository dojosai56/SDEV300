'''
Lab 2 Menu-Driven Program
'''

# Import statements
import secrets
import string
import math
import calendar
from datetime import date


# -- GLOBAL VARIABLES --
yes = ["yes", "Yes", "YES", 'Y', 'y']
no = ["no", "No", "NO", 'N', 'n']
valid_statement = ["yes", "Yes", "YES", 'Y', 'y', "no", "No", "NO", 'N', 'n']


def display_menu():
    '''
    Displays the menu with six possible choices
    :return:
    '''
    print("======= Menu =======")
    print("1. Generate Secure Password")
    print("2. Calculate and Format a Percentage")
    print("3. How many days from today until July 4, 2025?")
    print("4. Use the Law of Cosines to Calculate the leg of a triangle.")
    print("5. Calculate the volume of a Right Circular Cylinder")
    print("6. Exit program")
    print("====================")


def choice_1(length, has_upper, has_lower, has_numbers, has_special_chars):
    '''
    Generate a secure password
    :return:
    '''
    alphabet = ""  # the characters that can be used in password
    password = " "  # the generated password

    # add character sets to alphabet based on user's choices for complexity
    if has_upper in yes:
        alphabet = alphabet + string.ascii_uppercase
    if has_lower in yes:
        alphabet = alphabet + string.ascii_lowercase
    if has_numbers in yes:
        alphabet = alphabet + string.digits
    if has_special_chars in yes:
        alphabet = alphabet + string.punctuation

    # loop to continually generate psswrd until at least
    # 1 character present from each selected character set
    while True:
        password = ''.join(secrets.choice(alphabet) for i in range(length))
        is_at_least_one = bool((any(c.isupper() for c in password) or has_upper in no) and
                               (any(c.islower() for c in password) or has_lower in no) and
                               (any(c.isdigit() for c in password) or has_numbers in no) and
                               (any(c in string.punctuation for c in password) or
                                has_special_chars in no))
        if is_at_least_one:
            break

    print("password: " + password + "\n")


def choice_2(numerator, denominator, precision):
    '''
    Calculate and Format a Percentage
    :return:
    '''
    percentage = (numerator / denominator) * 100
    percentage = '{:.{prec}f}'.format(percentage, prec=precision)

    print("percentage = " + percentage + "\n")


def choice_3():
    '''
    How many days from today until July 4, 2025?
    :return:
    '''
    today = date.today()
    end_date = date(2025, 7, 4)
    final_day_year = date(today.year, 12, 31)
    resulting_days = 1 # days until july 4th, 2025

    #calculate remaining days in current
    resulting_days += abs((final_day_year - today).days)

    # if current year is leap year add 1
    if calendar.isleap(today.year):
        if today.month <= 2 and today.day < 29:
            resulting_days += 1

    # long through remaining years until 2020
    # and 365 for a non leap year and 366 for leap year
    for counter in range(today.year+1, 2025):
        if calendar.isleap(counter):
            resulting_days += 366
        else:
            resulting_days += 365

    resulting_days += abs((date(end_date.year, 1, 1) - end_date).days)
    if calendar.isleap(end_date.year):
        resulting_days += 1

    print("Days from " + str(today) + " to " + " is " + str(resulting_days) + "\n")

def choice_4(side_ac, side_bc, angle_acb, precision):
    '''
    Use the Law of Cosines to Calculate the leg of a triangle.
    :return:
    '''

    c_squared = math.pow(side_bc, 2) + math.pow(side_ac, 2) - \
                2 * side_bc * side_ac * math.cos(math.radians(angle_acb))
    side_c = math.sqrt(c_squared)
    side_c = '{:.{prec}f}'.format(side_c, prec=precision)
    print("Side AB is " + str(side_c) + "\n")


def choice_5(radius, height, precision):
    '''
    Calculate the volume of a Right Circular Cylinder
    :return:
    '''
    vol_circ_cylinder = (math.pi * math.pow(radius, 2)) * height
    vol_circ_cylinder = '{:.{prec}f}'.format(vol_circ_cylinder, prec=precision)
    print("Volume of Right Circular Cylinder is " + str(vol_circ_cylinder))

def main_method():
    '''
    the main_method for program execution
    :return:
    '''
    choice = 0
    precision = 0

    # loop to display menu and validate user's input
    while choice != 6:
        display_menu()
        choice = input("Enter choice(1-6):")

        # validate choice before casting to integer
        if choice.isdigit():
            choice = int(choice)

        if choice == 1:
            length, has_upper, has_lower, has_numbers, has_special_char,\
            is_all_no = 0, " ", " ", " ", " ", False

            print("\n-- Generating Password --")
            # Prompt user for password attribute's
            # And validate input
            while length < 10 or has_upper not in valid_statement \
                    or has_lower not in valid_statement or\
                    has_numbers not in valid_statement \
                    or has_special_char not in valid_statement or is_all_no:
                print("Length MUST be a number that is 10 or greater |"
                      " ALL questions are 'yes' or 'no' | At LEAST 1 yes required:")
                length = input("Enter length of password (minimum 10):")

                # Validate length is digit before casting to int
                if length.isdigit():
                    length = int(length)
                else:
                    length = 0

                # Prompt user for password complexity
                has_upper = input("Should password contain uppercase?")
                has_lower = input("Should password contain lowercase?")
                has_numbers = input("Should password contain numbers?")
                has_special_char = input("Should password contain special characters?")
                print("\n")

                # Boolean check if all answers are no
                # This would mean no characters to make password
                is_all_no = has_upper in no and has_lower in no \
                            and has_numbers in no and has_special_char in no

            # Data is valid so generate password
            choice_1(length, has_upper, has_lower, has_numbers, has_special_char)
        elif choice == 2:
            #Prompt the user for numerator, denominator, and decimal precision
            # NOTE: Validate numerator and denominator are integers!
            # NOTE: Validate denominator is NOT 0

            numerator, denominator = 0, 0
            while True:
                print("Only whole numbers accepted! | Decimal precision MUST be positive!")
                numerator = input("Pick a number for a numerator!")
                denominator = input("Now pick a number for a denominator!")
                precision = input("How many decimal precision desired?")

                if numerator[0] == '-':
                    numerator_sign = -1
                    numerator = numerator[1:]
                else:
                    numerator_sign = 1

                if denominator[0] == '-':
                    denominator_sign = -1
                    denominator = denominator[1:]
                else:
                    denominator_sign = 1

                if numerator.isdigit() and denominator.isdigit() \
                        and precision.isdigit() and denominator != '0':

                    numerator = int(numerator) * numerator_sign
                    denominator = int(denominator) * denominator_sign
                    precision = int(precision)
                    break

            choice_2(numerator, denominator, precision)
        elif choice == 3:
            choice_3()
        elif choice == 4:
            side_ac, side_bc, angle_acb = 0, 0, 0
            # Prompt user for side AC
            # Prompt user for side CB
            # Prompt user for angle <ACB

            while True:
                side_ac = input("Type length for side AC: ")
                side_bc = input("Type length for side BC: ")
                angle_acb = input("Type angle for <ACB: ")
                precision = input("How many decimal precision needed?")

                if side_ac.isdigit() and side_bc.isdigit() and\
                        angle_acb.isdigit() and precision.isdigit():
                    side_ac = int(side_ac)
                    side_bc = int(side_bc)
                    angle_acb = int(angle_acb)
                    precision = int(precision)
                    break
            choice_4(side_ac, side_bc, angle_acb, precision)

        elif choice == 5:
            radius, height = 0, 0
            # Prompt user for radius
            # Prompt user for height

            while True:
                radius = input("Type length of radius: ")
                height = input("Type length of height: ")
                precision = input("How many decimal precision desired?")

                if radius.isdigit() and height.isdigit() and precision.isdigit():
                    radius = int(radius)
                    height = int(height)
                    precision = int(precision)
                    break

            choice_5(radius, height, precision)
        elif choice == 6:
            print("Exiting program.")
        else:
            print("Invalid choice. Must be a number (1 to 6)")


main_method()
