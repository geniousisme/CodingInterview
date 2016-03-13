def grade2(subject):
    print "lalalalal"

class Student(object):
    def __init__(self, name, number):
        self.name       = name
        self.number     = number
        self.grade_hash = {"Chinese": 96, "Math": 100}

    def grade(self, subject):
        try:
            return self.grade_hash[subject]
        except KeyError:
            print "don't take this test la!"

if __name__ == "__main__":
    student = Student("Chris", 19)
    print student.name
    print student.number

    student.grade("Math")