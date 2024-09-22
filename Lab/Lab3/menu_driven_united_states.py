"""Welcome to the United STates Python Program"""
import os
import sys
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


# Global Variables
states_dict = {'Alabama': ["Montgomery", "Camellia", 4908620],
               'Alaska': ["Juneau", "Forget Me Not", 734002],
               'Arizona': ["Phoenix", "Saguaro Cactus Blossom", 7378490],
               'Arkansas': ["Little Rock", "Apple Blossom", 3039000],
               'California': ["Sacramento", "California Poppy", 39937500],
               'Colorado': ["Denver", "White and Lavender Columbine", 5845530],
               'Connecticut': ["Juneau", "Hartford", 3563080],
               'Delaware': ["Dover", "Peach Blossom", 982895],
               'Florida': ["Tallahassee", "Orange Blossom", 21993000],
               'Georgia': ["Atlanta", "Cherokee Rose", 10736100],
               'Hawaii': ["Honolulu", "Hibiscus", 1412690],
               'Idaho': ["Boise", "Syringa", 1826160],
               'Illinois': ["Springfield", "Purple Violet", 12659700],
               'Indiana': ["Indianapolis", "Peony", 6745350],
               'Iowa': ["Des Moines", "Wild Prairie Rose", 3179850],
               'Kansas': ["Topeka", "Sunflower", 2910360],
               'Kentucky': ["Frankfort", "Goldenrod", 4499690],
               'Louisiana': ["Baton Rouge", "Magnolia", 4645180],
               'Maine': ["Augusta", "White Pine Cone and Tassel", 1345790],
               'Maryland': ["Annapolis", "Black-Eyed Susan", 6083120],
               'Massachusetts': ["Boston", "Mayflower", 6976600],
               'Michigan': ["Lansing", "Apple Blossom", 10045000],
               'Minnesota': ["Saint Paul", "Pink and White Lady Slipper", 5700670],
               'Mississippi': ["Jackson", "Magnolia", 2989260],
               'Missouri': ["Jefferson City", "White Hawthorn Blossom", 6169270],
               'Montana': ["Helena", "Bitterroot", 1086760],
               'Nebraska': ["Lincoln", "Goldenrod", 1952570],
               'Nevada': ["Cason City", "Sagebrush", 3139660],
               'New Hampshire': ["Concord", "Purple Lilac", 1371250],
               'New Jersey': ["Trenton", "Violet", 8936570],
               'New Mexico': ["Santa Fe", "Yucca Flower", 2096640],
               'New York': ["Albany", "Rose", 19440500],
               'North Carolina': ["Raleigh", "Dogwood", 10611900],
               'North Dakota': ["Bismarck", "Wild Prairie Rose", 761723],
               'Ohio': ["Columbus", "Scarlet Carnation", 11747700],
               'Oklahoma': ["Oklahoma City", "Mistletoe", 3954820],
               'Oregon': ["Salem", "Oregon Grape", 4301090],
               'Pennsylvania': ["Harrisburg", "Mountain Laurel", 12820900],
               'Rhode Island': ["Providence", "Violet", 1056160],
               'South Carolina': ["Columbia", "Yellow Jessamine", 5210100],
               'South Dakota': ["Pierre", "Pasque Flower", 903027],
               'Tennessee': ["Nashville", "Iris", 6897580],
               'Texas': ["Austin", "Bluenonnet", 29472300],
               'Utah': ["Salt Lake City", "Sego Lily", 3282120],
               'Vermont': ["Montpelier", "Red Clover", 628061],
               'Virginia': ["Richmond", "Dogwood", 8626210],
               'Washington': ["Olympia", "Pink Rhododendron", 7797100],
               'West Virginia': ["Charleston", "Rhododendron", 1778070],
               'Wisconsin': ["Madison", "Wood Violet", 5851750],
               'Wyoming': ["Cheyenne", "Indian Paintbrush", 567025]}


def display_menu():
    """
    display the main menu for program
    :return:
    """
    print("===================== Menu =====================")
    print("1. Display all U.S States in Alphabetical order.")
    print("2. Look up a specific state.")
    print("3. Display bar graph of top 5 populated states.")
    print("4. Update a state's overall population.")
    print("5. Exit program.")
    print("================================================\n")


def display_alphabetical():
    """
    display all states in alphabetical order
    :return:
    """
    print("U.S State's in Order:")

    print("|{0: >15}|{1: >15}|{2: >30}|{3: >15}|".format("______State______", "_____Capital_____",
                                                         "__________State Flower__________", "___Population____"))

    for key, value in states_dict.items():
        print("| {0: >15} | {1: >15} | {2: >30} "
              "| {3: >15} |".format(key, value[0], value[1], value[2]))

    print("\n")


def display_state():
    """
    display a given state's data
    :return:
    """
    while True:
        state = input("Enter a U.S state's name to display data:")
        # make first letter capital, rest of letters lowercase
        state_data = states_dict.get(state)

        if state_data is not None:
            print(state + ": Capital=" + state_data[0] +
                  ", Flower=" + state_data[1] + ", Population=" + str(
                      state_data[2]) + "\n")
            flower_img = mpimg.imread(os.getcwd() + '/State Flower Images' + '/' + state + '.jpg')
            plt.imshow(flower_img)
            plt.show()
            break
        else:
            print("Invalid state entered! State's case sensitive!")


def display_graph():
    """
    display bar graph of 5 most populated states
    :return:
    """

    states_found = []  # hold 5 most populated states and pop value
    values = []

    for i in range(0, 5):
        states_found.append(find_largest_pop_state(states_found))
# find largest pop state
        values.append(states_dict.get(states_found[i])[2])
# append pop values

    plt.figure(figsize=(9, 3))

    plt.bar(states_found, values)
    plt.suptitle('Top 5 Most Populated States')
    plt.show()


def update_population():
    """
    update given state's overall population data
    :return:
    """
    while True:
        state = input("Which state's population do you wish to update?")
        state_data = states_dict.get(state)

        if state_data is not None:
            print("Original population: " + str(state_data[2]))
            new_pop = input("Enter new population: ")
            if new_pop.isdigit():
                state_data[2] = new_pop
                print("Population successfully changed!\n")
                break
            else:
                print("Invalid population! Must be positive integer.\n")
        else:
            print("Invalid state! State is case sensitive ex. 'Alabama'\n")


def find_largest_pop_state(states_found):
    """
    find the largest populated state excluding
    states given in states_found
    :param states_found:
    :return: tuple (most pop state, population)
    """
    max_state = 'Alabama'
    for state in states_dict:
        if state not in states_found and states_dict.get(max_state)[2] < states_dict.get(state)[2]:
            max_state = state

    return max_state


def main_method():
    """
    the main method of program operation
    :return:
    """
    choice = 0

    print("Welcome to my program!\n")

    # Change directory to that of this script
    # Necessary when running from python shell
    path_of_file = os.path.abspath(os.path.dirname(sys.argv[0]))
    # os.path.dirname(os.path.abspath(__file__))
    # print(path_of_file)

    if os.getcwd() != path_of_file:
        os.chdir(path_of_file)
    while choice != 5:
        display_menu()

        choice = input("Select an Option:")
        print("\n")

        if choice.isdigit():
            choice = int(choice)

        if choice == 1:
            display_alphabetical()
        elif choice == 2:
            display_state()
        elif choice == 3:
            display_graph()
        elif choice == 4:
            update_population()
        elif choice == 5:
            print("Exiting program.\n")
        else:
            print("Valid choices are 1-5!\n")


main_method()
