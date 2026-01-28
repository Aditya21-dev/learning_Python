class Student:
    def __init__(self, name, roll_no, course):
        self.name = name
        self.roll_no = roll_no
        self.course = course
        self.marks = []

    def add_marks(self, mark):
        self.marks.append(mark)

    def percentage(self):
        if not self.marks:
            return 0
        return sum(self.marks) / len(self.marks)

    def grade(self):
        p = self.percentage()
        if p >= 75:
            return "A"
        elif p >= 60:
            return "B"
        elif p >= 45:
            return "C"
        else:
            return "Fail"

    def details(self):
        return {
            "Name": self.name,
            "Roll": self.roll_no,
            "Course": self.course,
            "Marks": self.marks,
            "Percentage": self.percentage(),
            "Grade": self.grade()
        }


class Teacher:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject

    def give_marks(self, student, mark):
        student.add_marks(mark)


class College:
    def __init__(self, name):
        self.name = name
        self.students = []
        self.teachers = []

    def add_student(self, student):
        self.students.append(student)

    def add_teacher(self, teacher):
        self.teachers.append(teacher)

    def topper(self):
        if not self.students:
            return None
        return max(self.students, key=lambda s: s.percentage())

    def show_all_students(self):
        for student in self.students:
            print(student.details())

    def show_topper(self):
        t = self.topper()
        if t:
            print("Topper:", t.name, t.percentage())


s1 = Student("Adi", 101, "BCA")
s2 = Student("Rahul", 102, "BCA")
s3 = Student("Neha", 103, "BCA")

t1 = Teacher("Sharma Sir", "Python")
t2 = Teacher("Verma Ma'am", "DBMS")

t1.give_marks(s1, 80)
t1.give_marks(s1, 85)
t2.give_marks(s2, 65)
t2.give_marks(s2, 70)
t1.give_marks(s3, 40)
t2.give_marks(s3, 45)

college = College("Bhopal University")

college.add_student(s1)
college.add_student(s2)
college.add_student(s3)

college.add_teacher(t1)
college.add_teacher(t2)

college.show_all_students()
college.show_topper()
