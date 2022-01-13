class Student:

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
        self.list_grades = []

    def add_grade(self, grade):
        self.list_grades.append(grade)
    
    def delete_grades(self):
        self.list_grades.clear
    
    @property
    def get_average(self):
        if self.list_grades:
            return sum(self.list_grades)/len(self.list_grades)
        else:
            return 0
