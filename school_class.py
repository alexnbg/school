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
    
    @property
    def get_average(self):
        average = 0
        if len(self.list_students) > 0:
            for student in self.list_students:
                average += student.get_average()
            average = average/len(self.list_students)
            return average
        else:
            return 0
    
    def print_list(self):
        print ('\nStudents in {self.name} class:')
        if len(self.list_students) > 0:
            for student in self.list_students:
                print (student.name)
        else:
            print('   There are no students in this class!')
        print ('\n')
    
    def print_avegage(self):
        print ('\nAverage grades by students in {self.name} class:')
        if len(self.list_students) > 0:
            for student in self.list_students:
                print (student.name.ljust(20), str(round(student.get_average, 2)))
        else:
            print('   There are no students in this class!')
        print ('\n')
