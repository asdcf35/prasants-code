# created by : Prasant Neupane
# created date : 5/3/11:00
# version = '1.0'
#-------------------------
""" This code is a simple way to choose what you want to do in the themepark """
#-------------------------
# Built in Imports
#-------------------------
# User made Imports
#-------------------------

import time # works time from the Built in modules

while True: # works while the loop is True
    password = input('Enter the password "abc" to enter: \n').lower() # asks the user for the password
    if password != "abc": # works if password is not equal to abc
        print("You did not enter the right password.")
        print("Please try again.") 
    else: # works if password is abc
        break # end the loop


while True: # works while the loop is True
    print("Hello, welcome to the Monkey theme park")
    time.sleep(2) # pauses the code for 2 seconds 
    print("1. General \n2. Rides \n3. Concession \n4. Hotel\n5. Exit\n\n")
    choose = int(input("Where would you like to go? (Choose a number): "))
    # ask the user where they want to go and turn user input to int

    if choose == 1: # works if user choose number one
        
            chosen = int(input('Do you want to see the rules or park hours? (Enter "1. rules" or "2. park hour"): '))
            # asks the user if they want to see rules or park hour and turn user input to int
            if chosen == 1: # works if user chose 1. rules
                print("Going to rules...")
                time.sleep(1) # pauses the code for 1 second
                from general import rules # from the user defined module general import the function rules
                rules() # call the function rules
            elif chosen == 2: # works if user chose 2. park hour
                print("Going to park hours...")
                time.sleep(1) # pause the time for 1 second
                from general import park_hours # from the user defined module general import the function park_hours
                park_hours() # call the function park_hours
            else: # works if user chose any number other than 1 or 2
                print("Invalid choice.")
                print("please try again")
                time.sleep(1)
                
    elif choose == 2: # works if user chose number 2 from choose
        print("Going to rides...")
        time.sleep(1)  # pause the time for 1 second
        from rides import rides_main # from the user defined module rides import the function rides_main
        rides_main()# call the function rides_main
    elif choose == 3: # works if user chose number 3 from choose
        print("going to concessions...")
        time.sleep(1) # pause the time for 1 second
        from concession import food  # from the user defined module concession import the function food
        food() # call the function rides_main
    elif choose == 4:  # works if user chose number 4 from choose
        print("Going to the hotel...")
        time.sleep(1) # pause the time for 1 second
        from hotel import room # from the user defined module hotel import the function room
        room() # call the function room
    elif choose == 5: # works if user chose number 5 from choose
        print("Exiting the theme park") 
        break # ends the loop
    else: # works if user choose any number other than 1-5
        print("You did not select the right number.")







