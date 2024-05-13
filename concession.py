# created by : Prasant Neupane
# created date : 5/7/10:45
# version = '1.0'
#-------------------------
""" This code is a simple way to ask the user what food stalls, and concession stands they want to go on"""
#-------------------------
# Built in Imports
#-------------------------
# User made Imports
#-------------------------
import time #imports time from Built in modules
def food(): # makes a function called food
    """ prints the concession and location of each concession and the menu and price for each item in the concession"""
    while True: # works while the loop is True

        print("here are a list of concessions for food& drinks in the themepark: ")
        concessions = ['one piece donuts', 'burger town' , 'smoothie heaven', 'nepali place', ' sweet cakes', 'lovely foods']
        # makes a list of all the concessions in the theme park 
        for index, concession in enumerate(concessions, 1): # uses for loop and enumerate to make the concessions a list
            print(f"{index}. {concession}") # puts the concessions in a list when printing
        user = int(input(f" which place would you like to go to?(enter a number): "))
        # asks the user where they want to go and turn user input into int
        print("\n")
        
        location = ('next to the one piece ride' , 'front of the scenic river cruise', 'behind the regurgitator', 'right of tilt a whirl','behind the monkey run','next to the carvinal carousel') 
        # makes a tuple of all the locations
            
        print(f"the location for {concessions[user-1]} is: {location[user-1]}\n ")
        # prints the location of concession accordingly using the index
        time.sleep(2) # pauses the code for 2 second
        print(f"you are arriving to: {concessions[user-1]}\n") # print the concession using index
        
        
        menu = [('ace fire donut - $2.69', 'luffy lemon donut - $2.70', 'rengoku donut - $2.89', 'zoro sword donut - $2.49', 'sharingan red donut - $2.50'),
                ('veggie burger - $2.78', 'burger momo - $4.58', 'burger fries - $2.58', 'burger fried rice - $4.99', 'chicken burger - $3.48',' goat burger - $6.38'),
                ('strawberry smoothie - $3.58 ', 'chocolate smoothie - $4.39',' banana smoothie - $2.59', 'fruit mix smoothie - $4.78', 'vanilla smoothie - $3.98'),
                ('pani puri - $5.78', 'samosa - $2.99', 'chicken momo - $15.99' , 'dal bhat - $10.99', 'roti tarkari - $7.89', 'veg momo - $9.99'),
                ('strawberry cake - $20.99', 'cookie& cream cake - $19.99', 'red velvet cake - $25.99', 'coconut cake - $15.99', 'vanilla cake - $17.99'),
                ('lovely fried chicken - $15.99', 'lovely momo - $10.99', 'lovely pork chop - $20.99', 'lovely steak - $25.99', 'lovely soup - $7.99')]
        # makes a list of tuple with menu and the price of each item i the concessions
                
        print(f"Here is the menu for {concessions[user-1]}\n\n") 
        for item in menu[user-1]: # uses for loop and index to print the menu for the right concession
            print(item)

        quit2 = input('Do you want to go back to the main page (y/n): ') # asks the user if they want to go back to the main page
        if quit2.lower() != 'n': # if the quit2 is not equal to n
            return None  # breaks the whole function

            

