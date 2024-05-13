# created by : Prasant Neupane
# cracyed date : 5/6/10:50
# version = '1.0'
#-------------------------
""" This code is a simple way to tell the user all the rules and the operating hours of the themepark """
#-------------------------
# Built in Imports
#-------------------------
# User made Imports
#-------------------------

def rules():
    """prints the rules of the themepark and brings user back to main page if user chooses to """
    while True:
        print("""Here are the main rules in the theme park:
            1. No sprinting
            2. No littering/only throw food in the trash
            3. Keep hands, arms, legs, and feet inside the rides at all times
            4. No making out on the rides (Why would you do that? We have hotels available)
            5. Don't use cell phones on rides
            6. No one younger than 3 on any rides
            7. No one with health issues concerning heart issues
            8. No one older than 80 years old
            9. No motion sickness or dizziness
            10. No pregnant mothers""")

        quit2 = input('Do you want to go back to the main page? (y/n): ')

        if quit2.lower() != 'n':
            return None


def park_hours():
    """printd the operating hours of the theme park and brings user back to main page if user chooses to """
    print("""Here are the operating hours for the theme park:
        Saturday: 5:00 AM to 11:59 PM
        Sunday: 5:00 AM to 11:59 PM
        Monday to Thursday: 6:00 AM to 11:59 PM
        Friday: 6:00 AM to 11:59 PM""")
    quit2 = input('Do you want to go back to the main page? (y/n): ')
    if quit2.lower() != 'n':
        return None
        

