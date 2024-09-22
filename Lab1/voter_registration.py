"""Welcomes User to the Application"""
states = ["AL", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", "HI", "ID"
                                                                      "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
          "MA", "MI", "MN",
          "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND",
          "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT",
          "VT", "VA", "WA", "WV", "WI", "WY"]
yes = ["yes", "Yes", "YES", 'Y', 'y']
no = ["no", "No", "NO", 'N', 'n']


def main_method():
    print("Welcome to the Python Voter Registration Application!")
    # proceed is used to determine whether the user wants to continue with the application or not
    proceed = (input("Do you want to continue with Voter Registration?"))
    # Application continues if user says "Yes" or "yes" and terminates if users says anything else
    if proceed in yes:
        # User enters first name
        fname = (input("What's your first name?: "))
        # User enters last name
        lname = (input("What's your last name?: "))
        # used to determine whether the user wants to continue with the application or not
        proceed = input("Do you want to continue with Voter Registration?")
        # Application continues if user says "Yes" or "yes" and terminates if users says anything else
        if proceed in yes:
            # User enters age
            age = input("How old are you? (Type only number): ")

            if age.isdigit() is False:
                print("Age must be a positive integer!")
                return
            else:
                age = int(age)

            if age <= 120 and age >= 18:
                # used to determine whether the user wants to continue with the application or not
                proceed = input("Do you want to continue with Voter Registration?")
                # Application continues if user says "Yes" or "yes" and terminates if users says anything else
                if proceed in yes:
                    # Used to determine if user is U.S. citizen or not
                    citizen = (input("Are you a U.S. Citizen?: "))
                    # Application continues if user is a U.S. citizen
                    if citizen in yes:
                        # used to determine whether the user wants to continue with the application or not
                        proceed = input("Do you want to continue with Voter Registration?")
                        # Application continues if user says "Yes" or "yes" and terminates if users says anything else
                        if proceed in yes:
                            # asks user which state user lives in
                            state = input("Which state do you reside in?")
                            # program continues if and only if user enters a U.S. state in two letters
                            if state in states:
                                # used to determine whether the user wants to continue with the application or not
                                proceed = input("Do you want to continue with Voter Registration?")
                                # Application continues if user says "Yes" or "yes" and terminates if users says anything else
                                if proceed in yes:
                                    # asks user for zip code
                                    zipcode = input("What is your zip code?")
                                    if zipcode.isdigit() is False or len(zipcode) != 5:
                                        print("Zipcode is not valid. Must be only numbers and 5 digits long")
                                        return
                                    # Application thanks user for registration
                                    print("Thanks for registering to vote. "
                                          "Here is the information we received:")
                                    # Prints user information
                                    print("Name: " + fname + " " + lname + "\n" + "Age: " + str(age) +
                                          " Years Old" + "\n" + "U.S. Citizen:" + citizen + "\n" +
                                          "State: " + state + "\n" + "Zip Code: " +
                                          zipcode)
                                    # Thanks user for registration and notifies user of card shipment
                                    print("Congratulations! You are eligible to vote! "
                                          "Thanks for trying the Voter Registration Application. "
                                          "Your voter registration card "
                                          "should be shipped within 3 weeks.")
                                elif proceed in no:
                                    # ends program if user does not want to continue
                                    print("Okay. Have a nice day!")
                            elif state not in states:
                                # program terminates when user has inputted invalid input valid state
                                # in two letters
                                print("Sorry, Not a valid state!")
                        elif proceed in no:
                            # ends program if user does not want to continue
                            print("Okay. Have a nice day!")
                    elif citizen in no:
                        # program terminates if user is not U.S. citizen
                        print("Sorry, you have to be a U.S. Citizen or apply for citizenship")
                elif proceed in no:
                    # ends program if user does not want to continue
                    print("Okay. Have a nice day!")
            elif age < 18:
                # program will terminate if user's age does not meet requirements
                print("Sorry. You are not eligible to vote. You must be 18 years or older.")
            elif age > 120:
                print("Sorry, that age is much too high to register.")
        elif proceed in no:
            # ends program if user does not want to continue
            print("Okay. Have a nice day!")
    elif proceed in no:
        # ends program if user does not want to continue
        print("Okay. Have a nice day!")

main_method()
