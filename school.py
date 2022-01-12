from school_class import School_class

class School:
    
    list_classes = []

    # init ?

    def add_class(self, school_class_name):
        self.list_classes.append(School_class(school_class_name))
    
    def remove_class(self, school_class_name):
        for sch_class in self.list_classes:
            if sch_class.name == school_class_name:
                self.list_classes.remove(sch_class)
                print(f'Class {school_class_name} successfully removed!')
    
    def print_all_classes(self):
        print ('\nList of all classes in the school:')
        if len(self.list_classes) > 0:
            print ('Name'.ljust(11), 'Students'.center(7), 'Average grades')
            for sch_class in self.list_classes:
                print (sch_class.name.ljust(11), str(len(sch_class.list_students)).center(7), str(round(sch_class.get_average, 2)).rjust(5))
            print ('\n')
            print ('- end of list -')
        else:
            print('   There are no classes in this school!')
    
    def print_classes_by_grade(self):
        print ('\nList of all classes in the school by grades:')
        if len(self.list_classes) > 0:
            temp = self.list_classes
            def get_av_grades(cl):
                return cl.get_average
            temp.sort(key=get_av_grades)
            for sch_class in temp:
                print(sch_class.name.ljust(11),str(round(sch_class.get_average, 2)).ljust(6))
        else:
            print('   There are no classes in this school!')
