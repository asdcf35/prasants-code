# created by : Prasant Neupane
# created date : 5/3/24 11:00
# version = '1.0'
#-------------------------
""" This code is a simple way to choose what you want to do in the themepark """
#-------------------------
# Built in Imports
import time
#-------------------------
# User made Imports
from rides import rides_main
from general import general_main 
from concession import food
from hotel import room
#-------------------------

#password loop
while True:

    password = input('Enter the password "abc" to enter: \n')

    if password == "abc":
        break

    print("You did not enter the right password.")
    print("Please try again.")

#main loop code
while True:

    print("Hello, welcome to the Monkey theme park")
    time.sleep(2)

    print("1. General \n2. Rides \n3. Concession \n4. Hotel\n5. Exit\n\n")

    choose = int(input("Where would you like to go? (Choose a number): "))

    if choose == 1:
        pass
    elif choose == 2:
        print("Going to rides...")
        time.sleep(1)
        rides_main()
    elif choose == 3:
        print("going to concessions...")
        time.sleep(1)
        food()
    elif choose == 4:
        print("Going to the hotel...")
        time.sleep(1)
        room()
    elif choose == 5:
        print("Exiting the theme park")
        break
    else:
        print("You did not select the right number.")
