from school import School
from school_class import School_class
from student import Student

import json



file_name = 'data.json'


def save_json(school:School):
    data = {}

    saved_classes = 0
    saved_students = 0

    if school.list_classes:
        for sch_class in school.list_classes:
            data[sch_class.name] = {}
            saved_classes += 1
            if sch_class.list_students:
                for student in sch_class.list_students:
                    data[sch_class.name][student.name] = {}
                    data[sch_class.name][student.name]['name'] = student.name
                    data[sch_class.name][student.name]['age'] = student.age
                    data[sch_class.name][student.name]['sex'] = student.sex
                    data[sch_class.name][student.name]['list_grades'] = student.list_grades
                    saved_students += 1

        with open(file_name, 'w') as outfile:
            json.dump(data, outfile, indent=4)
        
        print (f'\nSave successful! Saved {saved_classes} classes and {saved_students} students')

    else:
        print('\nNothing to save!')

def load_json():

    with open(file_name) as json_file:
        data = json.load(json_file)

    if data:
        current_school = School()

        loaded_classes = 0
        loaded_students = 0

        for key_c, value_c in data.items():
            new_class = School_class(key_c)
            if value_c:
                for key_s, value_s in value_c.items():
                    new_student = Student(value_s['name'], int(value_s['age']), value_s['sex'])
                    new_student.list_grades = value_s['list_grades']
                    new_class.add_student(new_student)
                    loaded_students += 1
            current_school.add_class(new_class)
            loaded_classes += 1
        
        print (f'\nLoad successful! Loaded {loaded_classes} classes and {loaded_students} students.')

        return current_school
    else:
        print('The file is empty!')
        return '0'

    
