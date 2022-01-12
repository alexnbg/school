from school import School
from school_class import School_class
from student import Student


current_school = School()

# some notes

def _quit():
    quit()


def _print_main_menu():
    print('\nOptions:')
    print('[1] - Add a class')
    if len(current_school.list_classes) > 0:
        print('[2] - List all classes')
        print('[3] - Remove a class')
    print('[0] - Quit program')

def _main_menu(): 
    while True:
        user_input = str(input('Enter option number: '))
        try:
            user_input = int(user_input)
            if user_input == 0:
                _quit()
            elif user_input == 1:
                current_school.add_class(input('Enter class name: '))
                _print_main_menu()
            elif user_input == 2 and len(current_school.list_classes) > 0:
                print('2')
            elif user_input == 3 and len(current_school.list_classes) > 0:
                print('3')
            else:
                print('   This is not a valid entry!')
        except ValueError:
            print('   This is not a valid entry!')






print('\nWellcome')
_print_main_menu()
_main_menu()

