from StudentManagerImpl import StudentManagerImpl

class StudentManagerService:
    def __init__(self):
        self.__student_repo = StudentManagerImpl()

    def add_student(self, student): # 학생 추가
        self.__student_repo.add_student(student)

    def list_student(self): # 전체 학생 조회
        return self.__student_repo.list_student()

    def search_student(self, name): # 학생 조회
        return self.__student_repo.search_student(name)

    def delete_student(self, name): # 학생 제거
        self.__student_repo.delete_student(name)

    def update_student(self, name, student): # 학생 수정
        self.__student_repo.update_student(name, student)
    
    def list_student_by_gpa(self): #전체 학생 학점순 조회
        self.__student_repo.list_student_by_gpa()