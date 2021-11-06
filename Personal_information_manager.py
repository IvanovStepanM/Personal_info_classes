##Personal_information## this program manages 3 instances of personal information
##It uploads menu from user_interface file and contains instructions for entered commands.

import pickle                           # technical imports

import Personal_information       # imports of *.py files from working directory
from user_interface import user_interface
# Global constants for menu choices
#ADD = 1
LOOK_UP = 1
CHANGE = 2
QUIT = 3

# Global constant for the filename
FILENAME = '3PI.dat'

def main():                             ## main function loads infos and checks user's menu choice
    info = load_info()              # loads infos from data file
    choice = 0 # variable for user's choice

    while choice != QUIT:               
        choice = user_interface.get_menu_choice()   # loads user interface from user_interface.py
        if choice == LOOK_UP:               # here it checks what user have entered
            look_up(info)                # and calls for a function to execute. In this case - to show info by ID.
        #elif choice == ADD:                 # Here- to add a new info
        #    add(info)
        #    save_info(info) # save a new info to the file
        elif choice == CHANGE:
            change(info)
            save_info(info) # save changed info to the file

        

# now we define all the functions listed above as actions from the menu related to the infos


def load_info():       # This function loads infos from a database
    try:
        input_file = open(FILENAME, 'rb') # open the infos file (binary, reading)
        info_dct = pickle.load(input_file)
        input_file.close()
    except IOError: # if can't open the file
        info_dct = {} # then create an empty dictionary
    return info_dct

def save_info(info):    # This function saves infos back to database.
    output_file = open(FILENAME, 'wb') # writing, binary code
    pickle.dump(info, output_file) # pickle the dictionary and save it.
    output_file.close()

def look_up(info): # show info
        print("[1] My information, [2] Friend's information, [3] Grandfather's information")
        #print(list(info))
        try:
            id = int(input('Enter a number to show some information: '))
            if id in info:
                if id == 1:
                    print("Here's your personal information:")
                elif id == 2:
                    print("Here's your friend's personal information:")
                elif id == 3:
                    print("Here's your grandfather's personal information:")
            print(info.get(id, 'no information found'))
        except ValueError:
            print('You have entered an empty string or non-integer value.')

def change(info):                    # This function changes the existing info.
    print("[1] My information, [2] Friend's information, [3] Grandfather's information")
    try:
        id = int(input('Enter 1 or 2 or 3: '))  # by its ID.

        name = input('Name:') # user inputs
        address = input('Address:')
        age = input('Age:')
        phonenumber = input('Phone_number:')
        entry = Personal_information.Personal_information(id, name, address, age, phonenumber) # creates a Personal_information instance.
        info[id] = entry
        print('Information updated.')
    except ValueError:
        print('You have entered an empty string or non-integer value.') 

#def add(info):   # This function adds a new info.
#    name = input('Name:') # user inputs title for a new info
#    address = input('Address:')
#    age = input('Age:')
#    phonenumber = input('Phone_number:')
#    id = 1

#    #name = "Your_name"
#    #address = "Your_address"
#    #age = "Your_age"
#    #phonenumber = "Your_number"
#    #id = 3

#    entry = Personal_information.Personal_information(id, name, address, age, phonenumber) # create info object
#    info[id] = entry
#    print('Personal information was saved.')


main()