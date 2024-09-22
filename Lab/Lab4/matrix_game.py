"""Welcome to the Matrix Python Program"""
import sys
import math
import numpy as np



def phone_format(number_value):
    '''method for phone number format'''
    return format(int(number_value[:-1]), ",").replace(",", "-") + number_value[-1]

def create_matrix(str_values):
    '''method for creating the matrix'''
    matrix = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
    val = str_values.split()

    if len(val) != 9:
        print("Disclaimer: You don't have the correct amount of number per row")
        return None

    for counter in range(0, 9):
        if val[counter].isdigit() is False:
            print("You cannot input any characters other than numbers!")
            return None
        matrix[math.floor(counter / 3), counter % 3] = val[counter]

    return matrix


def matrix_addition():
    '''method for adding matrices'''
    matrix_add = MATRIX_1 + MATRIX_2
    print("You selected Addition. The results are: ")
    print(matrix_add)

    print("The Transpose is:")
    print(matrix_add.transpose())

    print("The row and column mean values of the results are: ")
    print("Row: " + str(np.mean(matrix_add[0, :])) + ", " + str(np.mean(matrix_add[1, :]))
          + ", " + str(np.mean(matrix_add[2, :])))
    print("Column: " + str(np.mean(matrix_add[:, 0])) + ", " + str(np.mean(matrix_add[:, 1]))
          + ", " + str(np.mean(matrix_add[:, 2])))


def matrix_subtraction():
    '''method for subtracting matrices'''
    matrix_minus = MATRIX_1 - MATRIX_2
    print("You selected Subtraction. The results are: ")
    print(matrix_minus)

    print("The Transpose is:")
    print(matrix_minus.transpose())

    print("The row and column mean values of the results are: ")
    print("Row: " + str(np.mean(matrix_minus[0, :])) + ", "
          + str(np.mean(matrix_minus[1, :])) + ", " + str(
              np.mean(matrix_minus[2, :])))
    print("Column: " + str(np.mean(matrix_minus[:, 0])) + ", "
          + str(np.mean(matrix_minus[:, 1])) + ", " + str(
              np.mean(matrix_minus[:, 2])))

def matrix_multiplication():
    '''method for multiplying matrices'''
    matrix_times = np.matmul(MATRIX_1, MATRIX_2)
    print("You selected Matrix Multiplication. The results are: ")
    print(matrix_times)

    print("The Transpose is:")
    print(matrix_times.transpose())

    print("The row and column mean values of the results are: ")
    print("Row: " + str(np.mean(matrix_times[0, :])) + ", "
          + str(np.mean(matrix_times[1, :])) + ", " + str(
              np.mean(matrix_times[2, :])))
    print("Column: " + str(np.mean(matrix_times[:, 0])) + ", "
          + str(np.mean(matrix_times[:, 1])) + ", " + str(
              np.mean(matrix_times[:, 2])))

def element_by_element():
    '''method for element by element multiplication'''
    matrix_element_times = MATRIX_1 * MATRIX_2
    print("You selected Element by Element Multiplication. The results are: ")
    print(matrix_element_times)

    print("The Transpose is:")
    print(matrix_element_times.transpose())

    print("The row and column mean values of the results are: ")
    print("Row: " + str(np.mean(matrix_element_times[0, :])) + ", "
          + str(np.mean(matrix_element_times[1, :])) + ", " + str(
              np.mean(matrix_element_times[2, :])))
    print("Column: " + str(np.mean(matrix_element_times[:, 0])) + ", "
          + str(np.mean(matrix_element_times[:, 1])) + ", " + str(
              np.mean(matrix_element_times[:, 2])))

VALUES = " "

while True:
    print("***************** Welcome to the Python Matrix Application***********")
    choice = input("Do you want to play the Matrix Game? \n Enter Y for Yes or N for No:")
    if choice == 'Y':
        # asks for phone number
        phone_number = input("Enter your phone number (Don't enter any dashes):")
        while phone_number.isdigit() is False or len(phone_number) != 10:
            phone_number = input("Your phone number is not in correct format. Please renter:")

        print(phone_format(phone_number))
        # asks user for zip code
        zipcode = input("Enter your 9-digit zip code "
                        "(put a dash after the first 5 digits before finishing): ")
        s_zipcode = zipcode.split("-")
        while len(s_zipcode) != 2 or len(s_zipcode[0]) != 5 or len(s_zipcode[1]) != 4 or \
                not s_zipcode[0] or not s_zipcode[1].isdigit():
            zipcode = input("Zipcode is not valid. Must be only numbers and 9 digits long: ")
            s_zipcode = zipcode.split("-")
        print("Zip Code: " + zipcode)

        MATRIX_1 = None
        MATRIX_2 = None
        while MATRIX_1 is None or MATRIX_2 is None:
            # ask user to enter first matrix
            print("Enter your first 3x3 matrix: ")
            values = input("")
            values += " " + input("")
            values += " " + input("")

            MATRIX_1 = create_matrix(values)

            print("Your first 3x3 matrix is: ")
            print(MATRIX_1)

            # ask user to enter second matrix
            print("Enter your second 3x3 matrix: ")
            values = input("")
            values += " " + input("")
            values += " " + input("")

            MATRIX_2 = create_matrix(values)

            print("Your second 3x3 matrix is: ")
            print(MATRIX_2)

        decision = input("Select a Matrix Operation from the list below: \n a. Addition "
                         "\n b. Subtraction \n "
                         "c. Matrix Multiplication \n d. Element by element multiplication \n ")
        if decision == 'a':
            matrix_addition()
        elif decision == 'b':
            matrix_subtraction()
        elif decision == 'c':
            matrix_multiplication()
        elif decision == 'd':
            element_by_element()
        else:
            print("Sorry. That was an invalid entry")

    elif choice == 'N':
        print("*********** Thanks for playing Python Numpy ***************")
        sys.exit(0)
    else:
        print("Sorry. Invalid entry")
