class School_class:

    list_students = []

    def __init__(self, name):
        self.name = name
    
    def add_student(self, student):
        self.list_students.append(student)
    
    def remove_student(self, name):
        for student in self.list_students:
            if name == student.name:
                self.list_students(student)
    
    def print_list(self):
        print ('\nStudents in {self.name} class:')
        for student in self.list_students:
            print (student.name)
        print ('\n')
    
    def print_avegage(self):
        print ('\nAverage grades by students in {self.name} class:')
        for student in self.list_students:
            print (student.name.ljust(20), str(round(student.get_average, 2)))
        print ('\n')
