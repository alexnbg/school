class Student:

    list_grades = []

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def add_grade(self, grade):
        self.list_grades.append(grade)
    
    def delete_grades(self):
        self.list_grades.clear
    
    @property
    def get_average(self):
        if len(self.list_grades) > 0:
            return sum(self.list_grades)/len(self.list_grades)
        else:
            return 0
