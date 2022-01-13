from school import School
from school_class import School_class
from student import Student

from save_load import save_json
from save_load import load_json

import utilities


current_school = School()

# some notes

def _quit():
    save_json(current_school)
    print('\nGoodbye!\n')
    quit()

def _anykey_continue():
    temp = input('\nPress enter to go back to main menu... ')

def _print_main_menu():
    print('\nMain menu')
    print('Options:')
    print('[1] - Add a class')
    if len(current_school.list_classes) > 0:
        print('[2] - List all classes')
        #print('[3] - Remove a class')
        #print('[4] - Statistics')
        #print('[5] - ')
        #print('[6] - ')
        print('[7] - Statistics')
    print('[8] - Load from file')
    print('[9] - Save to file')
    print('[0] - Quit program')

def _print_class_menu():
    print('\nOptions:')
    print('[1] - List classes again')
    if current_school.list_classes:
        print('[2] - Open class')
    print('[3] - Add a class')
    if current_school.list_classes:
        print('[4] - Remove a class')
        #print('[5] - Rename a class')
    print('[0] - Back to main menu')

def _print_student_menu(populated:bool):
    print('\nOptions:')
    print('[1] - List students again')
    print('[2] - Add new student')
    if populated:
        print('[3] - Add a grade to a student')
        print('[4] - Remode a student')
    print('[0] - Back to list of classes')

def _print_statistic_menu():
    print('\nOptions:')
    print('[1] - School statistic')
    print('[2] - List classes by average grade')
    print('[3] - List classes by average age')
    print('[4] - List top students')
    print('[5] - List gender by average grade')
    print('[0] - Back to main menu')

def _main_menu():
    global current_school
    _print_main_menu()
    while True:
        user_input = str(input('\nEnter option number: '))
        try:
            user_input = int(user_input)
            if user_input == 0:
                _quit()
            elif user_input == 1:
                # add a new class
                current_school.add_new_class(input('\nEnter class name (max 10 symbols): '))
                _print_main_menu()
            elif user_input == 2 and len(current_school.list_classes) > 0:
                # print list of all classes
                # show class edit menu
                current_school.print_all_classes()
                _class_menu()
                _print_main_menu()
            # elif user_input == 3 and len(current_school.list_classes) > 0:
            #     current_school.remove_class(input('\nEnter class name: '))
            #     _anykey_continue()
            #     _print_main_menu()
            # elif user_input == 4 and len(current_school.list_classes) > 0:
            #     current_school.print_all_classes()
            #     _anykey_continue()
            #     _print_main_menu()
            elif user_input == 7 and current_school.list_classes:
                # some statistics
                _statistic_menu()
                _print_main_menu()
            elif user_input == 8:
                if load_json() is School:
                    current_school = load_json()
                _anykey_continue()
                _print_main_menu()
            elif user_input == 9:
                save_json(current_school)
                #_anykey_continue()
                #_print_main_menu()
            else:
                print('   This is not a valid entry!')
        except ValueError:
            print('   This is not a valid entry!')

def _class_menu():
    _print_class_menu()
    while True:
        user_input = str(input('\nEnter option number: '))
        try:
            user_input = int(user_input)
            if user_input == 0:
                # back to previous menu
                break
            if user_input == 1:
                # list classes again
                current_school.print_all_classes()
                _print_class_menu()
            elif user_input == 2 and current_school.list_classes:
                # open class for editing
                name = input('\nEnter class name: ')
                if name in [x.name for x in current_school.list_classes]:
                    for sch_class in current_school.list_classes:
                        if sch_class.name == name:
                            sch_class.print_grades()
                            _student_menu(sch_class, bool(sch_class.list_students))
                            break
                    break
                else:
                    print('There is no class with that name!')
                _print_class_menu()
            elif user_input == 3:
                # add a new class
                current_school.add_new_class(input('\nEnter class name (max 10 symbols): '))
                _print_class_menu()
            elif user_input == 4 and current_school.list_classes:
                # remove a class
                while True:
                    name = input('\nEnter class name to be removed: ')
                    if name in [x.name for x in current_school.list_classes]:
                        current_school.remove_class(name)
                        break
                    else:
                        print('There is no class with that name!')
                _anykey_continue()
                _print_class_menu()
            else:
                print('   This is not a valid entry!')
        except ValueError:
            print('   This is not a valid entry!')

def _student_menu(sch_class:School_class, populated:bool):
    _print_student_menu(populated)
    while True:
        user_input = str(input('\nEnter option number: '))
        try:
            user_input = int(user_input)
            if user_input == 0:
                # back to previous menu
                break
            if user_input == 1:
                # list students again
                sch_class.print_grades()
                _print_student_menu(populated)
            elif user_input == 2:
                # add new student
                sch_class.add_new_student(
                    input('Enter student name (max 20 characters): '), 
                    int(input('Enter student age: ')), 
                    input('Enter student gender (boy/girl): ')
                    )
                print(f'Student added to class {sch_class.name}.')
                _print_student_menu(populated)
            elif user_input == 3:
                # add grade to a student
                while True:
                    name = input('Enter student name: ')
                    if name in [x.name for x in sch_class.list_students]:
                        for stud in sch_class.list_students:
                            if name == stud.name:
                                stud.add_grade(int(input('Enter grade: ')))
                                print(f'New grade added to {name}.')
                                break
                        break
                    else:
                        print('There is no student with that name!')
                _print_student_menu(populated)
            elif user_input == 4:
                # remove a student
                while True:
                    name = input('Enter student name: ')
                    if name in [x.name for x in sch_class.list_students]:
                        for stud in sch_class.list_students:
                            if name == stud.name:
                                sch_class.list_students.remove(stud)
                                print(f'Student {name} removed from class {sch_class.name}.')
                                break
                        break
                    else:
                        print('There is no student with that name!')
                _print_student_menu(populated)
            else:
                print('   This is not a valid entry!')
        except ValueError:
            print('   This is not a valid entry!')

def _statistic_menu():
    _print_statistic_menu()
    while True:
        user_input = str(input('\nEnter option number: '))
        try:
            user_input = int(user_input)
            if user_input == 0:
                # back to previous menu
                break
            if user_input == 1:
                # School statistic
                print('\nSchool statistics:')
                print('Number of classes'.ljust(35), len(current_school.list_classes))
                print('Number of all students'.ljust(35), sum([len(x.list_students) for x in current_school.list_classes]))
                print('Average grade of all classes'.ljust(35), round(sum([x.get_average for x in current_school.list_classes])/len(current_school.list_classes),2))
                print('Average grade of all students'.ljust(35), 'missing')
                print('Average age of all students'.ljust(35), 'missing')
                print('Number of boys'.ljust(35), 'missing')
                print('Number of girls'.ljust(35), 'missing')
                print('')
                _anykey_continue()
                _print_statistic_menu()
            if user_input == 2:
                # List classes by average grade
                print('- not implemented yet -')


                _print_statistic_menu()
            if user_input == 3:
                # List classes by average age
                print('- not implemented yet -')


                _print_statistic_menu()
            if user_input == 4:
                # List top students
                print('- not implemented yet -')


                _print_statistic_menu()
            if user_input == 5:
                # List gender by average grade
                print('- not implemented yet -')


                _print_statistic_menu()
            else:
                print('   This is not a valid entry!')
        except ValueError:
            print('   This is not a valid entry!')



print('\nWellcome')
_main_menu()

