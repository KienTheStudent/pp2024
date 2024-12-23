class Student:
    total_students = 0

    def __init__(self, student_id, name, dob):
        self.id = student_id
        self.name = name
        self.dob = dob
        self.courses = {}
        Student.total_students += 1

    def add_course(self, course_id, course_name, mark):
        self.courses[course_id] = {"course_name": course_name, "mark": mark}

    def print_courses(self):
        for course_id, details in self.courses.items():
            print(f"Course ID: {course_id}, Course Name: {details['course_name']}, Mark: {details['mark']}")

    @classmethod
    def get_total_students(cls):
        return cls.total_students


class DS(Student):
    def speak(self):
        return "I am the best"


class ICT(Student):
    def speak(self):
        return "How can I find an intern job??"


class CS(Student):
    def speak(self):
        return "I want to be a hacker"


# Main Logic
def main():
    num_students = int(input("Enter the number of students in the class: "))
    student_list = []

    for _ in range(num_students):
        student_id = input("Enter student ID: ")
        name = input("Enter student name: ")
        dob = input("Enter student DOB (dd/mm/yyyy): ")
        student = Student(student_id, name, dob)

        num_courses = int(input(f"Enter the number of courses {name} is enrolled in: "))
        for _ in range(num_courses):
            course_id = input("Enter course ID: ")
            course_name = input("Enter course name: ")
            mark = int(input(f"Enter the mark for {course_name}: "))
            student.add_course(course_id, course_name, mark)

        student_list.append(student)

    print("\nClass Summary:")
    for student in student_list:
        print(f"\nStudent ID: {student.id}, Name: {student.name}, DOB: {student.dob}")
        student.print_courses()

    print(f"\nTotal number of students: {Student.get_total_students()}")

if __name__ == "__main__":
    main()
