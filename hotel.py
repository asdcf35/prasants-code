# created by : Prasant Neupane
# created date : 5/8/10:55
# version = '1.0'
#-------------------------
""" This code is a simple way for the user to book a hotel room at the theme park """
#-------------------------
# Built in Imports
#-------------------------
# User made Imports
#-------------------------


import time # import time from the built in modules
import random # import random from the built in modules

def room(): # makes a function called room
    """ a check in for a hotel where you  book the room, see the price and see your room number"""
    while True:# works while the loop is True
        try:
            print("hello, welcome to the best hotel in the world")
            time.sleep(.5) # pauses the code for .5 second

            name = input("what is your name? \n").lower() # ask the user for their name

            while name == "": # while loop works if the user didn't enter anything
                print("you did not enter your name")
                name = input("what is your name? \n") # ask the user for the name again if they didn't enter it

            print("Hello", name.title() , ", welcome to the best hotel in the world") # welcome the user 
            age = int(input("Please, verify your age: ")) # asks for users age
            if age < 18: # works if age is less than 18
                print("GET THE HELL OUT OF HERE " + name.title() + " YOU NEED A ADULT!!!!!!!!!!!")
                quit() # ends the code

            else: # works if the age is higher than 18
                print("Hello", name.title() , ", welcome to the best hotel in the world")

            stay = int(input("How many days are you gonna stay in this hotel? \n "))
            # ask the user for the amount of days they are going to stay


            random_number = random.randint(1, 200) # sets a variable as a random number between 1 and 200



            print("\n")

            room_option = int(input("which room option would you like to choose: \n 1. normal 1 beds - $100\n 2. normal 2 beds - $150 \n 3. suite - $400 \n 4.deluxe room - $1000 \n please choose which room you would like: "))
            # asks the user to choose one of the room options and turns the user input to int
            time.sleep(2) # pauses the code for 2 seconds
            
            price = 0 # sets price to 0

                
            if room_option == 1: # works if user choose option 1
                price += 100 * stay # sets price to 100 times the stay

            elif room_option == 2: # works if user choose option 2
                price += 150 * stay # sets price to 150 times the stay

            elif room_option == 3: # works if user choose option 3
                price += 400 * stay # sets price to 400 times the stay

            elif room_option == 4: # works if user choose option 4
                price += 1000 * stay # sets price to 1000 times the stay
            else:
                raise ValueError
    
                
            time.sleep(1) # pauses the code for 1 second
            room = int(random_number) # sets room to int random_number

            floor = 0 # sets floor to 0
            if 1 <= random_number <= 50: # works if the random_number is between 1 and  less than 50
                floor = 1 # sets floor to 1
            elif 50 < random_number <= 100: # works if the random_number is between 50 and less than 100
                floor = 2 # sets floor to 2
            elif 100 < random_number <= 150: # works if the random_number is between 100 and less than 150
                floor = 3 # sets floor to 3
            elif 150 < random_number <= 200: # works if the random_number is between 150 and less than 200
                floor = 4 # sets floor to 4
            

            time.sleep(1) # pauses the code for 1 second

            print("you are going to stay for {0} days\n your room number is {1} floor:{2}\n your total price is {3} ".format(stay, room, floor, price))
            # uses string formatter to print the all the information about the room and te price
            quit2 = input('Do you want to go back to the main page (y/n): ') # asks user if they want to go back to the main page
            if quit2.lower() != 'n': # if the quit2 is not equal to n
                break # breaks the whole function
        except ValueError:
            print("Value is invalid, please try again")
            time.sleep(1)