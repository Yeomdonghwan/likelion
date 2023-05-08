from StudentManagerRepo import StudentManagerRepo

class StudentManagerImpl(StudentManagerRepo):
    def __init__(self):
        super().__init__()
        self.__studentList = []

    
    def add_student(self, student): # 학생 추가
        #유효성 검사
        if student.get_studentId() =="" or student.get_name()=="" or student.get_major=="" or student.get_gpa=="":
            print("\n 학생 정보가 유효하지 않습니다.")
            return
        
        self.__studentList.append(student)
        print(student.get_name()," 학생이 추가되었습니다.")

        
    def list_student(self): # 전체 학생 조회
        if len(self.__studentList) == 0: 
            print("학생이 존재하지 않습니다.")
        else:
            for student in self.__studentList:
                print("\n\t이름: "+student.get_name())
                print("\t학번: "+student.get_studentId())
                print("\t나이: "+student.get_age())
                print("\t전공: "+student.get_major())
                print("\t학점: "+student.get_gpa())


    def search_student(self, name): # 학생 조회
        found=False
        for student in self.__studentList:
            if student.get_name()== name:    
                print("\n\t이름: "+student.get_name())
                print("\t학번: "+student.get_studentId())
                print("\t나이: "+student.get_age())
                print("\t전공: "+student.get_major())
                print("\t학점: "+student.get_gpa())
                found=True
        if found == False: 
            print(name," 학생이 존재하지 않습니다.")

    def delete_student(self, name): # 학생 제거
        found = False
        for student in self.__studentList:
            if student.get_name() == name:
                self.__studentList.remove(student)
                found=True
        if found == False:
            print(name," 학생이 존재하지 않습니다.")
        else:
            print(name," 학생이 제거되었습니다.")

    def update_student(self, name, new_student): # 학생 수정
        found = False
        for student in self.__studentList:
            if student.get_name() == name:
                student.set_student_info(new_student.get_studentId(), new_student.get_name(), new_student.get_age(), new_student.get_major(), new_student.get_gpa())
                found = True
        if found == False:
            print(name," 학생이 존재하지 않습니다.")
        else:
            print(name," 학생 정보가 수정되었습니다.")

    def list_student_by_gpa(self):
        if len(self.__studentList) == 0:
            print("학생이 존재하지 않습니다.")
            return
        
        self.__studentList.sort(key=lambda student: student.get_gpa(), reverse=True)
        for student in self.__studentList:
            print("\t이름: ",student.get_name(),", 학점: ",student.get_gpa())

        