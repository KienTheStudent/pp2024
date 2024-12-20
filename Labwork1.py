student_list = []
student_management_list = []
def add_student(num_of_stu):
    for i in range(num_of_stu):
        id = input("Enter the id of that student: ")
        
        name = input("Enter the name of the student: ")
        student_list.append(name)
        dob = input("Enter the DOB (dd/mm/yyyy) of that student: ")
        
        course_num = int(input("Enter the number of his/her enrolled courses: "))
        course_id_list = []
        course_name_list = []
        mark_list=[]
        for j in range(course_num):
            course_id = input("Enter course's id: ")
            course_name = input("Enter the course name: ")
            course_id_list.append(course_id)
            course_name_list.append(course_name)
            mark = int(input("Enter the student mark: "))
            mark_list.append(mark)
            print("Student ",name, "get",mark,"at course",course_name)
        print("Id of enrolled cousre: ", course_id_list)
        print("Name of enrolled course respectively: ",course_name_list)
        
        student_management = {
            "id": id,
            "name": name,
            "dob": dob,
            "course_num": course_num
        }
        student_management_list.append(student_management)
    print("All students are all added")
add_student(2)