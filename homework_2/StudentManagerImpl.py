from StudentManagerRepo import StudentManagerRepo

class StudentManagerImpl(StudentManagerRepo):
    def __init__(self):
        super().__init__()
        self.__studentList = []
    
    def add_student(self, student): # 학생 추가
        self.__studentList.append(student)
        
    def list_student(self): # 전체 학생 조회
        return self.__studentList

    def search_student(self, name): # 학생 조회
        search_list = []
        for student in self.__studentList:
            if student.get_name()== name:
                search_list.append(student)    
        return search_list
    
    def delete_student(self, name): # 학생 제거
        deleted = False
        for student in self.__studentList:
            if student.get_name() == name:
                self.__studentList.remove(student)
                deleted=True
        return deleted
    
    def update_student(self, name, new_student): # 학생 수정
        updated = False
        for student in self.__studentList:
            if student.get_name() == name:
                student.set_student_info(new_student.get_studentId(), new_student.get_name(), new_student.get_age(), new_student.get_major(), new_student.get_gpa())
                updated = True
        return updated

        