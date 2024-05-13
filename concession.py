# created by : Prasant Neupane
# created date : 5/7/10:45
# version = '1.0'
#-------------------------
""" This code is a simple way to ask the user what food stalls, and concession stands they want to go on"""
#-------------------------
# Built in Imports
import time
#-------------------------
# User made Imports
#-------------------------


def food():
    """ prints the concession and location of each concession and the menu and price for each item in the concession"""
    
    #the main loop of the code
    while True:
        try:
            print("here are a list of concessions for food& drinks in the themepark: ")

            #create list that shows all the concessions
            concessions = ['one piece donuts', 'burger town' , 'smoothie heaven', 'nepali place', ' sweet cakes', 'lovely foods']

            #print all concessions and their indexes(off by 1) 
            for index, concession in enumerate(concessions, 1):
                print(f"{index}. {concession}")
            
            #ask user for which place they want to go to(using numbers)
            user = int(input(f" which place would you like to go to?(enter a number): "))

            #raise a ValueError if the number user inputted would be larger than the length of the list
            if user > len(concessions):
                raise ValueError 
            print("\n")

            #store all locations into a tuple called location(every concession has a corresponding location at the same index) 
            location = ('next to the one piece ride' , 'front of the scenic river cruise', 'behind the regurgitator', 'right of tilt a whirl','behind the monkey run','next to the carvinal carousel') 

            #access the location of the concessions and the locations using the input given by the user(off by 1)
            print(f"the location for {concessions[user-1]} is: {location[user-1]}\n ")
        
            time.sleep(2)
            print(f"you are arriving to: {concessions[user-1]}\n")

            #stores all menus to menu(every concession has a corresponding menu at the same index)      
            menu = [('ace fire donut - $2.69', 'luffy lemon donut - $2.70', 'rengoku donut - $2.89', 'zoro sword donut - $2.49', 'sharingan red donut - $2.50'),
                    ('veggie burger - $2.78', 'burger momo - $4.58', 'burger fries - $2.58', 'burger fried rice - $4.99', 'chicken burger - $3.48',' goat burger - $6.38'),
                    ('strawberry smoothie - $3.58 ', 'chocolate smoothie - $4.39',' banana smoothie - $2.59', 'fruit mix smoothie - $4.78', 'vanilla smoothie - $3.98'),
                    ('pani puri - $5.78', 'samosa - $2.99', 'chicken momo - $15.99' , 'dal bhat - $10.99', 'roti tarkari - $7.89', 'veg momo - $9.99'),
                    ('strawberry cake - $20.99', 'cookie& cream cake - $19.99', 'red velvet cake - $25.99', 'coconut cake - $15.99', 'vanilla cake - $17.99'),
                    ('lovely fried chicken - $15.99', 'lovely momo - $10.99', 'lovely pork chop - $20.99', 'lovely steak - $25.99', 'lovely soup - $7.99')]
            
            #print every item in the menu
            print(f"Here is the menu for {concessions[user-1]}\n\n") 
            for item in menu[user-1]:
                print(item)

            #check if the user wants to go back to the main page
            quit2 = input('Do you want to go back to the main page (y/n): ')
            if quit2.lower() != 'n':
                return None 
        except ValueError:
            print("Invalid value, please try again")
            time.sleep(1)
