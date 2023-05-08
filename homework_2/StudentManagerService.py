from StudentManagerImpl import StudentManagerImpl

class StudentManagerService:
    def __init__(self):
        self.__student_repo = StudentManagerImpl()

    def add_student(self, student): # 학생 추가
        #유효성 검사
        if not self.is_valid_student(student): 
            print("\n 학생 정보가 유효하지 않습니다.")
            return

        self.__student_repo.add_student(student)
        print(student.get_name()," 학생이 추가되었습니다.")

    def list_student(self): # 전체 학생 조회
        student_list = self.__student_repo.list_student()
        if len(student_list) == 0: 
            print("학생이 존재하지 않습니다.")
        else:
            for student in student_list:
                print("\n\t이름: "+student.get_name())
                print("\t학번: "+student.get_studentId())
                print("\t나이: "+student.get_age())
                print("\t전공: "+student.get_major())
                print("\t학점: "+student.get_gpa())
        # return self.__student_repo.list_student()

    def search_student(self, name): # 학생 조회
        search_list = self.__student_repo.search_student(name)
        if len(search_list)==0:
            print(name," 학생이 존재하지 않습니다.")
            return
        
        for student in search_list:
                print("\n\t이름: "+student.get_name())
                print("\t학번: "+student.get_studentId())
                print("\t나이: "+student.get_age())
                print("\t전공: "+student.get_major())
                print("\t학점: "+student.get_gpa())
        #return self.__student_repo.search_student(name)

    def delete_student(self, name): # 학생 제거
        deleted = self.__student_repo.delete_student(name)
        if deleted == False:
            print(name," 학생이 존재하지 않습니다.")
        else:
            print(name," 학생이 제거되었습니다.")


    def update_student(self, name, student): # 학생 수정
        #유효성 검사
        if not self.is_valid_student(student): 
            print("\n 학생 정보가 유효하지 않습니다.")
            return
        
        updated = self.__student_repo.update_student(name, student)
        if updated == False:
            print(name," 학생이 존재하지 않습니다.")
        else:
            print(name," 학생 정보가 수정되었습니다.")


    def list_student_by_gpa(self): #전체 학생 학점순 조회
        student_list = self.__student_repo.list_student()
        student_list.sort(key=lambda student: student.get_gpa(), reverse=True)
        for student in student_list:
            print("\t이름: ",student.get_name(),", 학점: ",student.get_gpa())

    #유효성 검사
    def is_valid_student(self,student):
        if student.get_studentId() == "" or student.get_name() == "" or student.get_major() == "" or student.get_gpa() == "":
            return False
        return True
    