class user_interface(): # Prints out menu options and accepts the command from user to transfer back to the notes_manager.


    def get_menu_choice():
        print('------------------------------------------------------')
        print('Menu')
        print('---------------------------')
        #print('1. Add an instance')
        print('1. Show personal data')
        print('2. Edit personal data')
        print('3. QUIT the program')
        print()

        #Get the user's choice.
        while True:
            try:
                choice = int(input('Enter your choice: '))
                print('______________________________________________________')
                return choice
            except ValueError: # in case user writes non integer value
                print('Please type a number from menu options.')

#get_menu_choice()