import math

class Student:
    total_students = 0

    def __init__(self, student_id, name, dob):
        self.id = student_id
        self.name = name
        self.dob = dob
        self.courses = {}
        Student.total_students += 1

    def add_course(self, course_id, course_name, mark, course_credit):
        self.courses[course_id] = {
            "course_name": course_name,
            "mark": mark,
            "credit": course_credit,
        }

    def print_courses(self):
        for course_id, details in self.courses.items():
            print(
                f"Course ID: {course_id}, Course Name: {details['course_name']}, Mark: {details['mark']}, Credit: {details['credit']}"
            )

    @classmethod
    def get_total_students(cls):
        return cls.total_students

    def round_down(self, mark):
        origin_mark = mark
        mark *= 10
        mark = math.floor(mark)
        mark /= 10
        print("Successfully rounded down student score!")
        print(f"\nThe original mark {origin_mark} is downgraded to {mark}")

    def avg_gpa(self):
        total_weighted_marks = 0
        total_credits = 0

        for details in self.courses.values():
            total_weighted_marks += details["mark"] * details["credit"]
            total_credits += details["credit"]

        if total_credits == 0:
            return 0  # Avoid division by zero

        return total_weighted_marks / total_credits


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
            course_credit = int(input(f"Enter the credit for {course_name}: "))
            student.add_course(course_id, course_name, mark, course_credit)

        student_list.append(student)

    # Sort the student list by GPA in descending order
    sorted_students = sort_students_by_gpa_desc(student_list)

    print("\nClass Summary (Sorted by GPA Descending):")
    for student in sorted_students:
        print(f"\nStudent ID: {student.id}, Name: {student.name}, DOB: {student.dob}")
        student.print_courses()
        print(f"GPA: {student.avg_gpa():.2f}")

    print(f"\nTotal number of students: {Student.get_total_students()}")


def sort_students_by_gpa_desc(student_list):
    """
    Sorts the student list by GPA in descending order.
    """
    return sorted(student_list, key=lambda student: student.avg_gpa(), reverse=True)


if __name__ == "__main__":
    main()
