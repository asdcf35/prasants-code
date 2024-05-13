# created by : Prasant Neupane
# cracyed date : 12/3/11:15
# version = '1.0'
#-------------------------
""" This code is a simple way to pick which ride you on the theme park """
#-------------------------
# Built in Imports
#-------------------------
# User made Imports
#-------------------------

def rides_main(): # makes a function called rides_main
    """ prints all the rides and the user can go on the ride according to their age and gives the description of each rides """
    while True: # works while the loop is True
        try:
            print("""\n\nthese are the available rides:\n
            1. Scenic River Cruise
            2. Carnival Carousel
            3. Jungle Adventure Water Splash
            4. Downhill Mountain Run
            5. The Regurgitator
            6. Monkey Run
            7. Dark ride
            8. Tilt a Whirl
            9. the one piece
            10. dark reunion
            11. Exit to main page""")
            # uses doc string to print all the ride names
            ride = int(input("What ride do you want to go on (enter the number): "))# asks the user, what ride they want to go on
            
            #raise ValueError if the ride number is larger than 12
            if ride > 12:
                raise ValueError
            if ride == 11: # works if user choose ride 11
                return None # ends the entire function
            
            
            if ride == 1: # works if user choose ride one
                print("you have selected Scenic River Cruise\n")
                print("step right up for this amazing ride called Scenic River Cruise, where you will  experience what cruising on a high tide river feels like. You will be placed in a boat and you will go through water. You will go up and down the water at a high speed.")
                quit2 = input('Do you want to go back to the main page (y/n): ')# asks user if they want to go back to the main page
                return None
            
            age = int(input("Please, verify your age: ")) #asks the user for their age

            if ride == 2: # works if user choose ride two
                print("you have selected Carnival Carousel\n")

                if age >= 3: # works if the age is greater than 3
                    print("you meet the requirement for this ride\n")
                    print("step right up for this amazing ride called Carnival Carousel. the carousel begins with a a magic rotation, the sky fills with stars. You see yourself riding a  horse while you looking at the wonderful night sky")
                else: # works if age is not greater than 3
                    print("Sorry you dont meet the age requirement for this ride")
            elif ride == 3: # wrks if user choose ride three
                print("you have selected Jungle Adventure Water Splash\n")
                if age >= 6: # works if the age is greater than 6
                    print("you meet the age requirement to go on this ride\n")
                    print("step right up for this amazing ride called Jungle Adventure Water Splash. This ride you explore the Jungle of amazon while going down the water fall, you see a lot of snakes trying to bite you but dont worry they are fake. Make sure you have a swimsuit because you will get wet")
                else:# works if age is not greater than 6
                    print("Sorry you dont meet the age requirement for this ride")
            elif ride == 4: # wrks if user choose ride four
                print(" you have selected Downhill Mountain Run.")
                if age >= 12: # works if the age is greater than 12
                    print("you meet the age requirement to go on this ride\n")
                    print("step right up for this amazing ride called downhill mountain run. This ride is full of happiness but not if your afraid of hights. In this ride you will go up a mountain and fall down. While going down you will see many things such as clouds")
                else: # works if age is not greater than 12 
                    print("Sorry you dont meet the age requirement for this ride")
            elif ride == 5: # wrks if user choose ride five
                if age >= 12 and age <= 70: # works if the age is greater than 12 and less than 70
                    print("you meet the age requirement to go on this ride\n")
                    print("step right up for this amazing ride called the regurgitator. This ride you will go on a ride that spins arounds the sky. It moves at a very high speed, up on the sky. Make sure all your items are safe because they might fall off the ride")    
                else:  # works if the age is not greater than 12 and less than 70
                    print("Sorry you dont meet the age requirement for this ride")
                    
            elif ride == 6: # wrks if user choose ride six
                print(" you have selected Monkey Run\n")
                if age >= 3 and age <= 21: # works if the age is greater than 3 and less than 21
                    print("you meet the age requirement to go on this ride\n")
                    print("step right up for this amazing ride called Monkey Run. This ride you go through the forst in a rollercoaster, you will see a lot of monkeys on the forest. Make sure to to keep all your items hidden because monkeys wil steal it")

                else: # works if the age is not greater than 3 and less than 21
                    print("Sorry you dont meet the age requirement for this ride")
            elif ride == 7: # wrks if user choose ride seven
                print(" you have selected Dark ride\n")
                if age >= 10 and age <= 30: # works if the age is greater than 10 and less than 30
                    print("you meet the age requirement to go on this ride\n")
                    print("step right up for this amazing ride called Dark Ride. In this ride you will go through a tunnel that is dark, you will be going at a very fast speed while oly being able to see darkness")
                else: # works if the age not is greater than 10 and less than 30
                    print("Sorry you dont meet the age requirement for this ride")
                
            elif ride == 8: # wrks if user choose ride eight
                print(" you have selected Tilt a Whirl\n")
                if age >= 18 and age <= 77: # works if the age is greater than 18 and less than 77
                    print("you meet the age requirement to go on this ride\n")
                    print("step right up for this amazing ride called Tilt a Whirl. In this ride you will go very high in the sky and be tilted on your side. and you have been tilted the ride will spin while you are on your side. ")
                else: # works if the age is not greater than 18 and less than 77
                    print("Sorry you dont meet the age requirement for this ride")    

            elif ride == 9: # wrks if user choose ride nine
                print(" you have selected the one piece\n")
            
                if age >= 3 and age <= 10: # works if the age is greater than 3 and less than 10
                    print("you meet the age requirement to go on this ride\n")
                    print("step right up for this amazing ride called  The one Piece. In this ride you will ride a big pirate ship and go on a adventure on the sea. You will see many creater, even a talking reindeer")

                else: # works if the age is not greater than 3 and less than 10
                    print("Sorry you dont meet the age requirement for this ride")

            elif ride == 10: # wrks if user choose ride ten
                print(" you have selected the one piece\n")
                if age >= 3 and age <= 10: # works if the age is greater than 3 and less than 10
                    print("you meet the age requirement to go on this ride\n")
                    print("step right up for this amazing ride called Dark reunion. In this ride you will spin round and round around a circle. you wont able able to see anything but you will be spinning")
                
                else: # works if the age is not greater than 3 and less than 10
                    print("Sorry you dont meet the age requirement for this ride")
    

            else: # works if user didnt put the valid number ride
                print("sorry that is not a valid ride")

            quit2 = input('Do you want to go back to the main page (y/n): ')# asks user if they want to go back to the main page
            if quit2.lower() != 'n':  # if the quit2 is not equal to n

                return None # breaks the whole function
        except ValueError:
            print("Value is invalid, please try again")
            time.sleep(1)