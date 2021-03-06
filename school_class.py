from student import Student
import utilities

class School_class:

    def __init__(self, name:str):
        self.name = name
        self.list_students = []
    
    def add_student(self, student:Student):
        self.list_students.append(student)
    
    def add_new_student(self, name:str, age:int, sex:str):
        self.list_students.append(Student(name, age, sex))
    
    def remove_student(self, name:str):
        for student in self.list_students:
            if name == student.name:
                self.list_students.remove(student)
    
    @property
    def get_average(self):
        average = 0
        if self.list_students:
            for student in self.list_students:
                average += student.get_average
            average = average/len(self.list_students)
            return average
        else:
            return 0

    def get_students_by_gender(self, sex:str):
        if self.list_students:
            list_gender = [x.sex for x in self.list_students if x.sex == sex]
            return len(list_gender)
        else:
            return 0
    
    def get_list_average_grade(self):
        if self.list_students:
            return [x.get_average for x in self.list_students]
        else:
            return 0
    
    def get_list_average_grade_by_gender(self, sex:str):
        if self.list_students:
            return [x.get_average for x in self.list_students if x.sex == sex]
        else:
            return 0
    
    def get_list_age(self):
        if self.list_students:
            return [x.age for x in self.list_students]
        else:
            return 0

    def print_list(self):
        print (f'\nStudents in {self.name} class:')
        if self.list_students:
            for student in self.list_students:
                print (student.name)
        else:
            print('   There are no students in this class!')
    
    def print_grades(self):
        print (f'\nStudents in {self.name} class:')
        if self.list_students:
            print ('Name'.ljust(21), 'Age'.center(5), 'Gender'.center(8), 'Average grade'.center(13), '  All grades')
            for student in self.list_students:
                print (student.name.ljust(21), str(student.age).center(5), student.sex.center(8), str(round(student.get_average, 2)).center(13), '  ', student.list_grades)
            print ('\n- end of list -')
        else:
            print('   There are no students in this class!')
