from school import School
from school_class import School_class
from student import Student

import json


file_name = 'data.txt'



def _data_for_save(school:School):
    data = {}

    for sch_class in school.list_classes:
        data[sch_class.name] = {}
        if sch_class.list_students:
            for student in sch_class:
                data[sch_class.name][student.name] = {}
                data[sch_class.name][student.name]['name'] = student.name
                data[sch_class.name][student.name]['age'] = student.age
                data[sch_class.name][student.name]['sex'] = student.sex
                data[sch_class.name][student.name]['list_grades'] = student.list_grades

    return data




def save_json(school:School):
    data = _data_for_save(school)

    with open(file_name, 'w') as outfile:
        json.dump(data, outfile)
    
    print ('Save successful!')


def load_json():
    current_school = School()

    with open(file_name) as json_file:
        data = json.load(json_file)

    if data:
        for sch_class, vc in data:
            new_class = School_class(sch_class)
            if vc:
                print(sch_class)
                for student, vs in sch_class:
                    print(student)
                    new_student = Student(vs['name'], int(vs['age']), vs['sex'])
                    new_student.list_grades = vs['list_grades']
                    new_class.add_student(new_student)
            current_school.add_class(new_class)
    
    print ('Load successful!')

    return current_school




#with open('data.txt', 'w') as outfile:
#    json.dump(data, outfile)
