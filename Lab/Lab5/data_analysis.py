'''Python Data Analysis'''
import matplotlib.pyplot as plt
import pandas as pd

a = ['a', 'A']
b = ['b', 'B']
c = ['c', 'C']
d = ['d', 'D']
e = ['e', 'E']
f = ['f', 'F']

def display_statistics(dataframe, col):
    """
    display count mean, stddev, min, max, histogram
    :return:
    """

    print("The statistics for this column are: ")
    print("Count = " + str(dataframe.count(axis=0, numeric_only=True)[col]))
    print("Mean = " + str(dataframe.mean(axis=0, numeric_only=True)[col]))
    print("Standard Deviation = " + str(dataframe.std(axis=0, numeric_only=True)[col]))
    print("Min = " + str(dataframe.min(axis=0, numeric_only=True)[col]))
    print("Max = " + str(dataframe.max(axis=0, numeric_only=True)[col]))
    print("The Histogram of this column is now displayed: ")
    #use matplotlib to display histogram
    dataframe[[col]].plot.hist(bins=500, alpha=0.5, logx=True)
    plt.show()

def display_statistics2(dataframe, col):
    """
    display count mean, stddev, min, max, histogram
    :return:
    """

    print("The statistics for this column are: ")
    print("Count = " + str(dataframe.count(axis=0, numeric_only=True)[col]))
    print("Mean = " + str(dataframe.mean(axis=0, numeric_only=True)[col]))
    print("Standard Deviation = " + str(dataframe.std(axis=0, numeric_only=True)[col]))
    print("Min = " + str(dataframe.min(axis=0, numeric_only=True)[col]))
    print("Max = " + str(dataframe.max(axis=0, numeric_only=True)[col]))
    print("The Histogram of this column is now displayed: ")
    #use matplotlib to display histogram
    dataframe[[col]].plot.hist(bins=100, alpha=0.5)
    plt.show()

def display_menu():
    '''
    Displays the menu with six possible choices
:return:
    '''

    print("***************** Welcome to the Python Data Analysis App**********")
    print("Select the file you want to analyze:")
    print("1. Population Data")
    print("2. Housing Data")
    print("3. Exit the Program")
    print("================================================\n")

def population_data():
    '''Display menu for population data'''
    pop_change = pd.read_csv('PopChange.csv')
    print("You have entered Population Data.")
    while True:
        print("a. Pop Apr 1")  # column 1
        print("b. Pop Jul 1")  # column 2
        print("c. Change Pop")  # column 3
        print("d. Exit Column")
        decision = input("Select the Column you want to analyze: ")

        if decision in a:
            print("You selected Pop Apr 1")
            display_statistics(pop_change, "Pop Apr 1")
        elif decision in b:
            print("You selected Pop Jul 1")
            display_statistics(pop_change, "Pop Jul 1")
        elif decision in c:
            print("You selected Change Pop")
            display_statistics(pop_change, "Change Pop")
        elif decision in d:
            print("Exiting column....")
            return
        else:
            print("Invalid choice")

def housing_data():
    '''Display menu for housing data'''
    housing = pd.read_csv('Housing.csv')
    print("You have entered Housing Data.")
    print("a. AGE")  # column 0
    print("b. BEDRMS")  # column 1
    print("c. BUILT")  # column
    print("d. ROOMS")
    print("e. UTILITY")
    print("f. Exit Column")

    while True:
        decision = input("Select the Column you want to analyze:")

        if decision in a:
            print("You selected AGE")
            display_statistics2(housing, "AGE")
        elif decision in b:
            print("You selected BEDRMS")
            display_statistics2(housing, "BEDRMS")
        elif decision in c:
            print("You selected BUILT")
            display_statistics2(housing, "BUILT")
        elif decision in d:
            print("You selected ROOMS")
            display_statistics2(housing, "ROOMS")
        elif decision in e:
            print("You selected UTILITY")
            display_statistics2(housing, "UTILITY")
        elif decision in f:
            print("Exiting column....")
            return
        else:
            print("Invalid choice")

        #display_statistics()
def main_method():
    """
    the main method of program operation
    :return:
    """
    choice = 0

    while choice != 3:
        display_menu()

        choice = input("Select an Option:")
        print("\n")

        if choice.isdigit():
            choice = int(choice)

        if choice == 1:
            population_data()
        elif choice == 2:
            housing_data()
        elif choice == 3:
            print("*************** Thanks for using the Data Analysis App**********\n")
        else:
            print("Valid choices are 1-3!\n")


main_method()
