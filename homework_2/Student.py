class Student:
    def __init__(self,studentId,name,age,major,gpa):
        self.__studentId = studentId
        self.__name = name
        self.__age = age
        self.__major = major
        self.__gpa = gpa
    
    def get_studentId(self):
        return self.__studentId
    
    def get_name(self):
        return self.__name
    
    def get_age(self):
        return self.__age
    
    def get_major(self):
        return self.__major
    
    def get_gpa(self):
        return self.__gpa
    
    def set_studentID(self, studentId):
        self.__studentId = studentId

    def set_name(self, name):
        self.__name = name

    def set_major(self, major):
        self.__major = major

    def set_age(self, age):
        self.__age = age

    def set_gpa(self, gpa):
        self.__gpa = gpa

#학생정보 수정을 위해 사용
    def set_student_info(self,studentId,name,age,major,gpa):
            self.__studentId = studentId
            self.__name = name
            self.__age = age
            self.__major = major
            self.__gpa = gpa
