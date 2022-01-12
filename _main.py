from school import School
from school_class import School_class
from student import Student

from save_load import save_json
from save_load import load_json

current_school = School()

# some notes

def _quit():
    quit()

def _anykey_continue():
    temp = input('\nPress any key to go back to main menu: ')

def _print_main_menu():
    print('\nMain menu')
    print('Options:')
    print('[1] - Add a class')
    if len(current_school.list_classes) > 0:
        print('[2] - List all classes')
        print('[3] - Remove a class')
        print('[4] - Statistics')
    print('[8] - Load from file')
    print('[9] - Save to file')
    print('[0] - Quit program')

def _main_menu(): 
    _print_main_menu()
    while True:
        user_input = str(input('\nEnter option number: '))
        try:
            user_input = int(user_input)
            if user_input == 0:
                _quit()
            elif user_input == 1:
                current_school.add_class(input('\nEnter class name (max 10 symbols): '))
                _print_main_menu()
            elif user_input == 2 and len(current_school.list_classes) > 0:
                current_school.print_all_classes()
                _anykey_continue()
                _print_main_menu()
            elif user_input == 3 and len(current_school.list_classes) > 0:
                current_school.remove_class(input('\nEnter class name: '))
                _anykey_continue()
                _print_main_menu()
            elif user_input == 4 and len(current_school.list_classes) > 0:
                current_school.print_classes_by_grade()
                _anykey_continue()
                _print_main_menu()
            elif user_input == 8:
                #global current_school
                #current_school = School()
                current_school = load_json()
                _anykey_continue()
                _print_main_menu()
            elif user_input == 9:
                save_json(current_school)
                _anykey_continue()
                _print_main_menu()
            else:
                print('   This is not a valid entry!')
        except ValueError:
            print('   This is not a valid entry!')

print('\nWellcome')
_main_menu()

