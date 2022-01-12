from school_class import School_class

class School:
    
    list_classes = []

    # init ?

    def add_class(self, school_class):
        self.list_classes.append(school_class)
    
    def remove_class(self, school_class):
        self.list_classes.remove(school_class)
    
    def list_all_classes(self):
        print ('\nClasses:')
        for sch_class in self.list_classes:
            print (sch_class.name)
        print ('\n')
